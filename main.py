# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            if(len(opening_brackets_stack) == 0 or are_matching(opening_brackets_stack[-1][0], next ) == False):
                return(i+1)
            else:
                return("Success")



def main():
    input = input("Ievadiet F vai I un nospiediet enter!")
    if input == "I":

        text = input()
        mismatch = find_mismatch(text)
        if (mismatch == "Sucess"):
            print("Success")
        else:
            print(mismatch)
        

if __name__ == "__main__":
    main()
