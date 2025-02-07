import pyfirmata2 as pyf
import time

board = pyf.Arduino('COM3')
pyf.util.Iterator(board).start()

pin = board.digital[13]

pin.mode = pyf.SERVO

while True:
    pin.write(0)
    time.sleep(2)
    pin.write(180)
    time.sleep(2)
    print("hello")