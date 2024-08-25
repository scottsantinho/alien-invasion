# Import the pygame module
import pygame
# Import the Sprite class from the pygame.sprite module
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Store the game's screen object
        self.screen = ai_game.screen
        # Get the rectangle of the game screen
        self.screen_rect = ai_game.screen.get_rect()
        # Store the game's settings object
        self.settings = ai_game.settings
        # Load the ship image from file
        self.image = pygame.image.load('images/ship.bmp')
        # Get the rectangle of the ship image
        self.rect = self.image.get_rect()
        # Position the ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # Store the ship's horizontal position as a float for precise movement
        self.x = float(self.rect.x)
        # Initialize movement flags for right and left directions
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Move the ship right if the flag is set and not at the right edge
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # Move the ship left if the flag is set and not at the left edge
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Update the ship's rectangle position based on the calculated x value
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        # Draw the ship image on the screen at its current position
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        # Set the ship's position to the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # Update the ship's x coordinate as a float for precise positioning
        self.x = float(self.rect.x)