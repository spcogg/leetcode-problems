def myAtoi(self, x: str) -> int:
    if x == '':  # handle empty case
        print(0)
        return 0
    a = x.lstrip()  # strip left spaces
    # add char to a new str, continue until non-numeric reached
    b = ''
    neg = False
    for i in range(len(a)):  # check every char
        if a[i].isnumeric():  # only add numerics
            b += a[i]
            print(b)
        # this implementation is problmatic because things can slip throuhg
        # the first char check 
        # elif i == 1:  # unless it's the first char, then check if negative
        #    if a[i] == '-':
        #        neg = True  # remember & handle later
        # also need to handle the 
        elif i == 0 and a[i] == '-':  # unless it's the first char and negative 
            neg = True  # remember & handle later    
        else:
            break
    print(b)
    if len(b) == 0 or b == '-':
        return 0  # handle null cases
    if neg:
        return -int(b)  # else convert to int and return
    else:
        return int(b)


# adhoc tests
"""
a = '012 - fewa'
a[0].isnumeric()
a[0].isspace()
a[3].isspace()
a[4]
a[4].isspace()
a[4] == '-'
a[4].isspace() or a[4] == '-'
del(a[0])  # str doesn't support item deletion

c ='       -2323 abc'
c.lstrip()
c -= ' '
list(c.lstrip())

1 == 1 and 2 != 2

-int('32')

"""