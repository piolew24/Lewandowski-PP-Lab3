class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score()
        else:
            self.p2_score()

    def score(self):
        if self.p1_points == self.p2_points:
            return self._equal_score()

        if self.p1_points >= 4 or self.p2_points >= 4:
            return self._late_game_score()

        return self._normal_score()

    def _point_to_text(self, points):
        names = ("Love", "Fifteen", "Thirty", "Forty")
        return names[points]

    def _equal_score(self):
        if self.p1_points < 3:
            return self._point_to_text(self.p1_points) + "-All"
        return "Deuce"

    def _late_game_score(self):
        diff = self.p1_points - self.p2_points
        if abs(diff) == 1:
            return "Advantage player1" if diff > 0 else "Advantage player2"
        return "Win for player1" if diff > 0 else "Win for player2"

    def _normal_score(self):
        return (
            self._point_to_text(self.p1_points)
            + "-"
            + self._point_to_text(self.p2_points)
        )

    def set_p1_score(self, number):
        for _ in range(number):
            self.p1_score()

    def set_p2_score(self, number):
        for _ in range(number):
            self.p2_score()

    def p1_score(self):
        self.p1_points += 1

    def p2_score(self):
        self.p2_points += 1
