#!/usr/bin/env python
import mincemeat
import base64

def addPadding(data):
        length = 16 - (len(data) % 16)
        data += "\x00"*(length-2)
        data += str(length).zfill(2)
        return data

def removePadding(data):
        return data[:-int(data[-2:])]

def chunks(longdata, n):
    """Yield successive n-sized chunks from longdata."""
    for i in range(0, len(longdata), n):
        yield longdata[i:i + n]

plain_text = 'AAAABBBBCCCCDDDDAAAABBBBCCCC'
plain_text = addPadding(plain_text)
datasource = dict(enumerate(list(chunks(plain_text, 8)), start=1))

def mapfn(k, v):
    yield v, k

def reducefn(k, vs):
    from Crypto.Cipher import DES
    from Crypto import Random
    from Crypto.Util import Counter
    import struct
    result = {}
    key = "12345678"
    #nonce = Random.new().read(DES.block_size/2)
    #ctr = Counter.new(DES.block_size*8/2, prefix=nonce)
    nonce = "0000"
    for offsetval in vs:
        ctr = nonce + struct.pack("!I",offsetval)
        def getctr():
            return str(ctr)
        des = DES.new(key, DES.MODE_CTR, counter=getctr)
        cipher_text = des.encrypt(k)
        result[offsetval] = cipher_text
    #print "k: " + k + ", vs: " + str(vs) + ", ctr: " + ctr + "cipher_text: " + cipher_text
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
#print results

print "ciphertext (base 16 encoded): " ,
sorted_results = {}
for kp,vp in results.iteritems():
    for kc,vc in vp.iteritems():
        sorted_results[kc] = str(map(''.join, zip(*[iter(base64.b16encode(vc))]*16))),
print sorted_results
