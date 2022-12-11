import os
import sys
import openai
from random import choice as rc

davinci_txt = 'txt_files/davinci.txt'

chars = ["!", "@", "#", "$", "%", "^", "&", "*"]

# Create a function that takes a string as input and returns a gpt response
def gpt_response(prompt):
    openai.api_key = os.getenv("API_KEY")
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = prompt,
        max_tokens = 2000,
        temperature = 0.3,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0.6,

    )
    print_prompt_to_file(prompt, response.choices[0].text)
    return response.choices[0].text


def get_prompt():
    prompt = input("What is your prompt? ")
    return prompt

def print_prompt_to_file(prompt, response):
    char = rc(chars)
    with open(davinci_txt, 'a') as f:
        f.write(f"{char*50}\nPrompt: {prompt}\nResponse: {response}\n{char*50}")
        f.close()

def return_response(prompt):
    response = gpt_response(prompt)
    return response

def main():
    flag = True
    while flag:
        prompt = get_prompt()
        if prompt == 'q':
            flag = False
        else:
            response = gpt_response(prompt)
            print(response)

if __name__ == "__main__":
    main()






