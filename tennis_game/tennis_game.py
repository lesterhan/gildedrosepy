class TennisGame(object):

    def __init__(self):
        self.playerScores = {
            'player1': ZeroPoint(),
            'player2': ZeroPoint(),
        }

    def getScore(self):
        return "Player 1 {}, Player 2 {}".format(
            self.playerScores['player1'].toString(),
            self.playerScores['player2'].toString(),
        )

    def wonPoint(self, player):
        self.playerScores[player] = self.playerScores[player].nextPoint()
        return self.playerScores[player]


class Point(object):

    def nextPoint(self):
        pass


class ZeroPoint(Point):

    def nextPoint(self):
        return OnePoint()

    def toString(self):
        return "Love"


class OnePoint(Point):

    def nextPoint(self):
        return TwoPoint()

    def toString(self):
        return "15"


class TwoPoint(Point):

    def nextPoint(self):
        pass