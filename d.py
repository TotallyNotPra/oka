

import requests
import json



api_key = ""

print("from here")
conversation = []
while True:
    messages = input("you:")
    if messages == "No":
        break
    conversation.append({"role": "user", "content": messages})
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers ={"authorization":f"Bearer {api_key}"},
        json ={
            "model": "qwen/qwen3-coder-30b-a3b-instruct",
            "messages":[{"role":"user","content": messages}]
            
        }
    )
    print("response",response.status_code)
    ai_response = response.json()["choices"][0]["message"]["content"]
    print("ai", ai_response)
    conversation.append({"role": "assistant", "content": ai_response})
    print()
    









