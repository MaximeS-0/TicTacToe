import board
import player

class game():
    def __init__(self):
        self.boardGame = board()
        self.player1 = player(1)
        self.player2 = player(2)

        self.playerList = [self.player1, self.player2]

    def playTurn(self):
        self._playMove()
        self._isGameCompleted()

    def _playMove(self):
        pass

    def _isGameCompleted(self):
        pass