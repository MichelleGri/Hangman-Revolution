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
guessed_letter = input("Please guess a letter!\n").lower()
print(guessed_letter)

s