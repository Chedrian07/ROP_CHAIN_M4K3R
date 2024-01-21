from openai import OpenAI
import os
import time
import sys



client = OpenAI(
    api_key=os.getenv("OPENAI_API"),
)


def check_api():
    if client.api_key is None:
        raise Exception("Please set your OPENAI_API environment variable.") 
    else:
        print("API is set")
        
        
def seek_info():
    file_path = sys.argv[1]
    output = os.popen(f"python seek_info.py {file_path}").read()
    print(output)


def set_ai():
    model = "gpt-3.5-turbo"
    prompt = "I will give you some information for make ROP_CHAIN with pwntools"
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role" : "System", "content" : prompt},
        ]
    )
    
    print(response)


if __name__ == "__main__":
    check_api()
    seek_info()
    set_ai()