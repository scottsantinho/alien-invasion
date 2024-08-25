# Alien Invasion

<img width="1199" alt="Screenshot 2024-08-25 at 6 40 30 PM" src="https://github.com/user-attachments/assets/fff2d4a6-b14b-4f06-a45d-a79b6e6e0210">

## Table of Contents
1. [Description](#description)
2. [Features](#features)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
4. [How to Play](#how-to-play)
5. [Game Controls](#game-controls)
6. [Customization](#customization)
7. [Project Structure](#project-structure)
8. [Contributing](#contributing)
9. [License](#license)
10. [Acknowledgments](#acknowledgments)

## Description

Alien Invasion is an exciting space-themed shooter game built with Python and Pygame. In this classic-style arcade game, players control a spaceship to defend Earth against waves of descending alien invaders. The game features increasing difficulty levels, a dynamic scoring system, and multiple lives for the player.

## Features

- Smooth spaceship movement and shooting mechanics
- Dynamic alien fleet that increases in speed and difficulty
- Scoring system with high score tracking
- Multiple difficulty levels
- Sound effects for enhanced gameplay experience
- Responsive controls and collision detection
- Colorful graphics and animations

## Getting Started

### Prerequisites

To run Alien Invasion, you'll need:

- Python 3.x
- Pygame library

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/scottsantinho/alien-invasion.git
   ```

2. Navigate to the project directory:
   ```
   cd alien-invasion
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## How to Play

1. Run the game:
   ```
   python alien_invasion.py
   ```

2. Click the "Play" button to start the game.
3. Use the arrow keys to move your ship left and right.
4. Press the spacebar to shoot bullets at the aliens.
5. Destroy all aliens to advance to the next level.
6. The game ends when an alien reaches the bottom of the screen or collides with your ship (by default, the player has 3 lives).

## Game Controls

- **←** : Move ship left
- **→** : Move ship right
- **Spacebar** : Fire bullet
- **Q** : Quit game

## Customization

You can customize various aspects of the game by modifying the `settings.py` file:

- Screen dimensions
- Ship speed
- Bullet properties
- Alien fleet characteristics
- Scoring values

## Project Structure

## Project Structure

- alien_invasion/
  - alien_invasion.py    # Main game file
  - settings.py          # Game settings and configuration
  - ship.py              # Ship class definition
  - alien.py             # Alien class definition
  - bullet.py            # Bullet class definition
  - game_stats.py        # Game statistics tracking
  - scoreboard.py        # Scoreboard display
  - button.py            # Button class for UI elements
  - sound_effects.py     # Sound effects management
  - images/              # Directory for game images
    - ship.bmp
    - alien.bmp
  - sounds/              # Directory for sound files
    - shoot.wav
    - explosion.wav
  - README.md
  - LICENSE
  - requirements.txt

## Contributing

While Alien Invasion is a modest project, I am very much open to contributions! If you'd like to contribute, here's how:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch-name`
5. Submit a pull request

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Eric Matthes, whose project in "Python Crash Course" served as the inspiration for this game.
- The Pygame community for their comprehensive documentation and illustrative examples.
- [Cursor.ai](https://www.cursor.sh/) and Claude 3.5 Sonnet for assistance in refactoring, commenting the code and writing this beautiful README.md !
- [Bfxr](https://www.bfxr.net/), the tool used to generate my game's sound effects.
- [OpenGameArt](https://opengameart.org/) for providing the alien and spaceship images used in the game.
