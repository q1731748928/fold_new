from Crypto.Cipher import AES
import base64
import json

# 如果text不足16位的倍数就用空格补足为16位
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


 # 加密
def encrypt(text):
    key = '9999999999999999'.encode('utf-8')
    mode = AES.MODE_CBC
    iv = b'qqqqqqqqqqqqqqqq'
    text = add_to_16(text)
    cryptos = AES.new(key, mode, iv)
    cipher_text = cryptos.encrypt(text)
    return base64.b64encode(cipher_text)


 # 解密后，去掉补足的空格用strip() 去掉
def decrypt():
    key = 'JhbGciOiJIUzI1Ni'.encode('utf8')
    # print(key)
    text = base64.b64decode(
        "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"
    )
    # print(text)
    iv = b"JhbGciOiJIUzI1Ni"
    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, iv)

    plain_text = cryptos.decrypt(text)
    #print(plain_text)
    print(plain_text.decode('unicode_escape'))

decrypt()
