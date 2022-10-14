import random
from hangman_movies import movies_list
from hangman_stages import stages


def random_movie():
    """
    function to choose a random movie from list

    display underscores for number of letters in movie
    """
    movie = random.choice(movies_list)
    return movie.upper()


def play_game(movie):
    """
    function to play game
    ask player to guess a letter
    """
    print("Let's play Hangman!")
    player_lives = 6
    print(stages[player_lives])
    game_over = False
    guessed_letters = []
    display = []
    movie_length = len(movie)

    for letter in movie:
        if letter == " ":
            display += " "
        else:
            display += "_"
    print(' '.join(display))

    while not game_over and player_lives > 0:
        guess = input("Please guess a letter:\n").upper().strip()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You have aleady guessed the letter {guess}")

            elif guess not in movie:
                print(f"The letter {guess} is not in this movie!")
                player_lives -= 1
                guessed_letters.append(guess)
        
            else:
                for position in range(movie_length):
                    letter = movie[position]
                    if letter == guess:
                        display[position] = letter
                print(f"{' '.join(display)}")
                print(f"Well done! {guess} is in the movie!")
        
                if player_lives == 0:
                    game_over = True
                    print("You lost the game!")

                if "_" not in display:
                    game_over = True
                    print("Congratulations! You guessed the correct movie!")
            
            print(stages[player_lives])

        else:
            print("Invalid guess, please enter letters from A-Z only!")


def main():
    """
    main function to set initial values
    """
    movie = random_movie()
    play_game(movie)


main()