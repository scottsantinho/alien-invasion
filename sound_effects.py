import pygame

class SoundEffects:
    """A class to manage sound effects for the game."""

    def __init__(self):
        """Initialize sound effects."""
        # Initialize the pygame mixer
        pygame.mixer.init()

        # Load the bullet sound effect
        self.bullet_sound = pygame.mixer.Sound('sounds/bullet.wav')
        # Load the explosion sound effect
        self.explosion_sound = pygame.mixer.Sound('sounds/explosion.wav')

    def play_bullet_sound(self):
        """Play the bullet sound effect."""
        # Play the bullet sound
        self.bullet_sound.play()

    def play_explosion_sound(self):
        """Play the explosion sound effect."""
        # Play the explosion sound
        self.explosion_sound.play()