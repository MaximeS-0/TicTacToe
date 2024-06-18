class board():

    GAMESTATE_IN_PROGRESS = 0
    GAMESTATE_PLAYER1_WIN = 1
    GAMESTATE_PLAYER2_WIN = 2
    GAMESTATE_TIE = 3

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

    def gameState(self) -> int:
        #Check row
        for row in range(len(self._board)):
            value = self._board[row][0]

            for column in range(len(self._board[0])):
                if (self._board[row][column] != value): #If there is a different value, there can't be a winner
                    break
                else:  #If it is always the same value, it could be all None, or 1 player has win the game
                    if value == 1:
                        return board.GAMESTATE_PLAYER1_WIN
                    elif value == 2:
                        return board.GAMESTATE_PLAYER2_WIN
                    
                    #If all None, we continue
    
        #Check column
        for column in range(len(self._board[0])):
            value = self._board[0][column]

            for row in range(len(self._board)):
                if (self._board[row][column] != value): #If there is a different value, there can't be a winner
                    break
                else:  #If it is always the same value, it could be all None, or 1 player has win the game
                    if value == 1:
                        return board.GAMESTATE_PLAYER1_WIN
                    elif value == 2:
                        return board.GAMESTATE_PLAYER2_WIN
                    
                    #If all None, we continue

        #Chek diagonal
        #First diagonal [(0,0) (1,1) (2,2)]
        value = self._board[0][0]
        for i in range(len(self._board)):
            if (self._board[i][i] != value): #If there is a different value, there can't be a winner
                    break
            else:  #If it is always the same value, it could be all None, or 1 player has win the game
                if value == 1:
                    return board.GAMESTATE_PLAYER1_WIN
                elif value == 2:
                    return board.GAMESTATE_PLAYER2_WIN
                    
                    #If all None, we continue

        #Second diagonal [(2,0) (1,1) (0,2)]
        value = self._board[2][0]
        for i in range(len(self._board)):
            if (self._board[i][len(self._board[0])-1 - i] != value): #If there is a different value, there can't be a winner
                    break
            else:  #If it is always the same value, it could be all None, or 1 player has win the game
                if value == 1:
                    return board.GAMESTATE_PLAYER1_WIN
                elif value == 2:
                    return board.GAMESTATE_PLAYER2_WIN
                    
                    #If all None, we continue

        #Check tie
        for row in range(len(self._board)):
            for column in range(len(self._board[0])):
                if self._board[row][column] == None:
                    return board.GAMESTATE_IN_PROGRESS
        
        return board.GAMESTATE_TIE