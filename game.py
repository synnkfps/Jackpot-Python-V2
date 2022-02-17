import random

# chars
seven = '[ 7️⃣ ]' 
cherries = '[ 🍒 ]'
orange = '[ 🍊 ]'

# table
row1 = {0:'0', 1:'0', 2:'0'}
row2 = {0:'0', 1:'0', 2:'0'}
row3 = {0:'0', 1:'0', 2:'0'}

# more duplicates = more chances to get more combinations
charList = [seven, cherries, orange]

# game
def game():
    print(f'{row1[0]} {row1[1]} {row1[2]}\n{row2[0]} {row2[1]} {row2[2]}\n{row3[0]} {row3[1]} {row3[2]}')
    option = input('Re-roll?\n1. Yes\n2. No\n>  ')
    if (option == "y" or option == "yes" or option == "1"):
        randomizer()
        game()
    elif (option == "n" or option == "no" or option == "2"):
        exit()
    else:
        print("I don't recognize this option. Returning to game.")
        game()
            
# randomizer system
def randomizer():
    random.shuffle(charList)
    # change table
    row1[0] = random.choice(charList)
    row2[0] = random.choice(charList)
    row3[0] = random.choice(charList)

    row1[1] = random.choice(charList)
    row2[1] = random.choice(charList)
    row3[1] = random.choice(charList)

    row1[2] = random.choice(charList)
    row2[2] = random.choice(charList)
    row3[2] = random.choice(charList)
    check()

def check():
    # Y Axis
    if (row1[0] == row2[0] == row3[0]):
        print("Y1")
    elif (row1[1] == row2[1] == row3[1]):
        print("Y2")
    elif (row1[2] == row2[2] == row3[2]):
        print("Y3")
    else:
        pass
    # X Axis
    if (row1[0] == row1[1] == row1[2]): 
        print("X1")
    elif (row2[0] == row2[1] == row2[2]):
        print("X2")
    elif (row3[0] == row3[1] == row3[2]):
        print("X3")
    else:
        pass
    # Z Axis
    if (row1[0] == row2[1] == row3[2] or row3[2] == row2[1] == row1[0]): 
        print("Z1-Z3")
    elif (row3[0] == row2[1] == row1[2] or row1[2] == row2[1] == row3[0]):
        print("Z3-Z1")
    else:
        pass

# Start automatically
game()
    

    
    
