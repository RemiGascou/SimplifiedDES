# -*- coding: utf-8 -*-

from lib.left_circular_shift import *
from lib.pboxes import *

def keygen(key, verbose = False):
    if verbose:
        print("[KEYG] Entering KEYGEN")
    key = p10(key)
    rkey, lkey = key[int(len(key)/2):], key[:int(len(key)/2)]
    if verbose:
        print("[KEYG] rkey, lkey                = ", rkey, lkey)
        print("[KEYG] LCS(rkey,1) , LCS(lkey,1) = ", left_circular_shift(rkey, 1), left_circular_shift(lkey, 1))
        print("[KEYG] LCS(rkey,2) , LCS(lkey,2) = ", left_circular_shift(rkey, 2), left_circular_shift(lkey, 2))
    subkey1 = p8(left_circular_shift(lkey, 1) + left_circular_shift(rkey, 1))
    subkey2 = p8(left_circular_shift(lkey, 3) + left_circular_shift(rkey, 3))
    if verbose:
        print("[KEYG] Exiting KEYGEN with :\n | subkey1 :",subkey1,"\n | subkey2 :",subkey2)
    return subkey1, subkey2

if __name__ == """__main__""":
    print(keygen("1010000010"))
    assert(keygen("1010000010") == ('00001001', '10010010'))
