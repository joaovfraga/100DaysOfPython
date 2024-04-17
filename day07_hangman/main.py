import random
import hangman_words
import hangman_arts

# Poderia ser: from hangman_arts import stages, logo

stages = hangman_arts.stages
logo = hangman_arts.logo
print(logo)

lives = 6

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)

# Creating an empty list with "_"
for letter in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])

    #Join all the elements in the list and turn it into a String (a prof que fez)
    print(f"{' '.join(display)}")
    #print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")
    elif lives == 0:
        end_of_game = True
        print("You lose")