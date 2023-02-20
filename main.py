# python3

from collections import namedtuple 

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for y, next in enumerate(text):
        if next in "([{":
        # Process opening bracket, write your code here
            bra = Bracket (next, y + 1)
            opening_brackets_stack.append(bra)

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return y + 1
            xx = opening_brackets_stack.pop()
            if not are_matching(xx.char, next):
                return y + 1

    if opening_brackets_stack:
        return opening_brackets_stack[0].position

    return "Success"

def main():
    # Printing answer, write your code here
    wee = input("F or I")
    if "F" in wee:
        file_name = input("Enter file name: ")
        with open(file_name, "r", encoding="latinl") as file:
            text = file.read()
        mismatch = find_mismatch(text)
        if mismatch == "Success":
            print("Success")
        else:
            print(mismatch)
    elif "I" in wee:
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == "Sucess":
            print("Success")
        else:
            print(mismatch)

if __name__ == "__main__":
    main()
