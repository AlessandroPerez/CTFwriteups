'''
A  = KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
B = KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
C = KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
D = FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf 

FLAG = D xor C xor A
'''

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


A = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
B = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
C = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
D = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

stringA = bytes.fromhex(A)
stringC = bytes.fromhex(C)
stringD = bytes.fromhex(D)

flag = xor(xor(stringD, stringC), stringA)

print(flag.decode())
