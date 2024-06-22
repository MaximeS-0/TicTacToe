
class player():
    def __init__(self, number_:int):
        self._number = number_

    @property
    def playerNumber(self):
        return self._number

    def makeMove(self) -> tuple:
        row_str, col_str = input("Enter your move: ").split()
        row = int(row_str)
        col = int(col_str)
        print("Your move is: " + str(row) + " - " + str(col))

        return (row, col)
    
