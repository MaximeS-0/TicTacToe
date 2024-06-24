
class player():
    def __init__(self, number_:int):
        self._number = number_

    @property
    def playerNumber(self):
        return self._number

    def makeMove(self) -> tuple or bool:

        row_str, col_str = input("Enter your move: ").split()
        
        try:
            row = int(row_str)
            col = int(col_str)
            
            if(row >= 0 and row <= 2 and col >=0 and col <= 2):

                print("Your move is: " + str(row) + " - " + str(col))
                return (True, row, col)
            else:
                print("Your move must be between 0 and 2")
                return (False, None, None)
        
        except ValueError:
            print("Your move must be a pair of positive integer")
            return (False, None, None)
    
