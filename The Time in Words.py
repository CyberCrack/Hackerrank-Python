def timeInWords(h, m):
    d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty',
         30: 'thirty', 40: 'forty', 45: 'quarter', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninety'}
    if m == 00:
        return d[h] + " o' clock"
    elif m == 15:
        return "quarter past " + d[h]
    elif m == 30:
        return "half past " + d[h]
    elif m >= 1 and m < 30:
        o = m % 10
        t = m - o
        if o != 0 and t != 0:
            return d[t] + " " + d[o] + " minutes past " + d[h]
        elif t == 0 and h != 1:
            return d[o] + " minutes past " + d[h]
        elif h == 1:
            return d[o] + " minute past " + d[h]
        else:
            return d[t] + " minutes past " + d[h]
    elif m == 45:
        if not h == 12:
            return "quarter to " + d[h + 1]
        else:
            return "quarter to " + d[1]
    elif m > 30 and m <= 59:
        r = 60 - m

        if r >= 21:
            o = r % 10
            t = r - o
            if h != 12:
                return d[t] + " " + d[o] + " minutes to " + d[h + 1]
            else:
                return d[r] + " " + d[o] + " minutes to " + d[1]
        else:
            if h != 12:
                return d[r] + " minutes to " + d[h + 1]
            else:
                return d[r] + " minutes to " + d[1]


print(timeInWords(1,1))
