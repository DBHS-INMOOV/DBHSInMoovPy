import pyfirmata2
import time
import pins

class Board:
    def __init__(self):
        try:
            self.board = pyfirmata2.Arduino('COM5')
            time.sleep(2)
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
                        print(f"No ASSIGNMENT to PIN {pin}")
        except Exception as e:
            print(f"Initialization error: {e}")
            raise

    def jawTest(self):
        try:
            print("Jaw Test: Neutral Position")
            self.Jaw.write(0)  # CLOSED/NEUTRAL
            time.sleep(1)
            
            print("Jaw Test: Open Position")
            self.Jaw.write(80)  # OPEN
            time.sleep(1)
        except Exception as e:
            print(f"Jaw Test Error: {e}")
            raise

    def verticaleyeTest(self):
        try:
            print("V.Eye Test: Neutral Position")
            self.VerticalEye.write(110)  # NEUTRAL
            time.sleep(1)
            
            print("V.Eye Test: Looking Up Position")
            self.VerticalEye.write(70)  # UP
            time.sleep(1)

            print("V.Eye Test: Looking Down Position")
            self.VerticalEye.write(160)  # DOWN
            time.sleep(1)
        except Exception as e:
            print(f"Vertical Eye Test Error: {e}")
            raise

    def horizontaleyeTest(self):
        try:
            print("H.Eye Test: Neutral Position")
            self.HorizontalEye.write(90)  # NEUTRAL
            time.sleep(1)
            
            print("H.Eye Test: Looking Left")
            self.HorizontalEye.write(0)  # LEFT
            time.sleep(1)

            print("H.Eye Test: Looking Right")
            self.HorizontalEye.write(180)  # RIGHT
            time.sleep(1)
        except Exception as e:
            print(f"Vertical Eye Test Error: {e}")
            raise

    def run(self):
        try:
            while True:
                self.jawTest()
                #self.verticaleyeTest()
                #self.horizontaleyeTest()
                time.sleep(0.5)  # Add a small delay between iterations









































































































##############################################################################################################################################################################################################
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"Runtime Error: {e}")
        finally:
            if hasattr(self, 'board'):
                try:
                    self.board.exit()
                    print("Board successfully closed")
                except Exception as exit_error:
                    print(f"Error during board exit: {exit_error}")