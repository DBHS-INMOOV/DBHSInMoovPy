import pyfirmata2
import time

# THE SAFE RANGES FOR THE INMOOV EYE MECH IS AROUND: (30 - 115)
# THIS IS TO REMOVE ANY BUZZING NOISES FROM THE MICRO SERVO BUT IT CAN GO A LITTLE FURTHER THAN THAT

class Board:
    def __init__(self):
        self.board = pyfirmata2.Arduino('COM5') # Might need to change: check ports in device manager on windows desktop
        self.board.digital[13].mode = pyfirmata2.SERVO
        self.servo_pin = self.board.digital[13]
        it = pyfirmata2.util.Iterator(self.board)
        it.start()

    # SAMPLE FUNCTION
    def kinematicsMovement(self, startPos : int):
        velocity = 1
        acceleration = 0.5
        timeToTravel = 2
        pos = startPos

        if pos >= 100:
            pos = 100
            while pos > 30:
                pos = pos - velocity * timeToTravel - acceleration * pow(timeToTravel,2)
                self.servo_pin.write(pos)
                print(pos)
                time.sleep(1)
        elif pos <= 30:
            pos = 30
            while pos < 100:
                pos = pos + velocity * timeToTravel + acceleration * pow(timeToTravel,2)
                self.servo_pin.write(pos)
                print(pos)
                time.sleep(1)
    
    # MAIN LOOP
    def run(self):
        try:
            while True:
                self.servo_pin.write(72.5) # starting position before user decision

                start = int(input("What angle do you want to start with?: "))
                print(f"You entered: {start} degrees.")

                self.kinematicsMovement(start)

##############################################################################################################################################
        except KeyboardInterrupt:
            self.board.exit()
            return
        except Exception as e:
            self.board.exit()
            print("ERROR: "+ str(e))

if __name__ == "__main__":
    board = Board()
    board.run()