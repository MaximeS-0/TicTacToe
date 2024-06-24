from Game.board import board
from Game.Player.humanPlayer import player

class game():
    def __init__(self):
        self.boardGame = board()
        self.player1 = player(1)
        self.player2 = player(2)

        self.playerList = [self.player1, self.player2]

    def playGame(self):
        nbTurn = 0
        while (not self._isGameCompleted()):
            self._playTurn(self.playerList[nbTurn % len(self.playerList)])
            nbTurn += 1
        
        if (self.boardGame.gameState() == board.GAMESTATE_TIE):
            print("The game is a tie")
        else:
            print("The winner is : Player " + str(self.playerList[(nbTurn - 1) % 2].playerNumber))

    def _playTurn(self, activePlayer: player):
        print("Player " + str(activePlayer.playerNumber) + " , your turn to play.")
        print(self.boardGame)
        self._playMove(activePlayer)



    def _playMove(self, activePlayer: player):
        moveInvalid = True
        while(moveInvalid):

            (isInputValid, row, col) = activePlayer.makeMove()

            if(isInputValid):
                moveInvalid = not self.boardGame.addValue(row, col, activePlayer.playerNumber)

            if (moveInvalid):
                print("Your move is invalid, play something else.")

        
    def _isGameCompleted(self):
        return self.boardGame.gameState() != board.GAMESTATE_IN_PROGRESS

