# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    flag = True
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            if(len(opening_brackets_stack) == 0 or are_matching(opening_brackets_stack[-1][0], next ) == False):
                print(i+1)
                return False
            opening_brackets_stack.pop()


def main():
    text = input()
    mismatch = find_mismatch(text)
    if (mismatch == False):
        pass
    else:
        print("Success")

if __name__ == "__main__":
    main()
