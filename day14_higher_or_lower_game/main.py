import random
from art import logo, vs
from game_data import data


def higher_lower_game():
    print(logo)

    end_game = True
    score = 0

    while end_game:
        chosen_randoms = random.choices(data, k=2)
        random1 = chosen_randoms[0]
        random2 = chosen_randoms[1]

        a = random1
        b = random2

        print(f"Compare A: {a.get('name')}, a {a.get('description')}, from {a.get('country')}.")
        print(vs)
        print(f"Compare B: {b.get('name')}, a {b.get('description')}, from {b.get('country')}.")
        who_has_more = input("Who has more followers? Type 'A' or 'B': ").lower()

        if a.get('follower_count') > b.get('follower_count') and who_has_more == a:
            score += 1
            a = b
            print(f"You're right! Current score: {score}")
        elif a.get('follower_count') > b.get('follower_count') and who_has_more == b:
            print(f"Sorry, that's wrong. Final score: {score}")
            end_game = False
        elif a.get('follower_count') < b.get('follower_count') and who_has_more == a:
            print(f"Sorry, that's wrong. Final score: {score}")
            end_game = False
        elif a.get('follower_count') < b.get('follower_count') and who_has_more == b:
            score += 1
            a = b
            print(f"You're right! Current score: {score}")

        # Alternativas para esse if statement

        # if a_followers > b_followers:
        #     if guessing == a_followers:
        #         return True
        #     else:
        #         return False
        # else:
        #     if guessing == b_followers:
        #         return True
        #     else:
        #         return False

        # if a_followers > b_followers:
        #     return guess == "a"
        # else:
        #     return guess == "b"
higher_lower_game()
