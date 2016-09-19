#!/bin/python

import base64
from Crypto.Cipher import DES
from Crypto import Random
from Crypto.Util import Counter

def addPadding(data):
        length = 16 - (len(data) % 16)
        data += bytes(length)*length
        return data

def removePadding(data):
        return data[:-int(data[-1])]

key = "12345678"

'''The Counter feedback mode requires a sequence of input blocks,
called counters, that are used to produce the output.  When 'mode'
is MODE_CTR, the 'counter' keyword argument must be provided, and
its value must be a callable object, such as a function or method.
Successive calls to this callable object must return a sequence of
strings that are of the length 'block_size' and that never
repeats. '''

#nonce = Random.new().read(DES.block_size/2)
nonce = "0000"
ctr = Counter.new(DES.block_size*8/2, prefix=nonce)
des = DES.new(key, DES.MODE_CTR, counter=ctr)

ctr2 = Counter.new(DES.block_size*8/2, prefix=nonce)
des2 = DES.new(key, DES.MODE_CTR, counter=ctr2)


plain_text = 'AAAABBBBCCCCDDDDAAAABBBBCCCC'
print "plaintext: " + plain_text
plain_text = addPadding(plain_text)

cipher_text = des.encrypt(plain_text)

print "key: " + key
print "nonce: " + nonce
print "plaintext with padding: " + plain_text
print "ciphertext (base 16 encoded): " + str(map(''.join, zip(*[iter(base64.b16encode(cipher_text))]*16)))
print "plaintext: " + removePadding(des2.decrypt(cipher_text))

