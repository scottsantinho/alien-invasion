# Import the pygame.font module to render text
import pygame.font

class Button:
    """A class to manage buttons in the game."""
    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        # Store the game screen for later use
        self.screen = ai_game.screen
        # Get the rectangle of the screen to position the button
        self.screen_rect = self.screen.get_rect()
        # Set button width and height
        self.width, self.height = 200, 50
        # Set button color (green)
        self.play_button_color = (0, 255, 0)
        # Set difficulty button color (blue)
        self.difficulty_button_color = (0, 0, 255)
        # Set text color (white)
        self.text_color = (255, 255, 255)
        # Set font and font size
        self.font = pygame.font.SysFont(None, 35)
        # Create a rectangle for the button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # Center the button on the screen
        self.rect.center = self.screen_rect.center
        # Call method to render the message on the button
        self._prep_msg(msg)
        # Initialize an empty list for difficulty buttons
        self.difficulty_buttons = []
        # Call method to create difficulty buttons
        self.create_difficulty_buttons()

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        # Create an image of the text
        self.msg_image = self.font.render(msg, True, self.text_color, self.play_button_color)
        # Get the rectangle of the text image
        self.msg_image_rect = self.msg_image.get_rect()
        # Center the text image on the button
        self.msg_image_rect.center = self.rect.center

    def create_difficulty_buttons(self):
        """Create difficulty buttons below the Play button."""
        # Set the width of the difficulty buttons
        button_width = 200
        # Set the height of the difficulty buttons
        button_height = 50
        # Set the spacing between buttons
        spacing = 10
        # Define the difficulty levels
        difficulties = ['Beginner', 'Intermediate', 'Difficult']
        # Create a button for each difficulty level
        for i, difficulty in enumerate(difficulties):
            # Create a rectangle for the button
            button = pygame.Rect(0, 0, button_width, button_height)
            # Center the button horizontally
            button.centerx = self.screen_rect.centerx
            # Position the button vertically
            button.top = self.rect.bottom + spacing + (button_height + spacing) * i
            # Add the button and its difficulty to the list
            self.difficulty_buttons.append((button, difficulty))

    def draw_button(self):
        # Draw the button rectangle on the screen
        self.screen.fill(self.play_button_color, self.rect)
        # Draw the text on the button
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def draw_difficulty_buttons(self, ai_game):
        """Draw the difficulty buttons."""
        # Iterate through each difficulty button
        for button, difficulty in self.difficulty_buttons:
            # Set the color based on whether it's the current difficulty
            color = self.difficulty_button_color if ai_game.settings.difficulty != difficulty.lower() else (100, 100, 255)
            # Draw the button rectangle
            self.screen.fill(color, button)
            # Render the difficulty text
            msg_image = self.font.render(difficulty, True, self.text_color, color)
            # Get the rectangle of the text image
            msg_image_rect = msg_image.get_rect()
            # Center the text on the button
            msg_image_rect.center = button.center
            # Draw the text on the button
            self.screen.blit(msg_image, msg_image_rect)