# LLM-BullsAI

This is a training program generator created for the BullsAI company. It makes use of the [Assistant API](https://platform.openai.com/) by OpenAI and the [OpenAI API](https://openai.com/index/openai-api/). The UI is created using [Streamlit](https://streamlit.io/).

## Requirements

1. Create a ".env" file with the following:

- OPENAI_API_KEY =
- ASSISTANT_ID =
- SENDER_EMAIL =
- SENDER_PASSWORD = (This is a 16-digit code for APP passwords from Google)

## Instalation

1. Create a python virtual env:

Windows (Command Prompt):

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

2. Activate the virtual env:

```bash
python3 -m venv venv
```

Or:

```bash
python3 -m venv venv
```

3. Install the requirements.txt

```bash
pip install -r requirements.txt
```

4. Run the streamlit application

```bash
streamlit run main.py
```
