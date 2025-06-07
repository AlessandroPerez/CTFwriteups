'''
I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

C = 73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
'''
c = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
c = bytes.fromhex(c)

key = b"myXORkey"
keyLen = len(key)

p = bytes([b ^ key[i % keyLen] for i, b in enumerate(c)])
print(p.decode())
