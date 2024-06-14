class board():

    def __init__(self):
        self._board = [[None]*3 for i in range(3)] 

    def __str__(self):
        textToShow = ""

        for row in self._board:
            textToShow += str(row) + "\n"
        
        return textToShow
    
    @property
    def boardState(self):
        return self._board
    
    def addValue(self, row:int, column:int, value:str) -> bool:
        if row > len(self._board) or column > len(self._board[0]):
            return False

        if self._board[row][column] == None:
            self._board[row][column] = value
            return True
        return False

