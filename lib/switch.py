# -*- coding: utf-8 -*-

def switch(data, verbose = False):
    if verbose:
        print("[ SW ] Entering switch with data :", data)
    if len(data) == 8:
        if verbose:
            print("[ SW ] Leaving switch with data  :", data[int(len(data)/2):] + data[:int(len(data)/2)])
        return data[int(len(data)/2):] + data[:int(len(data)/2)]
    return None


if __name__ == """__main__""":
    #print("00101111")
    #print(switch("00101111"))
    assert(switch("00101111") == "11110010")
