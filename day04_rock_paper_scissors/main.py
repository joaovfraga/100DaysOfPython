import random

random_number = random.randint(0, 2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

number_chosen = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))

if number_chosen == 0:
    print("You chose Rock:")
    print(rock)
elif number_chosen == 1:
    print("You chose Paper:")
    print(paper)
else:
    print("You chose Scissors:")
    print(scissors)

print("Computer chose:")

if random_number == 0:
    print("Rock")
    print(rock)
elif random_number == 1:
    print("Paper")
    print(paper)
elif random_number == 2:
    print("Scissors")
    print(scissors)

if (number_chosen == 0 and random_number == 0) or (number_chosen == 1 and random_number == 1) or (number_chosen == 2 and random_number == 2):
    print("It's a draw")
elif (number_chosen == 0 and random_number == 2) or (number_chosen == 2 and random_number == 1) or (number_chosen == 1 and random_number == 0):
    print("You win!")
else:
    print("You lose")