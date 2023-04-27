from dotenv import load_dotenv
import os
import openai
import requests
import json
import sys

load_dotenv()

def main(query: str):
    openai.organization = os.getenv("ORG_ID")
    openai.api_key = os.getenv("API_KEY")
    gpt_35(query, openai)

def gpt_35(prompt: str, api: openai):
    
    endpoint = "https://api.openai.com/v1/chat/completions" #POST
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api.api_key}"}
    body = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"{query}"}]
    }
    
    response = requests.post(url=endpoint, json=body, headers=headers).json()
        
    gpt_response = response["choices"][0]["message"]["content"]
    print(f"\"{gpt_response}\"") # Send to alfred viewer
    
    save_path = os.getenv("RESPONSE_PATH")
    
    with open(save_path, "w") as f:
        json.dump(response, f, indent=4) # Save last response to file
    
if __name__ == "__main__":
    query = sys.argv[1]
    main(query)
    