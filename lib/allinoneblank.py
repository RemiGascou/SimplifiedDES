

def expander(data, table=[4,1,2,3,2,3,4,1]):
    if len(data) == 8:
        return ''.join([data[k-1] for k in table])
    return None


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
    pass
