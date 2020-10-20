class TennisGame(object):

    def __init__(self):
        """
        docstring
        """
        self.player1Score = 0
        self.player2Score = 0

    def getScore(self):
        """
        docstring
        """
        return "Love-All"

    def wonPoint(self, player):
      pass


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