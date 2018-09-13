# -*- coding: utf-8 -*-

def sbox1(a, b, c, d):
    box = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    row = int("0b"+''.join(map(str, [a,d])), 2)
    column = int("0b"+''.join(map(str, [b,c])), 2)
    #print("Row:", row, "Column:", column, "=>", box[row][column])
    return bin(box[row][column])[2:].ljust(2,"0")


def sbox2(a, b, c, d):
    box = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
    row = int("0b"+''.join(map(str, [a,d])), 2)
    column = int("0b"+''.join(map(str, [b,c])), 2)
    #print("Row:", row, "Column:", column, "=>", box[row][column])
    return bin(box[row][column])[2:].ljust(2,"0")

if __name__ == """__main__""":
    a, b, c, d = 0,1,0,0
    assert(sbox1(a, b, c, d) == "11")
