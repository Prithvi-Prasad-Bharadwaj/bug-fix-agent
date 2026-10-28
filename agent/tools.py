import subprocess
import sys

def read_file(path):
    """Read a file and return its text."""
    with open(path, "r") as f:
        return f.read()
    
'''
open(path, "r") --> opens a file for reading ("r" means read).
with --> as f opens it and closes it automatically when done.
f is the open file. It has a method called .read() that gives back all its text.
f.read() --> f is the open file, and .read() gives back all the text inside it.

open(path, "r") is you opening a book.
f is the book, now open in your hands.
f.read() is reading everything written in that book.

means “open this file for reading, and call the opened file f”. After that, f.read() means “read the text from the file we called f”.

f is only a name. You could call it anything.
Ex:with open(path, "r") as my_file:
    return my_file.read()
This works exactly the same way. Programmers use f because it’s short.

What with does: when the indented lines finish, Python closes the book for you. You don’t have to remember to close it.
'''

def edit_file(path, new_content):
    """Overwrite a file with new_content. Send the WHOLE new file, because the old text is erased."""
    with open(path, "w") as f:
        f.write(new_content)
    return "File updated"

def run_tests(repo_folder):
    """Run pytest inside repo_folder and return the test report. Use this to see what fails and to check a fix."""
    result = subprocess.run(
        [sys.executable, "-m", "pytest"],
        cwd=repo_folder,
        capture_output=True,
        text=True,
    )
    return result.stdout