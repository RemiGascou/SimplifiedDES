# -*- coding: utf-8 -*-

from lib.expander import *
from lib.sboxes import *
from lib.pboxes import *

def fk(data, subkey, verbose = False):
    print("[ fk ] Entering fk with data:", data, "and subkey :",subkey)
    def F(R, subkey):
        print(" | [F(R,S)] Entering F with R:", R, "and subkey :",subkey)
        if len(R) == 4:
            #eR = expander(R)
            #print("    | expander(R) :",eR)
            eR = R
            p = [
                [str(int(R[3]) ^ int(subkey[0])), str(int(R[0]) ^ int(subkey[1])), str(int(R[1]) ^ int(subkey[2])), str(int(R[2]) ^ int(subkey[3]))],
                [str(int(R[1]) ^ int(subkey[4])), str(int(R[2]) ^ int(subkey[5])), str(int(R[3]) ^ int(subkey[6])), str(int(R[0]) ^ int(subkey[7]))]
            ]
            sb1 = sbox1(p[0][0], p[0][1], p[0][2], p[0][3])
            sb2 = sbox2(p[1][0], p[1][1], p[1][2], p[1][3])
            print("    | sbox1(",','.join([p[0][0], p[0][1], p[0][2], p[0][3]]),") : ",sb1, sep = "")
            print("    | sbox2(",','.join([p[1][0], p[1][1], p[1][2], p[1][3]]),") : ",sb2, sep = "")
            out = p4(sb1 + sb2)
            #out = p4(sbox1(p[0][0], p[0][1], p[0][2], p[0][3]) + sbox2(p[1][0], p[1][1], p[1][2], p[1][3]))
            print(" | [F(R,S)] Leaving F returning data           :",out)
            return out
        return None
    def ors(a, b):
        print(" | [ORS ] Entering ors with a:", a, "and b :",b)
        if len(a) == len(b):
            output = ''.join([str(int(a[k]) ^ int(b[k])) for k in range(len(a))]) # ^ = xor
            print(" | [ORS ] Leaving ors with output:", output)
            return output
        return None
    if len(data) == 8:
        L = data[:int(len(data)/2)]
        R = data[int(len(data)/2):]
        print(" | ors(L,F(R, subkey)) + R =",ors(L,F(R, subkey)),"+",R)
        out = ors(L,F(R, subkey)) + R #none : F(R, subkey)
        print("[ fk ] Leaving fk returning data  :",out)
        return out
    return None

##
if __name__ == """__main__""":
    assert(xors("1011", "1110") == "0101")
