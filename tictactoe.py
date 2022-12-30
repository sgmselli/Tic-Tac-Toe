#Description
#Create a tictactoe game that has a self.grid and two players, X and 0 that place on the board in turns.
#First player to get three in a row wins

class Board:
    def __init__(self):
        self.grid = [[' ']*3 for x in range(3)]
        self.player = 0
        self.pos = {
            '1' : (0,0),
            '2' : (0,1),
            '3' : (0,2),
            '4' : (1,0),
            '5' : (1,1),
            '6' : (1,2),
            '7' : (2,0),
            '8' : (2,1),
            '9' : (2,2),
        }      

    def draw(self):
        print(
            ' -------------\n',
            '| '+self.grid[0][0]+' | '+self.grid[0][1]+' | '+self.grid[0][2]+' |\n',
            '-------------\n',
            '| '+self.grid[1][0]+' | '+self.grid[1][1]+' | '+self.grid[1][2]+' |\n',
            '-------------\n',
            '| '+self.grid[2][0]+' | '+self.grid[2][1]+' | '+self.grid[2][2]+' |\n',
            '-------------\n',
        )

    def turn(self):
        move = (input('Select pos, 1-9: '))
        while move not in ['1','2','3','4','5','6','7','8','9']:
            print("Enter a position between 1 and 9")
            move = (input('Select pos, 1-9: '))

        if self.grid[self.pos[move][0]][self.pos[move][1]] != 'X' and self.grid[self.pos[move][0]][self.pos[move][1]] != 'O':
            if self.player == 0:
                self.grid[self.pos[move][0]][self.pos[move][1]] = 'X'
                self.player = 1
            else:
                self.grid[self.pos[move][0]][self.pos[move][1]] = 'O'
                self.player = 0
        else:
            print('This position is already placed')

        if self.player == 0:
            print("Player X's turn")
        else:
            print("Player O's turn")

    def win(self):

        for row in self.grid:
            if set(row) == {'X'}:
                return 'A'
            elif set(row) == {'O'}:
                return 'B'
        
        for col in zip(*self.grid):
            if set(col) == {'X'}:
                return 'A'
            elif set(col) == {'O'}:
                return 'B'
        
        if self.grid[0][0] == 'X' and self.grid[1][1] == 'X' and self.grid[2][2] == 'X':
            return 'A'
        elif self.grid[0][0] == 'O' and self.grid[1][1] == 'O' and self.grid[2][2] == 'O':
            return 'A'
        elif self.grid[0][2] == 'X' and self.grid[1][1] == 'X' and self.grid[2][0] == 'X':
            return 'A'    
        elif self.grid[0][2] == 'O' and self.grid[1][1] == 'O' and self.grid[2][0] == 'O':
            return 'B'  
        
        return None
        

board = Board()
board.draw()

while 1:
    board.turn()
    board.draw()

    if board.win() == 'A':
        print('Player X wins')
        break
    elif board.win() == 'B':
        print('Player O wins')
        break
