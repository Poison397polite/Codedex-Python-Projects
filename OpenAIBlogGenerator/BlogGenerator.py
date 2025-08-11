"""Program that uses openai to generate a blog on a topic"""

import openai
from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config['API_KEY']

def generateBlog(paragraphTopic):
    response = openai.completions.create(
        model = 'gpt-4o-mini'
        prompt = "Write a paragraph about the following topic. " + paragraphTopic,
        max_tokens = 400,
        temperature = 0.3
    )
    
    retrieveBlog = response.choices[0].text
    
    return retrieveBlog

keepWriting = True

while keepWriting:
    answer = input("Write a paragraph? Y for yes, anything else for no. ")
    if answer == "Y":
        paragraphTopic = input("What should this paragraph talk about? ")
        print(generateBlog(paragraphTopic))
    else:
        keepWriting = False
