
class player():
    def __init__(self, number_:int):
        self._number = number_

    @property
    def playerNumber(self):
        return self._number

    def makeMove(self) -> tuple:
        row, col = input("Enter your move: ").split()
        print("Your move is: " + row + " - " + col)

        return (row, col)
    
