import random
from hangman_movies import movies_list
from hangman_stages import stages

"""
choose a random movie from list

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
        display_movie += " "
    else:
        display_movie += "_"

"""
ask player to guess a letter

check if guessed letter is in the movie
"""

while not game_over:
    guess = input("Please guess a letter\n").upper()

    if len(guess) == 1 and guess.isalpha():

        if guess in display_movie:
            print(f"You have aleady guessed the letter {guess}")

        for p in range(movie_length):
            letter = movie[p]
            if letter == guess:
                display_movie[p] = letter
                print("You guessed a correct letter!")
            
        print(display_movie)

        if guess not in movie:
            player_lives -= 1
            print(f"The letter {guess} is not in this movie, you lose a life!")
            if player_lives == 0:
                game_over = True
                print("You lost the game!")

        if "_" not in display_movie:
            game_over = True
            print("Congratulations! You guessed the correct movie!")

    else:
        ("Invalid guess, please guess letters from A-Z only!")

        print(stages[player_lives])
    

