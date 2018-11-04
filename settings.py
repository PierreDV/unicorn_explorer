class Settings():
    """A class to store all settings for Unicorn Explorer."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (76, 209, 55)

        # Unicorn dude settings
        self.unicorn_dude_speed_factor = 0.5