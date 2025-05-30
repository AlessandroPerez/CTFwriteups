'''
I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

C = 73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
'''
def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

c = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

stringC = bytes.fromhex(c)
i = 0

for key in range(256):
    extendKey = bytes([key]*len(stringC))
    
    flagEncoded = xor(stringC, extendKey)

    try:
        flag = flagEncoded.decode()
        if "crypto" in flag:
            print(flag)
    except UnicodeDecodeError:
        continue
