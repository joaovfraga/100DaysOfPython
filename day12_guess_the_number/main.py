from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
chosen_number = random.randint(1, 100)


# print(f"Pssst, the correct answer is {chosen_number}")


def guessing_the_number(difficulty_func):
    global chosen_number

    if difficulty_func == "easy":
        attempts_numbers = 10

        while attempts_numbers > 0:
            print(f"You have {attempts_numbers} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if attempts_numbers == 1 and guess != chosen_number:
                attempts_numbers -= 1
            elif guess > chosen_number:
                attempts_numbers -= 1
                print("Too High")
                print("Guess again.")
            elif guess < chosen_number:
                attempts_numbers -= 1
                print("Too Low")
                print("Guess again.")
            else:
                print(f"You got it! The answer was {chosen_number} 😜")
                return
        print("You've run out of guesses, you lose.")
        return

    else:
        attempts_numbers = 5

        while attempts_numbers > 0:
            print(f"You have {attempts_numbers} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if attempts_numbers == 1 and guess != chosen_number:
                attempts_numbers -= 1
            elif guess > chosen_number:
                attempts_numbers -= 1
                print("Too High")
                print("Guess again.")
            elif guess < chosen_number:
                attempts_numbers -= 1
                print("Too Low")
                print("Guess again.")
            else:
                print(f"You got it! The answer was {chosen_number}")
                return
        print("You've run out of guesses, you lose.")
        return


difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

guessing_the_number(difficulty)
