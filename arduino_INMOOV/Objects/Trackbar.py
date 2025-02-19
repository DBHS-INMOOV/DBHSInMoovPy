import pygame, ObjectTemplate
class Trackbar(ObjectTemplate):
    def __init__(self, x, y, width, slider_pos, min_value, max_value, name):
        super().__init__(name,x,y)
        self.width = width  # Width of the track
        self.height = 10  # Height of the track
        self.slider_width = 20  # Width of the slider
        self.slider_height = 30  # Height of the slider
        self.slider_pos = slider_pos  # Slider's initial position (between 0 and 1)
        self.min_value = min_value  # Minimum value of the slider
        self.max_value = max_value  # Maximum value of the slider
        self.is_dragging = False  # Whether this trackbar is being dragged

    def draw(self, screen, TRACK_COLOR, SLIDER_COLOR):
        # Draw the track (the bar)
        pygame.draw.rect(screen, TRACK_COLOR, (super.getX(), super.getY(), self.width, self.height))
        
        # Calculate the current slider position
        slider_x = super.getX() + self.slider_pos * (self.width - self.slider_width)
        
        # Draw the slider
        pygame.draw.rect(screen, SLIDER_COLOR, (slider_x, super.getY() - (self.slider_height - self.height) / 2, self.slider_width, self.slider_height))

        
        # Drawing slider value to screen
        font = pygame.font.SysFont("Arial", 24)
        value_text = font.render(self.super.getName() + " : "+ f"{int(self.get_value())}", True, (0, 0, 0)) # Black colored text
        screen.blit(value_text, (super.getX() + (self.width - value_text.get_width()) // 2, super.getY() + self.height + 5))

    def update(self, mouse_x):
        # Constrain the slider to the track's width
        if super.getX() <= mouse_x <= super.getX() + self.width:
            self.slider_pos = (mouse_x - super.getX()) / self.width

    def get_value(self):
        # Calculate and return the integer value of the slider
        return int(self.slider_pos * (self.max_value - self.min_value) + self.min_value)