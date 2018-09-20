
##---------------------------------------------------------- Left Circular Shift * OK
def left_circular_shift(data, shift):
    shift = shift%len(data)
    #return data[len(data)-shift:] + data[:len(data)-shift] <- Right Circular Shift
    return data[shift:len(data)] + data[:shift]

##----------------------------------------------------------------------- PBOXES * OK
def p8(data, verbose = False, table=[6,3,7,4,8,5,10,9]):
    if len(data) == 10:
        return ''.join([data[k-1] for k in table])
    return None

def p10(data, verbose = False, table = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]):
    if len(data) == 10:
        return ''.join([data[k-1] for k in table])
    return None

def p4(data, verbose = False, table=[2,4,3,1]):
    if len(data) == 4:
        return ''.join([data[k-1] for k in table])
    return None

##----------------------------------------------------------------------- SBOXES * OK

def sbox1(a, b, c, d):
    box = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    row = int("0b"+''.join(map(str, [a,d])), 2)
    column = int("0b"+''.join(map(str, [b,c])), 2)
    return bin(box[row][column])[2:].ljust(2,"0")


def sbox2(a, b, c, d):
    box = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
    row = int("0b"+''.join(map(str, [a,d])), 2)
    column = int("0b"+''.join(map(str, [b,c])), 2)
    return bin(box[row][column])[2:].ljust(2,"0")

##----------------------------------------------------------------------- keygen * OK
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

##----------------------------------------------------------------------------IP * OK
def initial_permutation(data, verbose = False, table=[2,6,3,1,4,8,5,7]):
    if verbose:
        print("[ IP ] Entering initial_permutation with data :", data)
    if len(data) == 8:
        if verbose:
            print("[ IP ] Leaving initial_permutation with data  :", ''.join([data[k-1] for k in table]))
        return ''.join([data[k-1] for k in table])
    return None

def initial_permutation_reverse(data, verbose = False, table=[4,1,3,5,7,2,8,6]):
    if verbose:
        print("[IP-1] Entering initial_permutation_reverse with data :", data)
    if len(data) == 8:
        if verbose:
            print("[IP-1] Leaving initial_permutation_reverse with data  :", ''.join([data[k-1] for k in table]))
        return ''.join([data[k-1] for k in table])
    return None

##--------------------------------------------------------------------- expander * OK

def expander(data, verbose = False, table=[4,1,2,3,2,3,4,1]):
    if len(data) == 4:
        return ''.join([data[k-1] for k in table])
    return None

##--------------------------------------------------------------------------- fk

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

##----------------------------------------------------------------------- switch * OK

def switch(data, verbose = False):
    if verbose:
        print("[ SW ] Entering switch with data :", data)
    if len(data) == 8:
        if verbose:
            print("[ SW ] Leaving switch with data  :", data[int(len(data)/2):] + data[:int(len(data)/2)])
        return data[int(len(data)/2):] + data[:int(len(data)/2)]
    return None

##------------------------------------------------------------------------- SDES * OK

def SDES_encrypt(message, key):
    subkey1, subkey2 = keygen(key)
    buffer = initial_permutation(message)
    buffer = fk(buffer, subkey1)
    buffer = switch(buffer)
    buffer = fk(buffer, subkey2)
    cipher = initial_permutation_reverse(buffer)
    return cipher

def SDES_decrypt(cipher, key):
    subkey1, subkey2 = keygen(key)
    buffer = initial_permutation_reverse(cipher)
    buffer = fk(buffer, subkey2)
    buffer = switch(buffer)
    buffer = fk(buffer, subkey1)
    message = initial_permutation(buffer)
    return message

if __name__ == """__main__""":
    #print(SDES_encrypt("10101010", "0000000000"))
    #assert(SDES_encrypt("10101010", "0000000000") == "00010001")

    #print(SDES_encrypt("10101010", "1110001110"))
    assert(SDES_encrypt("10101010", "1110001110") == "11001010")

    #print(SDES_encrypt("01010101", "1110001110"))
    assert(SDES_encrypt("01010101", "1110001110") == "01110000")

    #print(SDES_encrypt("10101010", "1111111111"))
    assert(SDES_encrypt("10101010", "1111111111") == "00000100")
