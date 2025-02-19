import pyfirmata2
import time
import pins

class Board:
    def __init__(self):
        self.board = pyfirmata2.Arduino('COM3')
        self.board = pyfirmata2.Arduino('COM4')
        pyfirmata2.util.Iterator(self.board).start()

        for pin in pins.pins():
            self.board.digital[pin].mode = pyfirmata2.SERVO

        match pin:
            case pins.EYE_HORIZONTAL: 
                self.HorizontalEye = self.board.digital[pin]
            case pins.EYE_VERTICAL: 
                self.VerticalEye = self.board.digital[pin]
            case pins.JAW: 
                self.Jaw = self.board.digital[pin]
            case _: 
                print(f"ERROR with pin {pin}")

    def eyeMechHorizontal(self, angle):

        # Soft Max Ranges: 0 - 180

        if (angle <= 180 and angle >= 0):
            self.HorizontalEye.write(angle)
        else:
            print("ERROR: angle must be between 0 and 180")

    def jaw(self, angle):

            # Soft Max Ranges: 0 - 40
        
        if (angle <= 40 and angle >= 0):
            self.Jaw.write(angle)
        else:
            print("ERROR: angle must be between 0 and 40")

    def eyeMechVertical(self, angle):

        # Soft Max Ranges: 90 - 160

        if (angle <= 160 and angle >= 90):
            self.VerticalEye.write(angle)
        else:
            print("ERROR: angle must be between 90 and 160")
