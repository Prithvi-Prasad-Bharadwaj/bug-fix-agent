import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from agent.tools import read_file, edit_file, run_tests
from agent.prompts import SYSTEM_PROMPT

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def fix_repo(repo_folder):
    task = f"The tests in the folder '{repo_folder}' may be failing. Check them and fix the bug if there is one."
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=task,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=[read_file, edit_file, run_tests],
        ),
    )
    return response.text