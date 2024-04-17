from art import logo
import random
from replit import clear


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(card_list):
    """Take a list of cards and return the score calculated from the cards"""
    score = sum(card_list)

    if score == 21 and len(card_list) == 2:
        # the if could be: if 11 in card_list and 10 in card_list and len(card_list) == 2
        return 0

    if 11 in card_list and score > 21:
        card_list.remove(11)
        card_list.append(1)

    return score


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw 🫂"
    elif computer_score == 0:
        return "You lose. The opponent has Blackjack 🥲"
    elif user_score == 0:
        return "You win! With a Blackjack😜"
    elif user_score > 21:
        "You lose 🥲"
    elif computer_score > 21:
        return "You win! 🥰"
    elif user_score > computer_score:
        return "You win! 🥰"
    else:
        return "You lose 🥲"


def play_game():

    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
            print("You lose 🥹")
        else:
            draw_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_another_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has
    # a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
