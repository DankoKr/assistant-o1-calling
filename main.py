import os
import time
import json
import streamlit as st
from openai import OpenAI
from prompt import prompt

# Set up your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to retrieve the assistant
def retrieve_assistant(assistant_id):
    try:
        assistant = client.beta.assistants.retrieve(assistant_id)
        return assistant
    except Exception as e:
        st.error(f"Error retrieving assistant: {str(e)}")
        return None

# Function to create a new thread
def create_thread():
    try:
        thread = client.beta.threads.create()
        return thread
    except Exception as e:
        st.error(f"Error creating thread: {str(e)}")
        return None

# Function to chat with the assistant
def chat_with_assistant(thread, assistant_id, user_message):
    for attempt in range(3):  # Try 3 times
        try:
            client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=user_message
            )
            run = client.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=assistant_id
            )

            while True:
                time.sleep(1)
                run = client.beta.threads.runs.retrieve(
                    thread_id=thread.id,
                    run_id=run.id
                )

                if run.status == "failed":
                    st.error("An error occurred while processing your request.")
                    return None, None
                elif run.status == "completed":
                    messages = client.beta.threads.messages.list(thread_id=thread.id)
                    assistant_response = messages.data[0].content[0].text.value
                    return assistant_response, None
                elif run.status == "requires_action":
                    tool_calls = run.required_action.submit_tool_outputs.tool_calls
                    tool_outputs = []

                    for tool_call in tool_calls:
                        function_name = tool_call.function.name
                        function_args = json.loads(tool_call.function.arguments)

                        if function_name == "generate_training_plan":
                            o1_response = call_o1_preview_model(function_args)
                            tool_outputs.append({
                                "tool_call_id": tool_call.id,
                                "output": json.dumps(o1_response)
                            })

                    run = client.beta.threads.runs.submit_tool_outputs(
                        thread_id=thread.id,
                        run_id=run.id,
                        tool_outputs=tool_outputs
                    )

        except Exception as e:
            if attempt == 2:  # Last attempt
                st.error(f"Error in chat_with_assistant: {str(e)}")
            time.sleep(2)  # Wait a bit before retrying

    return "Failed to retrieve a response after multiple attempts.", None

def call_o1_preview_model(function_args):
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Replace with actual O1-preview model identifier
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": json.dumps(function_args)}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error calling O1-preview model: {str(e)}")
        return "Error generating workout plan"

# Streamlit UI
def main():
    st.title("OpenAI Assistant Chat")

    # Initialize session state
    if 'assistant' not in st.session_state:
        st.session_state.assistant = None
    if 'thread' not in st.session_state:
        st.session_state.thread = None
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Sidebar for assistant ID input
    assistant_id = st.sidebar.text_input("Enter Assistant ID", "asst_6nRA1lLnXj4JMZw1RGLKegmN")

    if st.sidebar.button("Initialize Assistant"):
        with st.spinner("Initializing assistant..."):
            st.session_state.assistant = retrieve_assistant(assistant_id)
            if st.session_state.assistant:
                st.session_state.thread = create_thread()
                st.success("Assistant initialized successfully!")

    # Main chat interface
    if st.session_state.assistant and st.session_state.thread:
        st.write("Chat with the assistant. Type 'exit' to end the conversation.")

        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # User input
        if prompt := st.chat_input("You:"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            if prompt.lower() != 'exit':
                with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    # Get assistant response
                    with st.spinner("Assistant is thinking..."):
                        response, function_result = chat_with_assistant(st.session_state.thread, st.session_state.assistant.id, prompt)
                    
                    if response:
                        message_placeholder.markdown(response)
                        st.session_state.messages.append({"role": "assistant", "content": response})

                    # Display function result if any
                    if function_result:
                        st.json(function_result)
            else:
                st.write("Conversation ended.")

if __name__ == "__main__":
    main()