class GameStats():

    def __init__(self, gs):
        self.gs = gs
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.gs.shiplimit
        