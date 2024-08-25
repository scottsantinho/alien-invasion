# Import the pygame.font module to render text
import pygame.font
# Import the Group class from pygame.sprite to manage groups of sprites
from pygame.sprite import Group
# Import the Ship class from the ship module
from ship import Ship

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        # Store a reference to the main game instance
        self.ai_game = ai_game
        # Get the screen surface from the game instance
        self.screen = ai_game.screen
        # Get the rectangle object that defines the screen's dimensions
        self.screen_rect = self.screen.get_rect()
        # Get the game settings
        self.settings = ai_game.settings
        # Get the game statistics
        self.stats = ai_game.stats
        # Define the color for the score text (dark grey)
        self.text_color = (30, 30, 30)
        # Create a font object for rendering the score
        self.font = pygame.font.SysFont(None, 30)
        # Prepare the initial score image
        self.prep_images()
    
    def prep_images(self):
        """Prepare all scoreboard images including score, high score, level, and ships."""
        # Prepare the score image
        self.prep_score()
        # Prepare the high score image
        self.prep_high_score()
        # Prepare the level image
        self.prep_level()
        # Prepare the ships images
        self.prep_ships()
    
    def prep_score(self):
        """Turn the score into a rendered image."""
        # Round the score to the nearest 10 using the round() function
        rounded_score = round(self.stats.score, -1)     
        # Format the score as a string with comma separators for thousands
        score_str = f"Current Score: {rounded_score:,}"   
        # Render the score string as an image using the font's render method
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)  
        # Create a rectangle object for the score image using get_rect() method
        self.score_rect = self.score_image.get_rect()   
        # Position the score rectangle 20 pixels from the right edge of the screen
        self.score_rect.right = self.screen_rect.right - 20  
        # Position the score rectangle 20 pixels from the top of the screen
        self.score_rect.top = 20
        
    def prep_level(self):
        """Turn the level into a rendered image."""
        # Convert the level number to a string
        level = str(self.stats.level)
        # Create a formatted string for the level display
        level_str = f"Current Level: {level}"
        # Render the level string as an image
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        # Create a rectangle for the level image
        self.level_rect = self.level_image.get_rect()
        # Position the level display below the score
        self.level_rect.right = self.score_rect.right
        # Set the top of the level rectangle 10 pixels below the bottom of the score rectangle
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        # Round the high score to the nearest 10
        high_score = round(self.stats.high_score, -1)
        # Format the high score with comma separators for thousands
        high_score_str = f"Highest Score: {high_score:,}"
        # Render the high score string as an image
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        # Create a rectangle for the high score image
        self.high_score_rect = self.high_score_image.get_rect()
        # Position the high score at the center of the screen horizontally
        self.high_score_rect.centerx = self.screen_rect.centerx
        # Align the top of the high score with the top of the score
        self.high_score_rect.top = self.score_rect.top

    def prep_ships(self):
        """Show how many ships are left."""
        # Create a Group to store the ship sprites
        self.ships = Group()
        # Iterate through the number of ships left
        for ship_number in range(self.stats.ships_left):
            # Create a new Ship instance
            ship = Ship(self.ai_game)
            # Set the x-coordinate of the ship based on its width and position
            ship.rect.x = 10 + ship_number * ship.rect.width
            # Set the y-coordinate of the ship
            ship.rect.y = 10
            # Add the ship to the Group
            self.ships.add(ship)
    
    def check_high_score(self):
        """Check to see if there's a new high score."""
        # Compare the current score with the high score
        if self.stats.score > self.stats.high_score:
            # Update the high score with the current score
            self.stats.high_score = self.stats.score
            # Prepare the new high score for display
            self.prep_high_score()
    
    def show_score(self):
        """Draw score to the screen."""
        # Blit (copy) the score image onto the screen at the position defined by score_rect
        self.screen.blit(self.score_image, self.score_rect)
        # Blit the high score image onto the screen
        self.screen.blit(self.high_score_image, self.high_score_rect)
        # Blit the level image onto the screen
        self.screen.blit(self.level_image, self.level_rect)
        # Blit the ships onto the screen
        self.ships.draw(self.screen)