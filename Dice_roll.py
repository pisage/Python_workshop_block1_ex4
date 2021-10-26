import random

def Dice_roll(roll_result):
    try:
        x = int(input("Give the number of rolls: "))
        y = int(input("Gice the type of the roll: "))
        z = int(input("Give an additional value of the roll: "))
        dice_type = {3, 4, 6, 8, 10, 12, 20, 100}

        if y in dice_type:
            print(f"Your dice and roll parameters: {x}D{y}+{z}")
        else:
            print("Wrong type of roll")
    except ValueError:
        print("Give only numbers")

    roll_result = (random.randint(1, y) * x) + z
    print("Your roll result is: ",roll_result)

    return roll_result






