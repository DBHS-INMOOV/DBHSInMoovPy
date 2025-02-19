import pygame, ObjectTemplate

class Button(ObjectTemplate):
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False, name="a button"):
        super().__init__(name,x,y)
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.buttonText = buttonText

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }