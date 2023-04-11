from replit import clear #clears console after each guess. Function called in at line 28

import random

#Importing the word list from from hangman_words.py 
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word) 

end_of_game = False
lives = 6 #keeping track of lives/limbs of hangman

#Importing the logo from hangman_art.py + stages from hangman_art.py that corresponds to current no. of lives left
from hangman_art import logo, stages
print(logo)

#Testing code to help us debug along the way. Gives answer!
print(f'Pssst, the solution is {chosen_word}.')

#Converting all the letters in chosen word to "_"
display = []
for _ in range(word_length):
    display += "_"
#Allows user to keep guessing, links to end_of_game = False line 11. The true condition set at the end line 53
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    #What will show if the user enters a letter they've already guessed
    if guess in display:
        print(f"You've already guessed {guess}")

    #Looping through the word and replacing the "_" for the users guessed letter if it is a correct guess.
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Reducing lives by 1 if the guessed letter is not in chosen word. If lives hit 0, end of the game
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.\n Game Over")

    #[From tricky challenge 4 vid]Joining all the elements in the list and turn it into a String]
    print(f"{' '.join(display)}")

    #Checking if user has guessed ALL of the letters correctly.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #calling in "stages" from line 14
    print(stages[lives])