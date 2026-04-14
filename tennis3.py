class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, name):
        if name == "player1":
            self.p1_points += 1
        else:
            self.p2_points += 1

    def score(self):
        point_names = ["Love", "Fifteen", "Thirty", "Forty"]
        p1, p2 = self.p1_points, self.p2_points

        if p1 == p2:
            return f"{point_names[p1]}-All" if p1 < 3 else "Deuce"

        if p1 >= 4 or p2 >= 4:
            leader = self.player1_name if p1 > p2 else self.player2_name
            return f"Advantage {leader}" if abs(p1 - p2) == 1 else f"Win for {leader}"

        return f"{point_names[p1]}-{point_names[p2]}"

