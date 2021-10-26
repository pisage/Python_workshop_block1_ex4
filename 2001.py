import random

comp_points = 0
user_points = 0
dice_type = {3, 4, 6, 8, 10, 12, 20, 100}

#pierwsza runda

print("Computer roll.")
comp_dice_choice = int(random.choice(["3", "4", "6", "8", "10", "12", "20", "100"]))
comp_roll = (random.randint(1, comp_dice_choice)) + (random.randint(1, comp_dice_choice))
comp_points = comp_points + comp_roll
print("Computer points:", comp_points)


print("User roll.")
user_dice_choice = int(input("Give the type of the roll (3, 4, 6, 8, 12, 20, 100: "))
if user_dice_choice in dice_type:
    user_roll = (random.randint(1, user_dice_choice)) + random.randint(1, user_dice_choice)
    if user_roll == 7:
        user_points = user_points // 7
    elif user_roll == 11:
        user_points = user_points * 11
    else:
        user_points = user_points + user_roll
    print("User points:", user_points)
else:
    print("Wrong type of roll")


user_roll = (random.randint(1, 6) * 2)
user_points = user_points + user_roll
print("User points:", user_points)

#od drugiej rundy

while (int(comp_points) < 2001) or (int(user_points) < 2001):

    print("Computer roll")
    comp_dice_choice = int(random.choice(["3", "4", "6", "8", "10", "12", "20", "100"]))
    comp_roll = (random.randint(1, comp_dice_choice)) + (random.randint(1, comp_dice_choice))
    if comp_roll == 7:
        comp_points = comp_points // 7
    elif comp_roll == 11:
        comp_points = comp_points * 11
    else:
        comp_points = comp_points + comp_roll
    print("Computer points:", comp_points)


    print("User roll.")
    user_dice_choice = int(input("Give the type of the roll (3, 4, 6, 8, 12, 20, 100: "))
    if user_dice_choice in dice_type:
        user_roll = (random.randint(1, user_dice_choice)) + random.randint(1, user_dice_choice)
        if user_roll == 7:
            user_points = user_points // 7
        elif user_roll == 11:
            user_points = user_points * 11
        else:
            user_points = user_points + user_roll
        print("User points:", user_points)
    else:
        print("Wrong type of roll")

    if comp_points > 2001:
        print(comp_points)
        print("Computer won")
        break
    elif user_points > 2001:
        print(user_points)
        print("User won")
        break