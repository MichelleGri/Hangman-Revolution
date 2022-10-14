import random
from hangman_movies import movies_list
from hangman_stages import stages


def main():
    """
    main function to set initial values
    """
    print("Let's play Hangman!")
    game_over = False
    player_lives = 6
    guessed_letters = []
    print(stages[player_lives])

    random_movie()
    display_movie()
    guess_letter()
    check_guess()


def random_movie():
    """
    function to choose a random movie from list
    """
    movie = random.choice(movies_list)
    return movie.upper()


def display_movie(movie):
    """
    function to display "_" for movie name
    """
    display = []

    for letter in movie:
        print(letter)
        if letter == " ":
            display += " "
        else:
            display += "_"
    return display
        

def guess_letter():
    """
    ask player to guess a letter
    """
    guess = input("Please guess a letter\n").upper()
    guess += guessed_letters
    return guess
    

def check_guess(guess, movie):
    """
    function to check guess
    """
    if len(guess) == 1 and guess.isalpha():
        if guess in display:
            print(f"You have aleady guessed the letter {guess}")

        for p in range(len(movie)):
            letter = movie[p]
            if letter == guess:
                display[p] = letter
                print("You guessed a correct letter!")
            
        print(display)

        if guess not in movie:
            player_lives -= 1
            print(f"The letter {guess} is not in this movie, you lose a life!")
            if player_lives == 0:
                game_over = True
                print("You lost the game!")

        if "_" not in display:
            game_over = True
            print("Congratulations! You guessed the correct movie!")

        print(stages[player_lives])

    else:
        print("Invalid guess, please enter letters from A-Z only!")


while not game_over:
    guess_letter()
    check_guess()
    

    
