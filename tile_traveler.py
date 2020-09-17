# Have player position pos_row and pos_col  start 1,1
# rows = 3 columns = 3
# func moves(column, row) and returns where he can move
    # if sentence to retrun the right moves (print)
# func move(direction) and call func moves with new position (player pos_row pos_col)
# when player enters pos_col = 3 and pos_row= 1

def directions(pos_col, pos_row):
    """
    returns where the player can go
    """
    valid_direction = ""
    if  (pos_col == 1 and pos_row == 1) or (pos_col == 2 and pos_row == 1):
        valid_direction = "(n)orth"
    elif (pos_col == 1 and pos_row == 2) or (pos_col == 3 and pos_row == 2):
        valid_direction = "(n)orth, (s)outh"
    elif (pos_col == 1 and pos_row == 3):
        valid_direction = "(s)outh, (e)ast"
    elif (pos_col == 2 and pos_row == 3):
        valid_direction = "(e)ast, (w)est"
    elif (pos_col == 3 and pos_row == 3) or (pos_col == 2 and pos_row == 2):
        valid_direction = "(w)est, (s)outh"
    return valid_direction

def move(direct, pos_col, pos_row):
    direct = direct.lower()
    if direct == "n":
        if (pos_col == 1 and pos_row == 1) or (pos_col == 2 and pos_row == 1):
            pos_row += 1
            return (pos_col, pos_row)
        elif (pos_col == 1 and pos_row == 2) or (pos_col == 3 and pos_row == 2):
            pos_row += 1
            return (pos_col, pos_row)
    elif direct == "s":
        if (pos_col == 1 and pos_row == 2) or (pos_col == 3 and pos_row == 2):
            pos_row -= 1
            return (pos_col, pos_row)
        elif (pos_col == 1 and pos_row == 3):
            pos_row -= 1
            return (pos_col, pos_row)
        elif (pos_col == 3 and pos_row == 3) or (pos_col == 2 and pos_row == 2):
            pos_row -= 1
            return (pos_col, pos_row)
    elif direct == "e":
        if (pos_col == 1 and pos_row == 3):
            pos_col += 1
            return (pos_col, pos_row)
        elif (pos_col == 2 and pos_row == 3):
            pos_col += 1
            return (pos_col, pos_row)
    elif direct == "w":
        if (pos_col == 2 and pos_row == 3):
            pos_col -= 1
            return (pos_col, pos_row)
        elif (pos_col == 3 and pos_row == 3) or (pos_col == 2 and pos_row == 2):
            pos_col -= 1
            return (pos_col, pos_row)
    else:
        print("Not a valid input!")
        return pos_col, pos_row

    """ 
    moves the player and returns new position 
    """
# Main program

pos_col = 1
pos_row = 1

while pos_col != 3 or pos_row != 1:
    moves = directions(pos_col, pos_row)
    print("You can travel: " + moves)
    move_pos = input("Direction: ")
    pos_col, pos_row = move(move_pos, pos_col, pos_row)
print("Victory!")