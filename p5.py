# Heads or Tails

from random import choice # choice is a function that randomly chooses from a list

while True:
    print("Welcome to our heads or tails game!")
    print("Please choose either heads or tails.")
    while True:
        guess = input("Heads or Tails? ")
        guess = guess.lower() # makes everything lower case

        if guess in {"heads", "tails", "head", "tail"}:
            break
        else:
            print("Please enter heads or tails.")

    flip_result = choice(["heads", "tails"])

    if guess in {"heads", "head"} and flip_result == "heads":
        print(f"The computer flipped {flip_result}! You Win!")
    elif guess in {"tails", "tail"} and flip_result == "tails":
        print(f"The computer flipped {flip_result}! You Win!")
    else:
        print(f"The computer flipped {flip_result}! You Lose!")

    user_input = input("Want to play again: Yes/no ")
    user_input = user_input.lower()
    if user_input == "yes":
        continue
    else:
        break

print("Thanks for playing!")