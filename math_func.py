def max2(x,y):
    if x > y:
        return x
    elif x == y:
        return 'x = y'
    else:
        return y
def max3 (x, y, z):
    return max2(x, max2(y, z))

def hi_sep(hello = 'Hello,', name = 'Alex', separator = "--" ):


print (max3(12.1, 23, 6))

