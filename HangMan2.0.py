#The code starts by importing the random module.
import random
from collections import counter

someWords = ["apple, banana, mango, strawberry,orange,grape, pineapple, apricot, lemon, coconut, watermelon,cherry, papaya, berry, peach, lychee, muskmelon"]

#This module provides a way to generate random numbers.


# randomly choose a secret word from our "someWords" LIST.
word = random.choice(someWords)

#Next, the code creates someWords, which is a list of fruit names.

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

#The list is split into spaces using the string ' ', and then each space is replaced with a letter.
    for i in word:
        # For printing the empty spaces for letters of the word
        print('_', end=' ')
    print()
#Next, the code randomly selects a secret word from our someWords list.



#This word will be used as the input for the game later on.

#The next part of the code checks to see if the user has entered an alpha character (a letter that appears in front of other letters).

#If not, then they are asked to enter only a letter.

#If they enter an alpha character, then it's assumed that they want to guess at another letter in word .

#So, this part of the code checks to see if guess matches one of the letters in word .

#If it does, then chances is updated and flag is set to 1 .

#Otherwise, chances is decreased by 1 and flag remains at 0 .

#The next part of the code tries to guess at another letter in word .

#If guess isn't valid (i.e., it doesn't match any of the letters in word ), then print() prints out all empty spaces for letters in word , and

#The code starts by importing the random module.

#This module provides us with a number of useful functions, one of which is the choice function.

#This function allows us to randomly choose a secret word from our list of words.

#Next, we create some variables which will be used throughout the program.

#These include someWords , word and letterGuessed .

#letterGuessed will store the letter guessed by the player, while chances will store the number of times that the player has correctly guessed the word so far.

#correct will keep track of how many letters have been guessed so far and flag will indicate whether or not the player has guessed the word correctly.

#We then start looping through our list of words and randomly choosing a secret word from it.