'''
I've encrypted the flag with my secret key, you'll never be able to guess it.

C = 0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
'''

c = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
c = bytes.fromhex(c)

key = b"myXORkey"
key_len = len(key)

plaintext = bytes([b ^ key[i % key_len] for i, b in enumerate(cipher_bytes)])
print(plaintext.decode())
