import random

NUM_SIDES = 6

def roll_dice():
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print("Total of two dice:", total)

def main():
    die1: int = 10  # This variable is not used in roll_dice, just shown in main() for demonstration.
    print("die in main() starts as:", die1)
    
    # Roll the dice 3 times
    roll_dice()
    roll_dice()
    roll_dice()

    print("die in main() is:", die1)

main()
