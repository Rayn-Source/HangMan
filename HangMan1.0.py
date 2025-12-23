#1. Welcome to HangMan! And initiliazation 
print("Welcome to HangMan")
print_array = []
blank = ""
count = 5

#2. Choose a number between 1-17 to choose a word from array
someWords = ["apple, banana, mango, strawberry,orange,grape, pineapple, apricot, lemon, coconut, watermelon,cherry, papaya, berry, peach, lychee, muskmelon"]

try:
    value = int(input("Enter a number between 1-17 to choose a word from array"))
except:
    print("Please enter a number and not string")

chosenWord = someWords[value -1]
#3. Choose a letter 
chosenWord_array = list(chosenWord)
for letters in chosenWord_array:
    if(input("Please enter a letter/character") == letters):
        blank += "_"
        print_array = list(blank)       

#4.If a letter is choosen, if it is not right it will display hangman
    else:
        print(count - 1)

#5.If the letter of the word in the array is correct it will display on the terminal
print(' '.join(print_array))


if(count <=0):
    print("Game Over")
else:
    print("Congrats you guessed the word")
#6.Congrats!