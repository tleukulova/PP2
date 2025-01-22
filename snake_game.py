"""
1.Checking for border (wall) collision and whether the snake is leaving the playing area
2.Generate random position for food, so that it does not fall on a wall or a snake
3.Add levels. For example, when the snake receives 3-4 foods or depending on score 
4.Increase speed when the user passes to the next level
5.Add counter to score and level
6.Comment your code
"""
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
SNAKE_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up fonts
font = pygame.font.SysFont(None, 36)

# Functions


def draw_text(text, font, color, surface, x, y):
    """
    Utility function to draw text on the screen
    """
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


class Snake:
    """
    Snake class to manage the snake properties and movements
    """

    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.score = 0

    def get_head_position(self):
        """
        Get the current head position of the snake
        """
        return self.positions[0]

    def turn(self, point):
        """
        Change the direction of the snake
        """
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        """
        Move the snake
        """
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % SCREEN_WIDTH), (cur[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        """
        Reset the snake properties
        """
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0

    def draw(self, surface):
        """
        Draw the snake on the screen
        """
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)

    def check_collision(self):
        """
        Check for border (wall) collision and whether the snake is leaving the playing area
        """
        head_x, head_y = self.get_head_position()
        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
            self.reset()


class Food:

    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (SCREEN_WIDTH / GRID_SIZE - 1)) * GRID_SIZE,
                         random.randint(0, (SCREEN_HEIGHT / GRID_SIZE - 1)) * GRID_SIZE)

    def draw(self, surface):
        """
        Draw the food on the screen
        """
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)


# Game function
def main():
    running = True
    snake = Snake()
    food = Food()
    level = 1
    speed = 5

    while running:
        screen.fill(BLACK)
        snake.handle_keys()
        snake.move()
        snake.check_collision()

        snake.draw(screen)
        food.draw(screen)

        # Check if snake eats food
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()

            # Increase speed and level
            if snake.score % 3 == 0:
                level += 1
                speed += 1

        draw_text(f"Score: {snake.score}", font, WHITE, screen, 10, 10)
        draw_text(f"Level: {level}", font, WHITE, screen, SCREEN_WIDTH - 100, 10)

        pygame.display.update()
        pygame.time.Clock().tick(speed)


if __name__ == "__main__":
    main()

