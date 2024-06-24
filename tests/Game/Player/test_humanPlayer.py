from unittest import TestCase
from unittest import mock

from src.Game.Player.humanPlayer import player

class Test_Player(TestCase):

    def setUp(self) -> None:
        self.testPlayer = player(1)

    def tearDown(self) -> None:
        self.testPlayer = None


    def test_playerSymbol(self):
        self.assertEqual(1, self.testPlayer.playerNumber)

    @mock.patch('src.Game.Player.humanPlayer.input', create=True)
    def test_userInput(self, mocked_input):
        mocked_input.side_effect = ['0 0']
        self.assertEqual((True, 0, 0), self.testPlayer.makeMove())

    @mock.patch('src.Game.Player.humanPlayer.input', create=True)
    def test_userInput_OverLimit(self, mocked_input):
        mocked_input.side_effect = ['3 5']
        self.assertEqual((False, None, None), self.testPlayer.makeMove())

    @mock.patch('src.Game.Player.humanPlayer.input', create=True)
    def test_userInput_Negative(self, mocked_input):
        mocked_input.side_effect = ['-1 -2']
        self.assertEqual((False, None, None), self.testPlayer.makeMove())

    @mock.patch('src.Game.Player.humanPlayer.input', create=True)
    def test_userInput_wrongInput(self, mocked_input):
        mocked_input.side_effect = ['a b']
        self.assertEqual((False, None, None), self.testPlayer.makeMove())