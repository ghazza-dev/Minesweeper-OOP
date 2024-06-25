class Cell:
    def __init__(self, row, col):
        self.row=row
        self.col=col
        self.clicked=False
        self.flagged=False
        self.neighbourBombs=0

class Bomb(Cell):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.flagged=False
        self.explode=False

class Board:
    def __init__(self, size=[]):
        self.size=size
        
        self.bombIndexes=[]   # array containing the coordinates of each bomb
        self.cellIndexes=[]   # array containing the coordinates of each cell

        self.cells=[]         # array containing each cell as an object of the 'Cell' class

        self.chooseMines()
        self.createMines()
        self.printBoard()
        self.assignCellHint()

    def chooseMines(self):  # choose random coordinates to be bombs
        num_of_mines=round((self.size[0]*self.size[1]) // 4)            # determine the number of mines in the board (amount of cells divided by 4)
        print(num_of_mines)
        import random
        
        for i in range(num_of_mines):       # choose a random row and col for each bomb to be placed, and add them to the array 'bombIndexes'
            randrow=random.randint(0,self.size[0]-1)
            randcol=random.randint(0,self.size[1]-1) 
            while [randrow,randcol] in self.bombIndexes:  # check if the randomly chosen coordinate has already been chosen                  
                randrow=random.randint(0,self.size[0]-1)       
                randcol=random.randint(0,self.size[1]-1) 
            self.bombIndexes.append([randrow,randcol])

        print(self.bombIndexes)
        print()

    def createMines(self):    # loop through every cell in the grid and determine whether it is a bomb or not 

        self.grid=[]

        for row in range(self.size[0]):
            rowArray=[]
            for col in range(self.size[1]):
                current=[row,col]
                if current in self.bombIndexes:
                    current=Bomb(row,col)              # if the current coordinate is seen to be a bomb, add it to the 'bomb' class 
                else:
                    self.cellIndexes.append([row,col])
                    current=Cell(row,col)              # if not, add it to the 'cell' class
                    self.cells.append(current)
                rowArray.append(col)
            self.grid.append(rowArray)

        print(self.cellIndexes)
        print()

    def printBoard(self):  # print the grid in the terminal

        for row in range(0, len(self.grid)):
            s=""
            for col in range(0, len(self.grid[1])):
                current=[row,col]
                if current in self.bombIndexes:
                    s=s+'bomb  '
                else:
                    s=s+f"({row},{col}) "
            print(s)
        print()

    def assignCellHint(self):   # loop through every cell and call 'determineNeighbours' function. Assign the returned value to cell.neighbourBombs
        for cell in self.cells:
            cell.neighbourBombs=self.determineNeighbours(cell.row,cell.col)
            print(f"({cell.row},{cell.col}) has {cell.neighbourBombs} neighbour bombs")
            
    def determineNeighbours(self, row, col):
        neighbours=0
        if (row-1 >= 0) and ([row-1,col] in self.bombIndexes):    # check above
            print(f'[{row},{col}] has a bomb above')
            neighbours+=1
        if (row+1 <= len(self.grid)) and ([row+1,col] in self.bombIndexes): # check below
            print(f'[{row},{col}] has a bomb below')
            neighbours+=1
        if (col-1 >= 0) and ([row,col-1] in self.bombIndexes):   # check left
            print(f'[{row},{col}] has a bomb to the left')
            neighbours+=1
        if (col+1 <= len(self.grid[0])) and ([row,col+1] in self.bombIndexes):   # check right
            print(f'[{row},{col}] has a bomb to the right')
            neighbours+=1
        if (row-1 >= 0) and (col-1 >= 0) and ([row-1,col-1] in self.bombIndexes):  # check top left
            print(f'[{row},{col}] has a bomb to the top left')
            neighbours+=1
        if (row-1 >= 0) and (col+1 <= len(self.grid[0])) and ([row-1,col+1] in self.bombIndexes):  # check top right
            print(f'[{row},{col}] has a bomb to the top right')
            neighbours+=1
        if (row+1 <= len(self.grid)) and (col-1 >= 0) and ([row+1,col-1] in self.bombIndexes):  # check bottom left
            print(f'[{row},{col}] has a bomb to the bottom left')
            neighbours+=1
        if (row+1 <= len(self.grid)) and (col+1 <= len(self.grid[0])) and ([row+1,col+1] in self.bombIndexes):  # check top right
            print(f'[{row},{col}] has a bomb to the bottom right')
            neighbours+=1
        return neighbours
