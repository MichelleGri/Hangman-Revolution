import random

movies_list = ["Harry Potter", "Lord of the Rings", "The Godfather"]

"""
variable to choose a random movie from movies list
"""
movie = random.choice(movies_list)
print(movie)

"""
display "_" for movie
"""

display_movie = []
movie_length = len(movie)
for letter in range(movie_length):
    if letter == "":
        continue
    else:
        display_movie += "_"
print(display_movie)


"""
ask player to guess a letter
"""
guessed_letter = input("Please guess a letter\n").lower()
print(guessed_letter)

"""
check if guessed letter is in the movie
"""

for p in range(movie_length):
    letter = movie[p]
    if letter == guessed_letter:
        display_movie[p] = letter

print(display_movie)
