import pyfirmata2
import time
import pins

class Board:

    def __init__(self):
        self.board = pyfirmata2.Arduino('COM5')
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
                case _ : 
                    print(f"ERROR with pin {pin}")

    def eyeMechHorizontalTest(self):

        # Soft Max Ranges: 0 - 180

        self.HorizontalEye.write(90) # NEUTRAL
        time.sleep(2)
        self.HorizontalEye.write(180) # LEFT
        time.sleep(2)
        self.HorizontalEye.write(0) # RIGHT
        time.sleep(2)

    def jawTest(self):

        # Soft Max Ranges: 0 - 40

        self.VerticalEye.write(0) # CLOSED/NEUTRAL
        time.sleep(2)
        self.VerticalEye.write(40) # OPEN
        time.sleep(2)

    def eyeMechVerticalTest(self):

        # soft Ranges: 90-160

        self.Jaw.write(135) # NAUTRAL
        time.sleep(2)
        self.Jaw.write(160) # UP
        time.sleep(2)
        self.Jaw.write(90) # DOWN
        time.sleep(2)


    # MAIN LOOP
    def run(self):
        try:
            while True:
                self.eyeMechVerticalTest()
                self.eyeMechHorizontalTest()
                self.jawTest()


















##############################################################################################################################################
        except KeyboardInterrupt:
            self.board.exit()
        except Exception as e:
            self.board.exit()
            print("ERROR: "+ str(e))