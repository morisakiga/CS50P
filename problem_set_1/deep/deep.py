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
