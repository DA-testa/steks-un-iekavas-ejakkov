# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])
from tkinter.filedialog import askopenfilename


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

opening_brackets_stack = []

def find_mismatch(text):
    global opening_brackets_stack
    for  i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
        if next in ")]}":
            if(len(opening_brackets_stack) == 0 or are_matching(opening_brackets_stack[-1][0], next) == False):
                print(i+1)
                return 0
            opening_brackets_stack.pop()


        

def main():
    ievade = input()
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == 0:
        pass
    elif(len(opening_brackets_stack) != 0 ):
        print(opening_brackets_stack[-1][1])
    else:
        print("Success")

if __name__ == "__main__":
    main()
