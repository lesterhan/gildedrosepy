import unittest

from tennis_game import TennisGame

class TestTennisGame(unittest.TestCase):

    def test_initial_player_scores(self):
        player1Score = 0
        player2Score = 0

        tennis_game = TennisGame()
        self.assertEqual(player1Score, tennis_game.player1Score)
        self.assertEqual(player2Score, tennis_game.player2Score)