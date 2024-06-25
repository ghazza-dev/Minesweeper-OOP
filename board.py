class Cell:
    def __init__(self, row, col):
        self.row=row
        self.col=col
        self.clicked=False
        self.flagged=False
        self.neighbourBombs=0

    def determineNeighbours(self):
        pass

class Bomb(Cell):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.flagged=False
        self.explode=False

class Board:
    def __init__(self, size=[]):
        self.size=size
        self.createMines()
        self.printBoard()

    def createMines(self):
        num_of_mines=round((self.size[0]*self.size[1]) // 4)            # determine the number of mines in the board (amount of cells divided by x)
        print(num_of_mines)
        import random
        self.bombIndexes=[]                                     # list containing the coordinates of each bomb 
        
        for i in range(num_of_mines):
            randrow=random.randint(0,self.size[0]-1)        
            randcol=random.randint(0,self.size[1]-1)                # choose a random row and col for each bomb to be placed
            while [randrow,randcol] in self.bombIndexes:                 # and add them to an array 'bombIndexes'
                randrow=random.randint(0,self.size[0]-1)       
                randcol=random.randint(0,self.size[1]-1) 
            self.bombIndexes.append([randrow,randcol])

        print(self.bombIndexes)
        print()

        # loop through every cell in the grid and determine whether it is a bomb or not 
        
        self.grid=[]

        for row in range(self.size[0]):
            rowArray=[]
            for col in range(self.size[1]):
                current=[row,col]
                if current in self.bombIndexes:
                    current=Bomb(row,col)
                else:
                    current=Cell(row,col)
                rowArray.append(col)
            self.grid.append(rowArray)

    def printBoard(self):

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
        
                 
board=Board([5,10]) 
