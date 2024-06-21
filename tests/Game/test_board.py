import unittest

from src.Game.board import board

class Test_Board(unittest.TestCase):

    def setUp(self) -> None:
        self.testBoard = board()

    def tearDown(self) -> None:
        self.testBoard = None


    def test_emptyBoard(self):
        solution = [[None, None, None], [None, None, None], [None, None, None]]
        self.assertEqual(solution, self.testBoard.boardState)

    def test_addValue(self):
        solution = [[1, None, None], [None, None, None], [None, None, None]]
        self.testBoard.addValue(0,0,1)
        self.assertEqual(solution, self.testBoard.boardState)

        solution = [[1, None, None], [None, None, None], [None, 2, None]]
        self.testBoard.addValue(2,1,2)

        solution = [[1, None, None], ['x', None, None], [None, 2, None]]
        self.testBoard.addValue(1,0,'x')


class Test_BoardState(unittest.TestCase):
    def setUp(self) -> None:
        self.testBoard = board()

    def tearDown(self) -> None:
        self.testBoard = None

    def test_gameState_newGame(self):
        self.assertNotEqual(board.GAMESTATE_PLAYER1_WIN, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_PLAYER2_WIN, self.testBoard.gameState())
        self.assertEqual(board.GAMESTATE_IN_PROGRESS, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_TIE, self.testBoard.gameState())


    def test_gameState_player1_Row1(self):
        self.testBoard.addValue(1,0,1)
        self.testBoard.addValue(1,1,1)
        self.testBoard.addValue(1,2,1)

        self.assertEqual(board.GAMESTATE_PLAYER1_WIN, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_PLAYER2_WIN, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_IN_PROGRESS, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_TIE, self.testBoard.gameState())


    def test_gameState_player2_Row2(self):
        self.testBoard.addValue(1,0,2)
        self.testBoard.addValue(1,1,2)
        self.testBoard.addValue(1,2,2)

        self.assertNotEqual(board.GAMESTATE_PLAYER1_WIN, self.testBoard.gameState())
        self.assertEqual(board.GAMESTATE_PLAYER2_WIN, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_IN_PROGRESS, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_TIE, self.testBoard.gameState())


    def test_gameState_player1_Column3(self):
        self.testBoard.addValue(0,2,1)
        self.testBoard.addValue(1,2,1)
        self.testBoard.addValue(2,2,1)

        self.assertEqual(board.GAMESTATE_PLAYER1_WIN, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_PLAYER2_WIN, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_IN_PROGRESS, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_TIE, self.testBoard.gameState())


    def test_gameState_player2_Column1(self):
        self.testBoard.addValue(0,0,2)
        self.testBoard.addValue(1,0,2)
        self.testBoard.addValue(2,0,2)

        self.assertNotEqual(board.GAMESTATE_PLAYER1_WIN, self.testBoard.gameState())
        self.assertEqual(board.GAMESTATE_PLAYER2_WIN, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_IN_PROGRESS, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_TIE, self.testBoard.gameState())


    def test_gameState_player1_Diagonal1(self):
        self.testBoard.addValue(0,0,1)
        self.testBoard.addValue(1,1,1)
        self.testBoard.addValue(2,2,1)

        self.assertEqual(board.GAMESTATE_PLAYER1_WIN, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_PLAYER2_WIN, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_IN_PROGRESS, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_TIE, self.testBoard.gameState())


    def test_gameState_player2_OtherDiagonal2(self):
        self.testBoard.addValue(2,0,2)
        self.testBoard.addValue(1,1,2)
        self.testBoard.addValue(0,2,2)

        self.assertNotEqual(board.GAMESTATE_PLAYER1_WIN, self.testBoard.gameState())
        self.assertEqual(board.GAMESTATE_PLAYER2_WIN, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_IN_PROGRESS, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_TIE, self.testBoard.gameState())


    def test_gameState_inProgress(self):
        self.testBoard.addValue(2,0,2)
        self.testBoard.addValue(1,1,2)

        self.assertNotEqual(board.GAMESTATE_PLAYER1_WIN, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_PLAYER2_WIN, self.testBoard.gameState())
        self.assertEqual(board.GAMESTATE_IN_PROGRESS, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_TIE, self.testBoard.gameState())

    def test_gameState_Tie(self):
        self.testBoard.addValue(0,0,1)
        self.testBoard.addValue(0,1,2)
        self.testBoard.addValue(0,2,1)
        self.testBoard.addValue(1,0,2)
        self.testBoard.addValue(1,1,2)
        self.testBoard.addValue(1,2,1)
        self.testBoard.addValue(2,0,1)
        self.testBoard.addValue(2,1,1)
        self.testBoard.addValue(2,2,2)

        self.assertNotEqual(board.GAMESTATE_PLAYER1_WIN, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_PLAYER2_WIN, self.testBoard.gameState())
        self.assertNotEqual(board.GAMESTATE_IN_PROGRESS, self.testBoard.gameState())
        self.assertEqual(board.GAMESTATE_TIE, self.testBoard.gameState())