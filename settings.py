class Settings:
    "A class to store all settings for Alien Invasion."

    def __init__(self):
        "Initialize the game's settings."
        # Define the width of the game screen
        self.screen_width = 1200
        # Define the height of the game screen
        self.screen_height = 800
        # Set the background color of the game screen (light gray)
        self.bg_color = (230, 230, 230)
        # Set the width of the bullet
        self.bullet_width = 3
        # Set the height of the bullet
        self.bullet_height = 15
        # Set the color of the bullet (dark gray)
        self.bullet_color = (60, 60, 60)
        # Set the maximum number of bullets allowed on screen at once
        self.bullets_allowed = 5
        # Set the speed at which the alien fleet drops down the screen
        self.fleet_drop_speed = 10
        # Set the number of ships (lives) the player has
        self.ship_limit = 3
        # Set the scale factor for increasing game speed
        self.speedup_scale = 1.1
        # Set the scale factor for increasing score
        self.score_scale = 1.5
        # Set the default difficulty level
        self.difficulty = 'normal'
        # Define difficulty scaling factors for different levels
        self.difficulty_scale = {
            'beginner': 0.8,
            'normal': 1.0,
            'intermediate': 1.2,
            'difficult': 1.5
        }
        # Set the speed for beginner difficulty
        self.beginner_speed = 1.0
        # Set the speed for intermediate difficulty
        self.intermediate_speed = 1.5
        # Set the speed for difficult difficulty
        self.difficult_speed = 2.0
        # Initialize the dynamic settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        # Set the base speed for the ship
        base_ship_speed = 5
        # Set the base speed for the bullet
        base_bullet_speed = 2.5
        # Set the base speed for the alien
        base_alien_speed = 1.0
        # Apply difficulty scaling to the speeds
        scale = self.difficulty_scale[self.difficulty]
        # Set the ship speed based on difficulty
        self.ship_speed = base_ship_speed * scale
        # Set the bullet speed based on difficulty
        self.bullet_speed = base_bullet_speed * scale
        # Set the alien speed based on difficulty
        self.alien_speed = base_alien_speed * scale
        # Set the initial direction of the alien fleet (1 for right, -1 for left)
        self.fleet_direction = 1
        # Set the initial point value for hitting an alien
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        # Get the difficulty scaling factor
        scale = self.difficulty_scale[self.difficulty]
        # Increase the ship speed
        self.ship_speed *= self.speedup_scale * scale
        # Increase the bullet speed
        self.bullet_speed *= self.speedup_scale * scale
        # Increase the alien speed
        self.alien_speed *= self.speedup_scale * scale
        # Increase the points awarded for hitting an alien
        self.alien_points = int(self.alien_points * self.score_scale)