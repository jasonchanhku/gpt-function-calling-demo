import requests
from src.sys_config import system_instruction
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#GPT_MODEL = "gpt-3.5-turbo-16k-0613" 
GPT_MODEL = "gpt-4-0613" 
messages = [
    {"role": "system", "content": system_instruction}
]

functions = [
    {
        "name": "get_current_weather", # name of your function
        "description": "Get the current weather", # description of your function
        "parameters": {
            "type": "object",
            "properties": { # 1st argument of your function
                "location": { # argument name
                    "type": "string", # argument type
                    "description": "The city and state, e.g. San Francisco, CA", # description of your function with example
                }
            },
            "required": ["location"], # required argument of your
        },
    },
    {
    "name": "get_top_headlines",
    "description": "Get top news headlines by country and/or category",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Freeform keywords or a phrase to search for.",
            },
            "country": {
                "type": "string",
                "description": "The 2-letter ISO 3166-1 code of the country you want to get headlines for",
            },
            "category": {
                "type": "string",
                "description": "The category you want to get headlines for",
                "enum": ["business","entertainment","general","health","science","sports","technology"]
            }
        },
        "required": [],
    }
}
]

def chat_completion_request(messages, functions=None, function_call=None, model=GPT_MODEL):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + OPENAI_API_KEY,
    }
    json_data = {
        "model": model, 
        "messages": messages
        }
    if functions is not None:
        json_data.update({"functions": functions})
    if function_call is not None:
        json_data.update({"function_call": function_call})
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=json_data,
        )

        return response
    except Exception as e:
        print(f"\n>>>> Unable to generate ChatCompletion response")
        print(f"\n>>>> Exception: {e}")
        raise e