def logical_and(bin1, bin2):
    if len(bin1) != len(bin2):
        raise ValueError("Os números binários devem ter o mesmo comprimento")
    
    result = ""
    for bit1, bit2 in zip(bin1, bin2):
        if bit1 == '1' and bit2 == '1':
            result += '1'
        else:
            result += '0'
    return result
