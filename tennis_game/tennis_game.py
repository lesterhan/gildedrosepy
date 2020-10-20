class TennisGame(object):

    def __init__(self):
        """
        docstring
        """
        self.playerScores = {
            'player1': ZeroPoint(),
            'player2': ZeroPoint(),
        }

    def getScore(self):
        """
        docstring
        """
        return "Love-All"

    def wonPoint(self, player):
        self.playerScores[player] = self.playerScores[player].nextPoint()
        return self.playerScores[player]


class Point(object):

    def nextPoint(self):
        pass


class ZeroPoint(Point):

    def nextPoint(self):
        return OnePoint()


class OnePoint(Point):

    def nextPoint(self):
        return TwoPoint()


class TwoPoint(Point):

    def nextPoint(self):
        pass