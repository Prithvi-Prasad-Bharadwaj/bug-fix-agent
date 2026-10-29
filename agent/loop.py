import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types
from agent.tools import read_file, edit_file, run_tests
from agent.prompts import SYSTEM_PROMPT

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "gemini-3.5-flash"
MAX_STEPS = 8
PAUSE_SECONDS = 13   # free tier allows about 5 requests per minute
MAX_RETRIES = 3

TOOLS = {
    "read_file": read_file,
    "edit_file": edit_file,
    "run_tests": run_tests,
}


def ask_gemini(contents, config):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            time.sleep(PAUSE_SECONDS)
            return client.models.generate_content(model=MODEL, contents=contents, config=config)
        except Exception as e:
            text = str(e)
            if "PerDay" in text:
                raise
            temporary = "503" in text or "429" in text
            if not temporary or attempt == MAX_RETRIES:
                raise
            wait = 60 if "429" in text else 20
            print(f"Gemini is busy, waiting {wait}s then retrying...")
            time.sleep(wait)


def fix_repo(repo_folder):
    task = f"The tests in the folder '{repo_folder}' may be failing. Check them and fix the bug if there is one."
    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        tools=[read_file, edit_file, run_tests],
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
    )
    contents = [types.Content(role="user", parts=[types.Part(text=task)])]

    for step in range(1, MAX_STEPS + 1):
        response = ask_gemini(contents, config)
        contents.append(response.candidates[0].content)

        if not response.function_calls:
            print(f"[step {step}] robot finished")
            return response.text

        results = []
        for call in response.function_calls:
            print(f"[step {step}] robot calls {call.name} with {dict(call.args)}")
            tool = TOOLS[call.name]
            output = tool(**call.args)
            results.append(types.Part.from_function_response(name=call.name, response={"result": output}))
        contents.append(types.Content(role="user", parts=results))

    return f"Stopped: reached the limit of {MAX_STEPS} steps."