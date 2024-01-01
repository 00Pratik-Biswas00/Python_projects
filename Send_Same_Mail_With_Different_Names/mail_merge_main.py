changeable_letter = "[name]"
with open("Input/Names/invited_names.txt", "r") as data:
    invited_names = data.readlines()

with open("Input/Letters/starting_letter.txt") as data:
    starting_letter = data.read()
    for name in invited_names:
        new_name = name.strip()
        new_letter = starting_letter.replace(changeable_letter, new_name)
        with open(f"Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as allDone:
            allDone.write(new_letter)















