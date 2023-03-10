from collections import namedtuple
Bracket = namedtuple("Bracket", ["char", "position"])
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for  i, next in enumerate(text):

        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
    
        if next in ")]}":
            if(len(opening_brackets_stack) == 0 or are_matching(opening_brackets_stack[-1][0], next) == False):
                print(i+1)
                return 0
            opening_brackets_stack.pop()

    return opening_brackets_stack
    
def main():
    ievade = input()
    if 'I' in ievade:
        text = input()
    elif 'F' in ievade:
        print("Ievadiet ceļu līdz teksta failam: ")
        ievade = input()
        text = open(ievade, "r").readline()
    mismatch = find_mismatch(text)
    if mismatch == 0:
        pass
    elif(len(mismatch) != 0 ):
        print(mismatch[-1][1])
    else:
        print("Success")

if __name__ == "__main__":
    main()
