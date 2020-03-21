import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Import libs for video playback
import sys
import os
from subprocess import Popen

# Software SPI configuration
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

print('Reading MCP3008 values, press Ctrl-C to quit...')

# Define the mcp analog input channel. Changes depending on which input connected to on MCP3008.
INPUT_CH = 7

# Define movie location
movie = ('../PensieveMovie.mp4')

# Main program loop
while True:

    input_value = mcp.read_adc(INPUT_CH)

    if(input_value == 0):
        print('No water detected \n')
    elif(input_value > 200):
        print('Water detected, value: ' + str(input_value))
        omxc = Popen(['omxplayer', '-b', '-o', 'local', '--win', '480 270 1440 810', movie])
        break

    time.sleep(1)
