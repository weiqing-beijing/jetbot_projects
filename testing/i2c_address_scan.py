import time
import board
import busio

#for jetson nano, use board.SDA(pin#3)/SCL(pin#5) or board.SDA_1(pin#27)/SCL_1(pin#28) as there are two i2c ports available 
i2c = busio.I2C(board.SCL_1, board.SDA_1)

print("I2C devices found: ", [hex(i) for i in i2c.scan()])
