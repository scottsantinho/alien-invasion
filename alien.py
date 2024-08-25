# Import the pygame module
import pygame
# Import the Sprite class from the pygame.sprite module
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        # Store the game screen object for later use
        self.screen = ai_game.screen
        # Store the game settings object for later use
        self.settings = ai_game.settings
        # Load the alien image from a file and set it as the sprite's image
        self.image = pygame.image.load('images/alien.bmp')
        # Get the rectangular area of the image
        self.rect = self.image.get_rect()
        # Set the x-coordinate of the alien to be its width from the left edge
        self.rect.x = self.rect.width
        # Set the y-coordinate of the alien to be its height from the top edge
        self.rect.y = self.rect.height
        # Store the alien's exact horizontal position as a float for precise movement
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        # Get the rectangular area of the screen
        screen_rect = self.screen.get_rect()
        # Check if the alien is at the right edge or left edge of the screen
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien to the right or left."""
        # Update the alien's horizontal position based on speed and direction
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        # Update the rect object's x-coordinate to match the calculated position
        self.rect.x = self.x




