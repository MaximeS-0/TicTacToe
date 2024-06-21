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

        if (
            self._checkingRows() == board.GAMESTATE_PLAYER1_WIN or
            self._checkingColumns() == board.GAMESTATE_PLAYER1_WIN or
            self._checkingDiagonals() == board.GAMESTATE_PLAYER1_WIN
        ):
            print("Player 1 win!")
            return board.GAMESTATE_PLAYER1_WIN
        
        elif(
            self._checkingRows() == board.GAMESTATE_PLAYER2_WIN or
            self._checkingColumns() == board.GAMESTATE_PLAYER2_WIN or
            self._checkingDiagonals() == board.GAMESTATE_PLAYER2_WIN
        ):
            print("Player 2 win!")
            return board.GAMESTATE_PLAYER2_WIN

        elif(self._isTie()):
            print("It is a tie!")
            return board.GAMESTATE_TIE

        else:
            return board.GAMESTATE_IN_PROGRESS



    def _checkingRows(self) -> int:

        for row in range(len(self._board)):
            winner = self._board[row][0]

            for column in range(len(self._board[0])):
                if (self._board[row][column] != winner): #If there is a different value, the row doesn't have a winner
                    winner = None
                    break
            
            #If winner is not None, there is winner
            if winner == 1:
                return board.GAMESTATE_PLAYER1_WIN
            elif winner == 2:
                return board.GAMESTATE_PLAYER2_WIN
        
        return None

    def _checkingColumns(self) -> int:
            
        for column in range(len(self._board[0])):
            winner = self._board[0][column]

            for row in range(len(self._board)):
                if (self._board[row][column] != winner): #If there is a different value, there can't be a winner
                    winner = None
                    break
            
            #If it is always the same value, it could be all None, or 1 player has win the game
            if winner == 1:
                return board.GAMESTATE_PLAYER1_WIN
            elif winner == 2:
                return board.GAMESTATE_PLAYER2_WIN
            
        return None

    def _checkingDiagonals(self) -> int:

        #First diagonal [(0,0) (1,1) (2,2)]
        winner = self._board[0][0]
        for i in range(len(self._board)):
            if (self._board[i][i] != winner): #If there is a different value, there can't be a winner
                    winner = None
            
        #If it is always the same value, it could be all None, or 1 player has win the game
        if winner == 1:
            return board.GAMESTATE_PLAYER1_WIN
        elif winner == 2:
            return board.GAMESTATE_PLAYER2_WIN
                

        #Second diagonal [(2,0) (1,1) (0,2)]
        winner = self._board[2][0]
        for i in range(len(self._board)):
            if (self._board[i][len(self._board[0])-1 - i] != winner): #If there is a different value, there can't be a winner
                    winner = None

        #If it is always the same value, it could be all None, or 1 player has win the game
        if winner == 1:
            return board.GAMESTATE_PLAYER1_WIN
        elif winner == 2:
            return board.GAMESTATE_PLAYER2_WIN
                    
        return None
    
    def _isTie(self) -> int:
        #Check tie
        for row in range(len(self._board)):
            for column in range(len(self._board[0])):
                if self._board[row][column] is None:
                    return False
                
        return True