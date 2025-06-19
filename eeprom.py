# SPDX-FileCopyrightText: Copyright (c) 2021 Tim Cocks for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

import board
import adafruit_24lc32
from busio import I2C

i2c = I2C(board.GP27,board.GP26)  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
eeprom = adafruit_24lc32.EEPROM_I2C(i2c)

print("length: {}".format(len(eeprom)))

# eeprom[0] = 49
print(eeprom[0])

# eeprom[1:10] = [83, 69, 69, 78, 71, 82, 69, 65, 84] #"SEENGREAT"
print(eeprom[1:10])
