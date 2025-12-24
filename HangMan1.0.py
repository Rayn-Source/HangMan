from pickle import TRUE
count = 6
someWords = []
blank_list = []
correct_guess = False
blank = ""

print("Welcome to HangMan")

Words = "mango,orange,grape,apricot,lemon,coconut,watermelon,,peach,muskmelon"
someWords = Words.split(",")
value = int(input("Enter a number between 1-9 to choose a word from array: "))
chosenWord = someWords[value -1]
blank_list = ["_"] * len(chosenWord)

try:
    while int(value) >9:
        print("Please enter a number below 10")  
        break
except:
    print("Please enter a number and not string")

else:
    while not correct_guess:
        guess = input("Please key in a character: ")
        

        if guess in chosenWord:
            for i in range(len(chosenWord)):
                if chosenWord[i] == guess:
                    blank_list[i] = guess
                    print(' '.join(blank_list))
        else:
            count -= 1
            print("There is no", guess)
            print("Remaining tries:", count)

        if count == 0:
            print("Game Over")
            break

        if "_" not in blank_list:
            correct_guess = True
            print("Congrats! You won!")

   

       

    
    
