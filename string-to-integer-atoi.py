class Solution:
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
            elif i == 0:  # unless it's the first char and negative or pos
                if a[i] == '-':
                    neg = True
                elif a[i] == '+':  # if it's a +, don't need to do anything
                    pass
                else:  # don't let any other char's through
                    break
            else:
                break
        if len(b) == 0 or b == '-':
            return 0  # handle null cases
        if neg:
            return max(-int(b), -(2**31))  # else convert to int and return
        return min(int(b), 2**31-1)