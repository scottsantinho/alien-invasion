class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        # Store the game settings for easy access
        self.settings = ai_game.settings
        # Reset all statistics to their initial values
        self.reset_stats()
        # Set the game to an inactive state initially
        self.game_active = False
        # Initialize the high score to 0
        self.high_score = 0


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        # Set the number of ships left to the initial ship limit
        self.ships_left = self.settings.ship_limit
        # Initialize the player's score to 0
        self.score = 0
        # Set the initial game level to 1
        self.level = 1