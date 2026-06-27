import random
print("Hi! there so today we are going to play a guess the number game!")
print("I will think of a number between 1 and 50, and you have to guess it.")
print("You will have 5 attempts to guess the number correctly.")
print("let's begin!")

no = random.randint(1, 50)
i = int(input("Enter your 1st guess: "))
if i == no:
    print("Congratulations! You guessed the number correctly.")
else:
    print("Sorry, that's not the correct number.")
    print("You have 4 more lives.")
    i = int(input("Enter your 2nd guess: "))
    if i == no:
        print("Congratulations! You guessed the number correctly.")
    else:
        print("Sorry, that's not the correct number.")
        print("You have 3 more lives.")
        i = int(input("Enter your 3rd guess: "))
        if i == no:
            print("Congratulations! You guessed the number correctly.")
        else:
            print("Sorry, that's not the correct number.")
            print("You have 2 more lives.")
            i = int(input("Enter your 4th guess: "))
            if i == no:
                print("Congratulations! You guessed the number correctly.")
            else:
                print("Sorry, that's not the correct number.")
                print("You have 1 more life.")
                i = int(input("Enter your 5th guess: "))
                if i == no:
                    print("Congratulations! You guessed the number correctly.")
                else:
                    print("Sorry, that's not the correct number.")
                    print(f"The correct number was {no}.")