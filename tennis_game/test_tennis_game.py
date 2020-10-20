import unittest

from tennis_game import TennisGame, ZeroPoint, OnePoint

class TestTennisGame(unittest.TestCase):

    # def test_initial_player_scores(self):
    #     player1Score = 0
    #     player2Score = 0
    #     tennis_game = TennisGame()

    #     self.assertEqual(player1Score, tennis_game.player1Score)
    #     self.assertEqual(player2Score, tennis_game.player2Score)

    def test_get_score(self):
        score = "Love-All"
        tennis_game = TennisGame()

        self.assertEqual(score, tennis_game.getScore())

    def test_won_point(self):
        player1Score = 1
        player2Score = 0
        tennis_game = TennisGame()

    def test_won_point_returns_next_point_for_zero_points(self):
        tennis_game = TennisGame()
        next_point = tennis_game.wonPoint('player1')

        self.assertTrue(isinstance(next_point, OnePoint))







if __name__ == '__main__':
    unittest.main()