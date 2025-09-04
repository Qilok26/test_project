import random

energy = 10
move_count = 1

def do_move():
    global energy
    rand_chance = random.randint(1, 10)
    if rand_chance > 3:
        print("You found food. +3 Energy")
        energy += 3
    elif rand_chance < 5:
        print("Nothing happened")
    else:
        print("You lost 2 energy")
        energy -= 2

def rest():
    global energy
    print("You rested up, gained 2 energy, but wasted a move")
    energy += 2

def randomizer():
    global energy
    print("Welcome to the randomizer, guess my number from 1 to 5")
    rand_chance = random.randint(1, 5)
    user_input = int(input("Enter your guess: "))
    if user_input == rand_chance:
        print("Congratulations, you guessed the number!!! It was:", rand_chance)
        energy += 5
    else:
        print("You guessed wrong, the number was:", rand_chance)
        energy -= 2

print("Welcome to the game! To win, get more than 20 energy in the least number of moves.")

while energy > 0 and energy < 20:
    print("\nYour energy is:", energy, ". Move number:", move_count)
    print("1. Move\n2. Rest\n3. Randomizer")
    
    try:
        main_input = int(input("Choose an action (1, 2, or 3): "))
    except ValueError:
        print("Invalid input. Minus 2 energy.")
        energy -= 2
        continue

    if main_input == 1:
        do_move()
    elif main_input == 2:
        rest()
    elif main_input == 3:
        randomizer()
    else:
        print("You entered an incorrect value. Minus 2 energy.")
        energy -= 2
        
    move_count += 1


if energy <= 0:
    print("Womp womp, you lost.")
else:
    print("Congratulations, you won!!! You did it in", move_count-1, "moves.")
