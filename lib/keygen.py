from lib.left_circular_shift import *
from lib.pboxes import *

def keygen(key):
    def lcs(data, shift):              #Left Circular Shift
        shift = shift%len(data)
        return data[len(data)-shift:] + data[:len(data)-shift]
    key = p10(key)
    rkey, lkey = key[int(len(key)/2):], key[:int(len(key)/2)]
    subkey1 = p8(left_circular_shift(lkey, 1) + lcs(rkey, 1))
    subkey2 = p8(left_circular_shift(left_circular_shift(lkey, 2), 1) + left_circular_shift(left_circular_shift(rkey, 2), 1))
    return subkey1, subkey2

if __name__ == """__main__""":
    print(keygen("1010000010"))
    assert(keygen("1010000010") == ('00001001', '10010010'))
