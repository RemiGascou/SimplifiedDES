# -*- coding: utf-8 -*-

def left_circular_shift(data, shift):              #Left Circular Shift
    shift = shift%len(data)
    return data[len(data)-shift:] + data[:len(data)-shift]

if __name__ == """__main__""":
    print(lcs([1,2,3,4,5,6,7,8,9], 2))
    assert(lcs([1,2,3,4,5,6,7,8,9], 2) == [8,9,1,2,3,4,5,6,7])  #[8,9] [1,2,3,4,5,6,7]
    print(lcs([1,2,3,4,5,6,7,8,9], 5))
    assert(lcs([1,2,3,4,5,6,7,8,9], 5) == [5,6,7,8,9,1,2,3,4])
