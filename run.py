import random
from hangman_movies import movies_list

"""
variable to choose a random movie from movies list
"""
movie = random.choice(movies_list)
print(movie)

player_lives = 6

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

check if guessed letter is in the movie
"""
game_over = False

while not game_over:
    guessed_letter = input("Please guess a letter\n").lower()
    print(guessed_letter)

    for p in range(movie_length):
        letter = movie[p]
        if letter == guessed_letter:
            display_movie[p] = letter
            
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

    print(hangman_stages[player_lives])

