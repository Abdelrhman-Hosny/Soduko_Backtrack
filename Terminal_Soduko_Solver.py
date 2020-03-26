# Soduko A.H

board1 =[
[3,7,5,6,2,0,0,0,4],
[4,9,2,3,0,8,0,5,6],
[0,0,0,0,9,4,0,7,0],
[7,4,8,1,5,0,6,3,2],
[1,2,0,8,6,0,0,4,5],
[6,5,9,2,0,3,7,0,0],
[2,0,4,7,3,6,5,8,9],
[0,8,6,4,1,5,3,2,0],
[0,3,7,0,8,2,0,6,1]
]

board2= [
[0,7,0,0,0,4,0,0,0],
[0,0,8,0,0,3,2,0,5],
[5,0,0,6,0,0,0,0,0],
[0,2,0,0,0,1,0,0,0],
[0,8,3,0,0,2,1,9,0],
[6,0,0,0,0,0,5,2,0],
[0,0,0,1,4,0,0,0,8] ,   
[0,0,0,0,0,0,0,0,2],
[9,0,0,0,0,0,6,3,1]
]




PossibleSolutions = [1,2,3,4,5,6,7,8,9]




def Soduko_Solver(possible_solutions,board,Blocks_Solved=0,start_x=0,start_y=0):
    if(Blocks_Solved == 81):
        PrintBoard(board)
        return
    if(start_x == 9):
        start_y += 1
        start_x = 0
        

    if(board[start_x][start_y] != 0):
        Soduko_Solver(possible_solutions,board,Blocks_Solved+1,start_x+1,start_y)      
    else:
        for i in PossibleSolutions:
            if(isValid(board,start_x,start_y,i)):

                board[start_x][start_y] = i
                Soduko_Solver(possible_solutions,board,Blocks_Solved+1,start_x+1,start_y)
                board[start_x][start_y] = 0
            



def isValid(board,row_num,col_num,number):


    #check row
    for i in range(0,9):
        if (board[i][col_num] == number ):
            return False
    
    #check column
    for j in range(0,9):
        if (board[row_num][j] == number ):
            return False
    
    #check box
    x_range , y_range = determine_box(row_num,col_num)
    for i in x_range:
        for j in y_range:
            if(board[i][j] == number):
                return False
    
    return True



    

def PrintBoard(board):

    for i in range(0,9):
        print()
        if(i in [3,6]):
            print('_'*21)
            print()
        for j in range(0,9):
            print(board[i][j],end=" ")
            if(j in [2,5]):
                print('|',end='')
    print('\n\n')


def determine_box(row_num,col_num):
    x_range , y_range = [],[]
    if(row_num <= 2):
        x_range = [0,1,2]
    elif(row_num <= 5):
        x_range = [3,4,5]
    else:
        x_range = [6,7,8]
    if(col_num <= 2):
        y_range = [0,1,2]
    elif(col_num <= 5):
        y_range = [3,4,5]
    else:
        y_range = [6,7,8]

    return x_range,y_range    


if __name__ == "__main__":
    Soduko_Solver(PossibleSolutions,board2)