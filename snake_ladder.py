import random
print("Welcome to the GAME")
print("Let's start the Snake and Ladder Game")
p1 = input("Enter first player name: ")
p2 = input("Enter second player name: ")
cursor1 = 0
cursor2 = 0
while(cursor1 != 100 and cursor2 != 100):
    print()
    print("Let's start the next move")
    print("Heyy", p1)
    inp = input("Enter 'roll' to roll the dice: ")
    if(inp == "roll"):
        current = random.randint(1, 6)
        print("Dice gives", current)
        if(cursor1+current <= 100):
            cursor1 += current
        if(cursor1 == 2):
            print("Hurray you got a ladder")
            cursor1 = 23
        if(cursor1 == 8):
            print("Hurray you got a ladder")
            cursor1 = 12
        if(cursor1 == 17):
            print("Hurray you got a ladder")
            cursor1 = 93
        if(cursor1 == 29):
            print("Hurray you got a ladder")
            cursor1 = 54
        if(cursor1 == 62):
            print("Hurray you got a ladder")
            cursor1 = 78
        if(cursor1 == 70):
            print("Hurray you got a ladder")
            cursor1 = 89
        if(cursor1 == 99):
            print("Ayoo, snake killed you")
            cursor1 = 4
        if(cursor1 == 59):
            print("Ayoo, snake killed you")
            cursor1 = 37
        if(cursor1 == 41):
            print("Ayoo, snake killed you")
            cursor1 = 20
        if(cursor1 == 31):
            print("Ayoo, snake killed you")
            cursor1 = 14
        if(cursor1 == 67):
            print("Ayoo, snake killed you")
            cursor1 = 50
        if(cursor1 == 92):
            print("Ayoo, snake killed you")
            cursor1 = 76
        print(p1, "you are currently on", cursor1)
        print()
    else:
        print("Invalid Option selected")
    print("Now it's", p2, "'s turn")
    print("Heyy ", p2)
    inp = input("Enter 'roll' to roll the dice: ")
    if(inp == "roll"):
        current = random.randint(1, 6)
        print("Dice gives", current)
        if(cursor2+current <= 100):
            cursor2 += current
        if(cursor2 == 2):
            print("Hurray you got a ladder")
            cursor2 = 23
        if(cursor2 == 8):
            print("Hurray you got a ladder")
            cursor2 = 12
        if(cursor2 == 17):
            print("Hurray you got a ladder")
            cursor2 = 93
        if(cursor2 == 29):
            print("Hurray you got a ladder")
            cursor2 = 54
        if(cursor2 == 62):
            print("Hurray you got a ladder")
            cursor2 = 78
        if(cursor2 == 70):
            print("Hurray you got a ladder")
            cursor2 = 89
        if(cursor2 == 99):
            print("Ayoo, snake killed you")
            cursor2 = 4
        if(cursor2 == 59):
            print("Ayoo, snake killed you")
            cursor2 = 37
        if(cursor2 == 41):
            print("Ayoo, snake killed you")
            cursor2 = 20
        if(cursor2 == 31):
            print("Ayoo, snake killed you")
            cursor2 = 14
        if(cursor2 == 67):
            print("Ayoo, snake killed you")
            cursor2 = 50
        if(cursor2 == 92):
            print("Ayoo, snake killed you")
            cursor2 = 76
        print(p2, "you are currently on", cursor2)
        print()
    else:
        print("Invalid Option selected")
