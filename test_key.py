''' import os
print(os.getcwd()) '''

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
#Reads your .env file and loads the settings inside it into memory. After this line, GEMINI_API_KEY is available to your program. Without it, Python would not know your key exists.

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

'''
This line has three parts, read from the inside out:

--> os.getenv("GEMINI_API_KEY") means “get the value of the setting named GEMINI_API_KEY”, which is your key.
--> genai.Client(api_key=...) creates a connection to Gemini that uses that key.
--> client = ... stores the connection in a name called client, so we can reuse it.

Think of client as a phone already dialed to Gemini.
'''
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Say hello in one short sentence.",
)

'''
--> response = client.models.generate_content : Using the phone, ask a Gemini model to generate something. Whatever Gemini sends back is stored in response.
-->     model="gemini-3.5-flash" : Which Gemini model to ask. “Flash” is the fast, light one. Models are like different employees, and this one is quick.
--> contents="Say hello in one short sentence." : Your question, called the prompt. The ) closes the bracket we opened above.

'''
print(response.text)