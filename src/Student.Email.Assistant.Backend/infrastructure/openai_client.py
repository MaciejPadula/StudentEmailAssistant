from openai import OpenAI
import os


def call_openai_api(messages, temperature = 0.9, max_tokens = 250):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=openai_api_key)
    
    return client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    
# [
#     {
#     "role": "system",
#     "content": [
#         {
#         "type": "text",
#         "text": """
# You have to search for a product by it's name. Here is an input provided from user.\nPlease provide a list of product names in english on which you can filter the products. Return as mauch as you can please :). Result should be a JSON list of strings!!!! And do not add json word at the beginning.
# """
        
#         }
#     ]
#     },
#     {
#     "role": "user",
#     "content": [
#         {
#         "type": "text",
#         "text": search_phrase
#         }
#     ]
#     }
# ]
