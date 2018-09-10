def expander(data, table=[4,1,2,3,2,3,4,1]):
    if len(data) == 8:
        return ''.join([data[k-1] for k in table])
    return None
