
##---------------------------------------------------------- Left Circular Shift
def left_circular_shift(data, shift):
    shift = shift%len(data) #Used to avoid overflows
    return ...

##----------------------------------------------------------------------- PBOXES
def p8(data, table=[6,3,7,4,8,5,10,9]):
    if len(data) == 10:
        return ...
    return None

def p10(data, table = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]):
    if len(data) == 10:
        return ...
    return None

def p4(data, table=[2,4,3,1]):
    if len(data) == 4:
        return ...
    return None

##----------------------------------------------------------------------- SBOXES

def sbox1(a, b, c, d):
    box = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    row = ...
    column = ...
    return bin(box[row][column])[2:].ljust(2,"0")


def sbox2(a, b, c, d):
    box = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
    row = ...
    column = ...
    return bin(box[row][column])[2:].ljust(2,"0")

##----------------------------------------------------------------------- keygen
def keygen(key):
    key = ...
    rkey, lkey = ..., ...
    subkey1 = ...
    subkey2 = ...
    return subkey1, subkey2

##----------------------------------------------------------------------------IP
def initial_permutation(data, table=[2,6,3,1,4,8,5,7]):
    print("[ IP ] Entering initial_permutation with data :", data)
    if len(data) == 8:
        out = ...
        print("[ IP ] Leaving initial_permutation with data  :", out)
        return out
    return None

def initial_permutation_reverse(data, table=[4,1,3,5,7,2,8,6]):
    print("[IP-1] Entering initial_permutation_reverse with data :", data)
    if len(data) == 8:
        out = ...
        print("[IP-1] Leaving initial_permutation_reverse with data  :", out)
        return out
    return None

##--------------------------------------------------------------------- expander

def expander(data, table=[4,1,2,3,2,3,4,1]):
    if len(data) == 4:
        return ...
    return None

##--------------------------------------------------------------------------- fk

def fk(data, subkey, table=[2,6,3,1,4,8,5,7]):
    print("[ fk ] Entering fk with data:", data, "and subkey :",subkey)
    def F(R, subkey):
        print(" | [F(R,S)] Entering F with R:", R, "and subkey :",subkey)
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

##----------------------------------------------------------------------- switch

def switch(data):
    print("[ SW ] Entering switch with data :", data)
    if len(data) == 8:
        print("[ SW ] Leaving switch with data  :", data[int(len(data)/2):] + data[:int(len(data)/2)])
        return ...
    return None

##------------------------------------------------------------------------- SDES

def SDES_encrypt(message, key):
    cipher = ""
    return cipher

def SDES_decrypt(cipher, key):
    message = ""
    return message

if __name__ == """__main__""":
    print(SDES_encrypt("10101010", "0000000000"))
