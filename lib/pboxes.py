def p8(data, table=[6,3,7,4,8,5,10,9]):
    if len(data) == 10:
        return ''.join([data[k-1] for k in table])
    return None

def p10(data, table = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]):
    if len(data) == 10:
        return ''.join([data[k-1] for k in table])
    return None

def p4(data, table=[2,4,3,1]):
    if len(data) == 4:
        return ''.join([data[k-1] for k in table])
    return None
