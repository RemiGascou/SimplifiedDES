# -*- coding: utf-8 -*-

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

if __name__ == """__main__""":
    pass
