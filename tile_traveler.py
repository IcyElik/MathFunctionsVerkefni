# Have player position pos_row and pos_col  start 1,1
# rows = 3 columns = 3
# func moves(column, row) and returns where he can move
    # if sentence to retrun the right moves (print)
# func move(direction) and call func moves with new position (player pos_row pos_col)
# when player enters pos_col = 3 and pos_row= 1

def directions(column, row):
    """
    returns where the player can go
    """
    valid_direction = ""
    if  possition == "1,1" or possition == "2,1" or possition == "2,1":
        valid_direction = "(n)orth"
    elif possition == "1,2" or possition == "3,2":
        valid_direction = "(n)orth, (s)outh"
    elif possition == "1,3":
        valid_direction = "(s)outh, (e)ast"
    elif possition == "2,3":
        valid_direction = "(e)ast, (w)est"
    elif possition == "3,3" or possition == "2,2":
        valid_direction = "(w)est, (s)outh"
    else:
        #victory
    return valid_direction
def move(direction):
    """ 
    moves the player and returns new position 
    """
# Main program

possition = "1,1"

while pos_col != 3 and pos_row != 1:
    where_to_go = str(input())