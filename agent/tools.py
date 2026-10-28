def read_file(path):
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
    with open(path, "w") as f:
        f.write(new_content)
    return "File updated"