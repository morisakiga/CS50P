"""
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
"""

def get_guess():
    guess = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    guess = guess.lower().strip()
    return guess


def main():
    answer = ["42", "forty two", "forty-two"]
    
    guess = get_guess()
    if guess in answer:
        print("Yes")
    else:
        print("No")


main()
