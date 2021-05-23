from random import randint
from art import logo

print(logo)
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


def guessing_game(number_of_guesses):
    game_over = False
    counter = number_of_guesses
    correct_number = randint(1, 101)
    print(correct_number)
    while not game_over:
        guess = int(input("Make a guess: "))
        if guess == correct_number:
            print(f"That's it, you win! The number was {correct_number}.")
            game_over = True
        elif guess > correct_number:
            print("Too High\nGuess again.")
            counter -= 1
            if counter == 0:
                print(f"You've run out of guesses, you lose.\nThe number was: {correct_number}.")
                game_over = True
                break
            print(f"You have {counter} attempts remaining to guess the number")
        elif guess < correct_number:
            print("Too Low.\nGuess again")
            counter -= 1
            if counter == 0:
                print(f"You've run out of guesses, you lose.\nThe number was: {correct_number}.")
                game_over = True
                break
            print(f"You have {counter} attempts remaining to guess the number")

if difficulty == 'easy':
    number_of_guesses = 10
    print(f"You have {number_of_guesses} attempts remaining to guess the number.")
elif difficulty == 'hard':
    number_of_guesses = 5
    print(f"You have {number_of_guesses} attempts remaining to guess the number.")
else:
    print("Good bye!")

guessing_game(number_of_guesses)