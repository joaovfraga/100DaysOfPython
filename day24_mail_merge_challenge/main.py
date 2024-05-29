PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as names:
    names_listed = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in names_listed:
        new_name = name.strip("\n")
        new_letter = letter_content.replace(PLACEHOLDER, new_name)

        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)



