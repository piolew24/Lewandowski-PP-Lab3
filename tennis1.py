class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_points += 1
        else:
            self.p2_points += 1

    def score(self):
        point_names = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }
        if self.p1_points == self.p2_points:
            if self.p1_points < 3:
                result = point_names[self.p1_points] + "-All"
                return result
            result = "Deuce"
            return result
        elif self.p1_points >= 4 or self.p2_points >= 4:
            minus_result = self.p1_points - self.p2_points
            if abs(minus_result) == 1:
                result = "Advantage player1" if minus_result > 0 else "Advantage player2"
                return result
            result = "Win for player1" if minus_result > 0 else "Win for player2"
            return result
        result = point_names[self.p1_points] + "-" + point_names[self.p2_points]
        return result