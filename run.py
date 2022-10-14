import random
from hangman_movies import movies_list
from hangman_stages import stages

"""
choose a random movie from movies list

set player lives to 6

number of letters in movie name

set initial game over state to false

"""

movie = random.choice(movies_list).upper()
player_lives = 6
movie_length = len(movie)
game_over = False

"""
display "_" for movie name
"""

display_movie = []

for letter in range(movie_length):
    if letter == " ":
        continue
    else:
        display_movie += "_"

"""
ask player to guess a letter

check if guessed letter is in the movie
"""


while not game_over:
    guessed_letter = input("Please guess a letter\n").upper()
    print(guessed_letter)

    if guessed_letter in display_movie:
        print(f"You have aleady guessed the letter {guessed_letter}")

    for p in range(movie_length):
        letter = movie[p]
        if letter == guessed_letter:
            display_movie[p] = letter
            print("You guessed a correct letter!")
            
    print(display_movie)

    if guessed_letter not in movie:
        player_lives -= 1
        print(f"The letter {guessed_letter} is not in this movie, you lose a life.")
        if player_lives == 0:
            game_over = True
            print("You lost the game!")

    if "_" not in display_movie:
        game_over = True
        print("Congratulations! You guessed the correct movie!")

    print(stages[player_lives])

