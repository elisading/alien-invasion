class Settings():

    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230,230,230)

        # ship settings
        self.ship_speed = 1
        self.shiplimit = 3

        # bullet settings (pew pew!)
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (19,0,166)
        self.bullets_allowed = 5

        # alien settings
        self.alien_speed = 1
        self.drop_speed = 10
        self.direction = 1 # R=1, L=-1