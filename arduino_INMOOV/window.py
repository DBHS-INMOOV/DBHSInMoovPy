import pygame
import sys

import threading
from board import Board

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SLIDER_COLOR = (100, 100, 255)
TRACK_COLOR = (200, 200, 200)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SKIBIDI-SIGMA DEBUGGING HUD')

class Trackbar:
    def __init__(self, x, y, width, slider_pos, min_value, max_value, name):
        self.x = x  # X position of the trackbar
        self.y = y  # Y position of the trackbar
        self.width = width  # Width of the track
        self.height = 10  # Height of the track
        self.slider_width = 20  # Width of the slider
        self.slider_height = 30  # Height of the slider
        self.slider_pos = slider_pos  # Slider's initial position (between 0 and 1)
        self.min_value = min_value  # Minimum value of the slider
        self.max_value = max_value  # Maximum value of the slider
        self.name = name  # Name of the trackbar
        self.is_dragging = False  # Whether this trackbar is being dragged

    def draw(self):
        # Draw the track (the bar)
        pygame.draw.rect(screen, TRACK_COLOR, (self.x, self.y, self.width, self.height))
        
        # Calculate the current slider position
        slider_x = self.x + self.slider_pos * (self.width - self.slider_width)
        
        # Draw the slider
        pygame.draw.rect(screen, SLIDER_COLOR, (slider_x, self.y - (self.slider_height - self.height) / 2, self.slider_width, self.slider_height))

        
        # Drawing slider value to screen
        font = pygame.font.SysFont("Arial", 24)
        value_text = font.render(self.name + " : "+ f"{int(self.get_value())}", True, BLACK)
        screen.blit(value_text, (self.x + (self.width - value_text.get_width()) // 2, self.y + self.height + 5))

    def update(self, mouse_x):
        # Constrain the slider to the track's width
        if self.x <= mouse_x <= self.x + self.width:
            self.slider_pos = (mouse_x - self.x) / self.width

    def get_value(self):
        # Calculate and return the integer value of the slider
        return int(self.slider_pos * (self.max_value - self.min_value) + self.min_value)

def main():
    board = Board()

    clock = pygame.time.Clock()

    horizontalEyeMech = Trackbar(100, 25, 400, 0.5, 0, 180, "horizontal eye mech")
    verticalEyeMech = Trackbar(100, 100, 400, 0.5, 90, 160, "vertical eye mech")
    jawMech = Trackbar(100, 175, 400, 1, 0, 40, "jaw mech")

    # Create multiple trackbars
    trackbars = [
        horizontalEyeMech,
        verticalEyeMech,
        jawMech,
    ]

    while True:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Start dragging if mouse is within any trackbar
                for trackbar in trackbars:
                    if trackbar.x <= pygame.mouse.get_pos()[0] <= trackbar.x + trackbar.width and trackbar.y <= pygame.mouse.get_pos()[1] <= trackbar.y + trackbar.height:
                        trackbar.is_dragging = True  # Track this trackbar as being dragged

            if event.type == pygame.MOUSEBUTTONUP:
                # Stop dragging all trackbars when mouse button is released
                for trackbar in trackbars:
                    trackbar.is_dragging = False
                    match trackbar.name():
                        case "horizontal eye mech":
                            board.eyeMechHorizontal(trackbar.get_value())
                        case "vertical eye mech":
                            board.eyeMechVertical(trackbar.get_value())
                        case "jaw mech":
                            board.jaw(trackbar.get_value())

            if event.type == pygame.MOUSEMOTION:
                # Update the position of the slider for the trackbar being dragged
                for trackbar in trackbars:
                    if trackbar.is_dragging:
                        mouse_x = pygame.mouse.get_pos()[0]
                        trackbar.update(mouse_x)

        # Draw each trackbar and display its value
        for trackbar in trackbars:
            trackbar.draw()

        pygame.display.flip()
        clock.tick(60)

main()
