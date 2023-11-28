class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.even_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.advantage_or_win()
        else:
            return self.score()
    
    def even_score(self):
        score_names = ["Love-All", "Fifteen-All", "Thirty-All", "Deuce"]
        if self.player1_score < 3:
            return score_names[self.player1_score]
        return score_names[3]
    
    def advantage_or_win(self):
        minus_result = self.player1_score - self.player2_score
        if abs(minus_result) == 1:
            leader = self.player1_name if minus_result == 1 else self.player2_name
            return f"Advantage {leader}"
        winner = self.player1_name if minus_result >= 2 else self.player2_name
        return f"Win for {winner}"
    
    def score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        return f"{score_names[self.player1_score]}-{score_names[self.player2_score]}"



