import openai
import os
import time
import json
from prompt import prompt

# Set up your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to retrieve the assistant
def retrieve_assistant(assistant_id):
    try:
        print(f"Retrieving assistant with ID: {assistant_id}")
        assistant = openai.beta.assistants.retrieve(assistant_id)
        print("Assistant retrieved successfully")
        return assistant
    except Exception as e:
        print(f"Error retrieving assistant: {str(e)}")
        return None

# Function to create a new thread
def create_thread():
    try:
        print("Creating a new thread")
        thread = openai.beta.threads.create()
        print(f"Thread created with ID: {thread.id}")
        return thread
    except Exception as e:
        print(f"Error creating thread: {str(e)}")
        return None

# Function to chat with the assistant
def chat_with_assistant(thread, assistant_id, user_message):
    for attempt in range(3):  # Try 3 times
        try:
            print(f"Adding user message to thread: {user_message}")
            openai.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=user_message
            )
            print("Message added successfully")
            print("Running the assistant")
            run = openai.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=assistant_id
            )
            print(f"Run created with ID: {run.id}")
            
            while True:
                print("Waiting for run to complete")
                time.sleep(1)
                run = openai.beta.threads.runs.retrieve(
                    thread_id=thread.id,
                    run_id=run.id
                )
                print(f"Current run status: {run.status}")
                
                if run.status == "failed":
                    print("Run failed, retrieving detailed information:")
                    print(f"Run details: {run}")
                    break
                elif run.status == "completed":
                    print("Run completed, retrieving assistant's response")
                    messages = openai.beta.threads.messages.list(thread_id=thread.id)
                    assistant_response = messages.data[0].content[0].text.value
                    print(f"Assistant response: {assistant_response}")
                    return assistant_response, None
                elif run.status == "requires_action":
                    print("Run requires action, processing function call")
                    tool_calls = run.required_action.submit_tool_outputs.tool_calls
                    tool_outputs = []
                    
                    for tool_call in tool_calls:
                        function_name = tool_call.function.name
                        function_args = json.loads(tool_call.function.arguments)
                        
                        if function_name == "generate_training_plan":
                            print(f"Calling O1-preview model for function: {function_name}")
                            print(f"Arguments: {function_args}")
                            
                            # Call O1-preview model
                            o1_response = call_o1_preview_model(function_args)
                            
                            tool_outputs.append({
                                "tool_call_id": tool_call.id,
                                "output": json.dumps(o1_response)
                            })
                    
                    print("Submitting tool outputs")
                    run = openai.beta.threads.runs.submit_tool_outputs(
                        thread_id=thread.id,
                        run_id=run.id,
                        tool_outputs=tool_outputs
                    )
                else:
                    print(f"Waiting for run to complete. Current status: {run.status}")
                    
        except Exception as e:
            print(f"Attempt {attempt + 1}: Error in chat_with_assistant: {str(e)}")
            time.sleep(2)  # Wait a bit before retrying
    
    return "Failed to retrieve a response after multiple attempts.", None

def call_o1_preview_model(function_args):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Replace with actual O1-preview model identifier
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": json.dumps(function_args)}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"Error calling O1-preview model: {str(e)}")
        return "Error generating workout plan"

# Conduct interview function
def conduct_interview():
    print("Starting the interview. Type 'exit' to end the interview.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response, function_result = chat_with_assistant(thread, assistant.id, user_input)
        print(f"Assistant: {response}")

        if function_result:
            print(f"Function Result: {function_result}")
            break

# Run the interview
assistant_id = "asst_6nRA1lLnXj4JMZw1RGLKegmN"
assistant = retrieve_assistant(assistant_id)

if assistant:
    thread = create_thread()
    if thread:
        conduct_interview()
