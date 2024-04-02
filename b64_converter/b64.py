# base64 text encoder/decoder! (only works on .txt files)
# 1st cmdline arg is -e/-d (encode/decode)
# 2nd is input filename
# 3rd is output filename

import sys

usage = """Correct usage:
1st arg is -e/-d (encode/decode)
2nd arg is input filename
3rd arg is output filename"""

if len(sys.argv) != 4:
    print(usage)
    sys.exit()

table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
bits = ""
padding = 0

if "-e" in sys.argv[1]:
    inf = open(sys.argv[2], "rb")
    outf = open(sys.argv[3], "w")
    input = inf.read()
    # 1s and 2s must be switched to determine the
    # appropriate amount of "="'s based on the number of
    # missing bits
    padding = len(input) % 3
    if padding == 1:
        padding = 2
    elif padding == 2:
        padding = 1
    for char in input:
        byte = f"{char:08b}"
        bits = "".join([bits, f"{byte}"])
    bits = "".join([bits, "00"*padding])
    code = ""
    i = 0
    while i < len(bits):
        code = "".join([code, f"{table[int(bits[i:i+6], 2)]}"])
        i += 6
    code = "".join([code, "="*padding])
    outf.write(code)
elif "-d" in sys.argv[1]:
    inf = open(sys.argv[2], "r")
    outf = open(sys.argv[3], "wb")
    for char in inf.read():
        if len(char) != 1: break
        if char != "=":
            byte = f"{table.find(char):06b}"
            bits =  "".join([bits, f"{byte}"])
        else:
            padding += 1
    if padding != 0:
        bits = bits[:-(padding*2)]
    decoded = []
    i = 0
    while i < len(bits):
        decoded.append(int(bits[i:i+8], 2))
        i += 8
    outf.write(bytes(decoded))
else:
    print(usage)
    sys.exit()
    
inf.close()
outf.close()