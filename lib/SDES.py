# -*- coding: utf-8 -*-

from lib.keygen import *
from lib.initial_permutation import *
from lib.fk import *
from lib.switch import *

def SDES_encrypt(message, key):
    subkey1, subkey2 = keygen(key)
    buffer = initial_permutation(message)
    buffer = fk(buffer, subkey1)
    switch(buffer)
    buffer = fk(buffer, subkey2)
    cipher = initial_permutation_reverse(buffer)
    return cipher

def SDES_decrypt(cipher, key):
    subkey1, subkey2 = keygen(key)
    buffer = initial_permutation_reverse(cipher)
    buffer = fk(buffer, subkey2)
    switch(buffer)
    buffer = fk(buffer, subkey1)
    message = initial_permutation(buffer)
    return message

if __name__ == """__main__""":
    print(SDES_encrypt("10101010", "0000000000"))
    assert(SDES_encrypt("10101010", "0000000000") == "00010001")

    print(SDES_encrypt("10101010", "1110001110"))
    assert(SDES_encrypt("10101010", "1110001110") == "11001010")

    print(SDES_encrypt("01010101", "1110001110"))
    assert(SDES_encrypt("01010101", "1110001110") == "01110000")

    print(SDES_encrypt("10101010", "1111111111"))
    assert(SDES_encrypt("10101010", "1111111111") == "00000100")
