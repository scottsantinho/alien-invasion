# Import necessary modules
import sys
import pygame
from time import sleep

# Import custom game components
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from sound_effects import SoundEffects  # Add this import

# Define the main game class
class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        # Initialize Pygame modules
        pygame.init()
        # Create a clock object to control the game's frame rate
        self.clock = pygame.time.Clock()
        # Create a settings object based on the Settings class
        self.settings = Settings()
        # Create a screen object based on the screen size settings
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # Set the caption of the game window
        pygame.display.set_caption("Alien Invasion")
        # Create an instance to store game statistics
        self.stats = GameStats(self)
        # Create a scoreboard
        self.scoreboard = Scoreboard(self)
        # Create a ship object and pass the current game instance to it
        self.ship = Ship(self)
        # Create a group to store all the bullets
        self.bullets = pygame.sprite.Group()
        # Create a group of aliens
        self.aliens = pygame.sprite.Group()
        # Create a fleet of aliens
        self._create_fleet()
        # Start Alien Invasion in an inactive state
        self.game_active = False
        # Create a play button
        self.play_button = Button(self, "Play")
        # Create difficulty buttons
        self.play_button.create_difficulty_buttons()
        # Create a SoundEffects instance
        self.sound_effects = SoundEffects()

    def run_game(self):
        """Start the main loop for the game."""
        # Start the main game loop
        while True:
            # Check for events
            self._check_events()
            # If game is active, update game elements
            if self.game_active:
                # Update the ship's position
                self.ship.update()
                # Update the bullets
                self._update_bullets()
                # Update the aliens
                self._update_aliens()
            # Update the screen
            self._update_screen()
            # Adjust the frame rate to 60 frames per second
            self.clock.tick(60)
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Iterate through all events in the Pygame event queue
        for event in pygame.event.get():
            # Check if the user has clicked the close button
            if event.type == pygame.QUIT:
                # Quit the game by exiting the program
                sys.exit()
            # Check if a key has been pressed down
            elif event.type == pygame.KEYDOWN:
                # Handle key press events using a separate method
                self._check_keydown_events(event)
            # Check if a key has been released
            elif event.type == pygame.KEYUP:
                # Handle key release events using a separate method
                self._check_keyup_events(event)
            # Check if a mouse button has been pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the current position of the mouse cursor
                mouse_pos = pygame.mouse.get_pos()
                # Check if the play button has been clicked
                self._check_play_button(mouse_pos)
                # Check if a difficulty button has been clicked
                self._check_difficulty_buttons(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        # Check if the Play button was clicked by comparing mouse position with button rectangle
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # If the button was clicked and the game is not active, initialize a new game
        if button_clicked and not self.game_active:
            # Reset the game settings to their initial values
            self.settings.initialize_dynamic_settings()
            # Reset the game statistics (score, ships left, etc.)
            self.stats.reset_stats()
            # Prepare all scoreboard images
            self.scoreboard.prep_images()
            # Set the game to active state to start gameplay
            self.game_active = True
            # Remove any remaining aliens from the previous game
            self.aliens.empty()
            # Remove any remaining bullets from the previous game
            self.bullets.empty()
            # Create a new fleet of aliens for the new game
            self._create_fleet()
            # Center the player's ship on the screen
            self.ship.center_ship()
            # Hide the mouse cursor during gameplay
            pygame.mouse.set_visible(False)

    def _check_difficulty_buttons(self, mouse_pos):
        """Set the game difficulty when a difficulty button is clicked."""
        # Iterate through all difficulty buttons
        for button, difficulty in self.play_button.difficulty_buttons:
            # Check if the button was clicked and the game is not active
            if button.collidepoint(mouse_pos) and not self.game_active:
                # Set the game difficulty
                self.settings.difficulty = difficulty.lower()
                # Initialize dynamic settings based on the new difficulty
                self.settings.initialize_dynamic_settings()

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        # Move ship right if right arrow key is pressed
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        # Move ship left if left arrow key is pressed
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Quit game if 'Q' key is pressed
        elif event.key == pygame.K_q:
            sys.exit()
        # Fire bullet if spacebar is pressed
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""  
        # Stop moving ship right when right arrow key is released
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        # Stop moving ship left when left arrow key is released
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an instance of the Alien class
        alien = Alien(self)
        # Get the width and height of the alien image
        alien_width, alien_height = alien.rect.size
        # Set the initial x-coordinate and y-coordinate for alien placement
        current_x, current_y = alien_width, alien_height
        # Create rows of aliens until 3 alien heights from screen bottom
        while current_y < (self.settings.screen_height - 5 * alien_height):
            # Create aliens in a row, placing them 2 widths apart horizontally
            while current_x < (self.settings.screen_width - 2 * alien_width):
                # Create an alien at the current position
                self._create_alien(current_x, current_y)
                # Move to the next horizontal position
                current_x += 2 * alien_width
            
            # Reset the x-coordinate for the next row
            current_x = alien_width
            # Move the y-coordinate down by two alien heights
            current_y += 2 * alien_height
            
    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        # Create a new alien instance
        new_alien = Alien(self)
        # Set the x-coordinate of the new alien
        new_alien.x = x_position
        # Update the rect attribute to match the new x-coordinate
        new_alien.rect.x = x_position
        # Set the y-coordinate of the new alien
        new_alien.rect.y = y_position
        # Add the new alien to the aliens group
        self.aliens.add(new_alien)
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        # Check each alien in the fleet
        for alien in self.aliens.sprites():
            # If an alien has reached an edge, change fleet direction and break
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        # Move each alien down by the fleet drop speed
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        # Reverse the fleet direction
        self.settings.fleet_direction *= -1

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        # Check if the number of bullets is less than the allowed limit
        if len(self.bullets) < self.settings.bullets_allowed:
            # Create a new bullet
            new_bullet = Bullet(self)
            # Add the new bullet to the bullets group
            self.bullets.add(new_bullet)
            # Play the bullet sound effect
            self.sound_effects.play_bullet_sound()

    def _update_bullets(self):
        """Update the position of the bullets and get rid of old bullets."""
        # Update the position of all bullets
        self.bullets.update()
        # Remove bullets that have gone off the screen
        for bullet in self.bullets.copy():
            # Check if the bullet has gone off the top of the screen
            if bullet.rect.bottom <= 0:
                # Remove the bullet from the group
                self.bullets.remove(bullet)
        # Check for any bullets that have hit aliens
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Check for collisions between bullets and aliens
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True) 
        # If there are collisions, update the score and play explosion sound
        if collisions:
            # Play the explosion sound effect
            self.sound_effects.play_explosion_sound()
            # For each alien in the collisions, update the score
            for aliens in collisions.values():  
                # The score is increased by the number of aliens times the points per alien
                self.stats.score += self.settings.alien_points * len(aliens)
            # Update the scoreboard
            self.scoreboard.prep_score()
            # Check for a new high score
            self.scoreboard.check_high_score()
        # If all aliens are destroyed, create a new fleet
        if not self.aliens:
            # Start a new level
            self._start_new_level()
    
    def _start_new_level(self):
        """Start a new level."""
        # Destroy existing bullets
        self.bullets.empty()
        # Create a new fleet
        self._create_fleet()
        # Increase game speed
        self.settings.increase_speed()
        # Increase the game level
        self.stats.level += 1
        # Update the level display
        self.scoreboard.prep_level()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        # Check if there are ships left
        if self.stats.ships_left > 0:
            # Decrement ships_left
            self.stats.ships_left -= 1
            # Update the ship display
            self.scoreboard.prep_ships()
            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            # Empty the bullets group
            self.bullets.empty()
            # Create a new fleet
            self._create_fleet()
            # Center the ship
            self.ship.center_ship()
            # Pause for a moment
            sleep(0.5)
        else:
            # Set game to inactive state if no ships left
            self.game_active = False
            # Show the mouse cursor
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        # Get the rectangle of the screen
        screen_rect = self.screen.get_rect()
        # Check each alien in the fleet
        for alien in self.aliens.sprites():
            # If an alien has reached the bottom, treat it as a ship hit
            if alien.rect.bottom >= screen_rect.bottom:
                # Call the ship_hit method
                self._ship_hit()
                # Exit the loop after the first alien reaches the bottom
                break
    
    def _update_aliens(self):
        """Update the position of the aliens."""
        # Check if the fleet is at an edge
        self._check_fleet_edges()
        # Update the positions of all aliens in the fleet
        self.aliens.update()
        # Check if any aliens have reached the bottom of the screen
        self._check_aliens_bottom()
        # Check for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            # Call the ship_hit method if there's a collision
            self._ship_hit()
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Fill the screen with the background color
        self.screen.fill(self.settings.bg_color)
        # Draw all bullets on the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()    
        # Draw the ship on the screen
        self.ship.blitme() 
        # Draw all aliens on the screen
        self.aliens.draw(self.screen)
        # Draw the scoreboard
        self.scoreboard.show_score()
        # Draw the play button if the game is not active
        if not self.game_active:
            # Draw the main play button
            self.play_button.draw_button()
            # Draw the difficulty buttons
            self.play_button.draw_difficulty_buttons(self)
        # Update the display
        pygame.display.flip() 

# Check if this script is being run as the main program
if __name__ == '__main__':
    # Create a game instance
    ai = AlienInvasion()
    # Run the game
    ai.run_game()