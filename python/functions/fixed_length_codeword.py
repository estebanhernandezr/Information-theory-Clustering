import numpy as np

def d2r(radix, decnum, current):
    res = decnum % radix
    decnum = decnum // radix
    if decnum == 0:
        return str(res) + current
    else:
        return d2r(radix, decnum, str(res) + current)

def dec2radix(radix, decnum):
    return d2r(radix, decnum, '')

def radix2dec(radix, rnum):
    dec = 0
    for i in range(0,len(rnum)):
        dec += int(rnum[len(rnum)-i-1])*(radix**i)
    return dec

def d2a(alphabet, decnum, current):
    radix = len(alphabet)
    res = decnum % radix
    decnum = decnum // radix
    if decnum == 0:
        return alphabet[res] + current
    else:
        return d2a(alphabet, decnum, alphabet[res] + current)

def dec2alpha(alphabet, decnum):
    return d2a(alphabet, decnum, '')

def codeWord(pos, size, char, n, l):
    cd = dec2alpha(['0', '1'], pos).rjust(int(np.ceil(np.log(n-l) / np.log(2))), '0')
    cd += dec2alpha(['0', '1'], size).rjust(int(np.ceil(np.log(l) / np.log(2))), '0')
    cd += char
    return cd