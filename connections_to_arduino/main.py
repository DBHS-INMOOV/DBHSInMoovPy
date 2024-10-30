import pyfirmata2

# Servo demo on port 5. The default frequency is 50Hz approx.
# Lowest dutycycle (1ms) at 0 degrees and highest (2ms) at 180 degrees.

# Adjust that the port match your system, see samples below:
# On Linux: /dev/tty.usbserial-A6008rIF, /dev/ttyACM0,
# On Windows: \\.\COM1, \\.\COM2
# PORT = '/dev/ttyACM0'

# Creates a new board
board = pyfirmata2.Arduino('\\.\COM5')
print("Setting up the connection to the board ...")

# Setup the digital pin as servo
servo_5 = board.get_pin('d:12:s')

v = float(input("Servo angle from 0 to 180 degrees: "))

# Set the duty cycle
servo_5.write(v)

# just idle here
input("Press enter to exit")

# Close the serial connection to the Arduino
board.exit()