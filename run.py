import random

movies_list = ["Harry Potter", "Lord of the Rings", "The Godfather"]

"""
variable to choose a random movie from movies list
"""
secret_movie = random.choice(movies_list)
print(secret_movie)

"""
ask player to guess a letter
"""
guessed_letter = input("Please guess a letter\n").lower()
print(guessed_letter)

"""
check if guessed letter is in the secret movie
"""
for letter in secret_movie:
    if letter == guessed_letter:
        print("You have guessed the correct letter!")
    else:
        print(f"The letter {guessed_letter} is not in the secret movie!")