import openai

openai.api_key = "your-openai-api-key"

def query_openai(prompt, conversation_context):
    full_prompt = f"{conversation_context}\nUser: {prompt}\nBot:"
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=full_prompt[-2000:],  # Limit the length to avoid large payloads
        max_tokens=150
    )
    return response.choices[0].text.strip()
