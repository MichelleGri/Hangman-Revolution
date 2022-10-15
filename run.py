import random
import sys
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
    print("\n")

    while not game_over and player_lives > 0:
        guess = input("Please guess a letter:\n\n").upper().strip()
        print("\n")

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You have aleady guessed the letter {guess},\n\nplease guess a different letter!")
                print("\n")

            elif guess not in movie:
                print(f"The letter {guess} is not in this movie!")
                print("\n")
                player_lives -= 1
                guessed_letters += guess
            
            else:
                for position in range(movie_length):
                    letter = movie[position]
                    if letter == guess:
                        display[position] = letter
                print(f"{' '.join(display)}")
                print("\n")
                print(f"Well done! {guess} is in the movie!")
                print("\n")
                guessed_letters += guess

                if "_" not in display:
                    game_over = True
                    print("Congratulations! You guessed the correct movie!")
                    print("\n")
        
            if player_lives == 0:
                game_over = True
                print(f"You lost the game!\n\nThe movie was {movie}!")
                print("\n")
            
            print(stages[player_lives])

        else:
            print("Invalid guess, please enter letters from A-Z only!")
            print("\n")


def main():
    """
    main function to set initial values
    """
    movie = random_movie()
    play_game(movie)

    play_again = input(f"Do you want to play again? Y/N:\n").upper().strip()
    print("\n")
    while play_again == "Y":
        main()
    if play_again == "N":
        print("Thank you for playing!")
        sys.exit()


main()
