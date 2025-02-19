from board import Board
from Objects import Trackbar, Button

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
SLIDER_COLOR = (100, 100, 255)
TRACK_COLOR = (200, 200, 200)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('BIG BOOM REMI DEBUGGING HUD')

def main():
    board = Board()

    clock = pygame.time.Clock()

    #horizontalEyeMech = Trackbar(100, 25, 400, 0.5, 0, 180, "horizontal eye mech")
    #verticalEyeMech = Trackbar(100, 100, 400, 0.5, 90, 160, "vertical eye mech")
    jawMech = Trackbar.Trackbar(100, 175, 400, 0, 0, 80, "jaw mech")

    # Create multiple trackbars
    trackbars = [
        #horizontalEyeMech,
        #verticalEyeMech,
        jawMech,
    ]

    objects = []

    for i in trackbars:
        objects.append(i)

    for object in objects:
        print(object.getName())

    currentAngle = 0

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
                    match trackbar.name:
                        # case "horizontal eye mech":
                        #     board.eyeMechHorizontal(trackbar.get_value())
                        #     print(trackbar.get_value())
                        # case "vertical eye mech":
                        #     board.eyeMechVertical(trackbar.get_value())
                        #     print(trackbar.get_value())
                        case "jaw mech":
                            if currentAngle == trackbar.get_value():
                                print("Same Angle (no change to angle)")
                                continue
                            currentAngle = trackbar.get_value()
                            
                            board.jaw(trackbar.get_value())
                            print(trackbar.get_value())

                    print(trackbar.get_value())

            if event.type == pygame.MOUSEMOTION:
                # Update the position of the slider for the trackbar being dragged
                for trackbar in trackbars:
                    if trackbar.is_dragging:
                        mouse_x = pygame.mouse.get_pos()[0]
                        trackbar.update(mouse_x)

        # Draw each trackbar and display its value
        for trackbar in trackbars:
            trackbar.draw(screen,TRACK_COLOR,SLIDER_COLOR)

        pygame.display.flip()
        clock.tick(60)

main()
