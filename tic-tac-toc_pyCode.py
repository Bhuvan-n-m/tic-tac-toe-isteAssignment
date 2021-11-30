rows=3
cols=3
game_board = [["___" for i in range(cols)] for j in range(rows)]
mark = '_X_'

def print_game_board():
        for row in game_board:
            for item in row:
                print(item, end=" ")
            print()

def enter_choice(prow,pcol,mark):
    game_board[prow][pcol]=mark

def check_win(mark):
        win = None

        n = len(game_board)

        #for checking win because of row marks
        for i in range(n):
            win = True
            for j in range(n):
                if game_board[i][j] !=mark:
                    win = False
                    break
            if win:
                return win

        #for checking win because of column marks
        for i in range(n):
            win = True
            for j in range(n):
                if game_board[j][i] != mark:
                    win = False
                    break
            if win:
                return win

        #for checking win because of diagonal marks
        win = True
        for i in range(n):
            if game_board[i][i] != mark:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if game_board[i][n - 1 - i] != mark:
                win = False
                break
        if win:
            return win
        return False

        
        for row in game_board:
            for item in row:
                if item == '___':
                    return False
        return True

def check_draw():
        for row in game_board:
            for item in row:
                if item == '___':
                    return False
        return True

def swap_playermak():
    if mark == '_X_':
        return '_O_'
    else :
        return '_X_'


while True:
            print(f"{mark}'s turn : ")

            print_game_board()

            prow=int(input("Enter row number : "))
            pcol=int(input("Enter Column number : "))

            enter_choice(prow-1,pcol-1,mark)

            if check_win(mark):
                print(f"Player {mark} wins the game!")
                break
            
                
            if check_draw():
                print("Match is a draw since all spots are filled")
                break
            

            mark = swap_playermak()
            
            print_game_board()