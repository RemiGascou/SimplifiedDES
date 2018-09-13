# -*- coding: utf-8 -*-
##SDES implementation

from lib import *


print(SDES_encrypt("10101010", "0000000000"))
print()
#assert(SDES_encrypt("10101010", "0000000000") == "00010001")

#print(SDES_encrypt("10101010", "1110001110"))
#assert(SDES_encrypt("10101010", "1110001110") == "11001010")

#print(SDES_encrypt("01010101", "1110001110"))
#assert(SDES_encrypt("01010101", "1110001110") == "01110000")

#print(SDES_encrypt("10101010", "1111111111"))
#assert(SDES_encrypt("10101010", "1111111111") == "00000100")
