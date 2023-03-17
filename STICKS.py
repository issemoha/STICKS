sticks = 25
print("This program is for a game called 21 sticks.")
print("In this game there are 21 sticks and you have to 1-3 sticks each turn.")
print("But, the way you win is by not taking the last stick")
print("Will you win agaisnt the Overlord or will you fail like so many others.")
while True:
    print("There are: ", sticks)  ## prints how many sticks are left
    sticks_taken = int(input("Take sticks (1-4): "))  ## user input that asks how many sticks to take
    if sticks == 1:
        print("You got the last stick you lose")
        break

    if sticks_taken > 4 and sticks_taken <= 0:
        print("You can't pick amount that's not between 1-4") ## checks for an invalid number 18 Take
        continue
    print("Computer took: ", (5- sticks_taken))
    sticks -= 5
    ## the math for the ai that allows it to win everytime