import random
yes_or_no=input("speacial character (y/n):")
if yes_or_no=="y":
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?']
    special_choice=random.choice(special_characters)
password_len=input()

character=random.randint(1,9)
print(character,special_choice)