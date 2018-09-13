# -*- coding: utf-8 -*-

from lib.expander import *
from lib.sboxes import *
from lib.pboxes import *

def fk(data, subkey, table=[2,6,3,1,4,8,5,7]):
    print("[ fk ] Entering fk with data:", data, "and subkey :",subkey)
    def F(R, subkey):
        print(" | [F(R,S)] Entering F with R:", R, "and subkey :",subkey)
        def expander(data, table=[4,1,2,3,2,3,4,1]):
            if len(data) == 4:
                return ''.join([data[k-1] for k in table])
            return None
        if len(R) == 4:
            eR = expander(R)
            p = [
                [str(int(eR[3]) ^ int(subkey[0])), str(int(eR[0]) ^ int(subkey[1])), str(int(eR[1]) ^ int(subkey[2])), str(int(eR[2]) ^ int(subkey[3]))],
                [str(int(eR[1]) ^ int(subkey[4])), str(int(eR[2]) ^ int(subkey[5])), str(int(eR[3]) ^ int(subkey[6])), str(int(eR[0]) ^ int(subkey[7]))]
            ]
            out = p4(sbox1(p[0][0], p[0][1], p[0][2], p[0][3]) + sbox2(p[1][0], p[1][1], p[1][2], p[1][3]))
            print(" | [F(R,S)] Leaving F returning data           :",out)
            return out
        return None
    def ors(a, b):
        if len(a) == len(b):
            output = ''.join([str(int(a[k]) ^ int(b[k])) for k in range(len(a))]) # ^ = xor
            return output
        return None
    if len(data) == 8:
        L = data[:int(len(data)/2)]
        R = data[int(len(data)/2):]
        out = ors(L,F(R, subkey)) + R #none : F(R, subkey)
        print("[ fk ] Leaving fk returning data  :",out)
        return out
    return None

##
if __name__ == """__main__""":
    assert(xors("1011", "1110") == "0101")
