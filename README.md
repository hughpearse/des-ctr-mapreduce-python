# des-ctr-mapreduce-python
DES encryption in CTR mode using MapReduce

##Usage:
To run the traditional DES alforithm in CTR mode execute:
```
python ./des-ctr-mode-traditional.py

It should output the following:
key: 12345678
nonce: 0000
plaintext: AAAABBBBCCCC4444
plaintext with padding: AAAABBBBCCCC4444
ciphertext (base 16 encoded): ['128586D247D57223', '7956BEE3F412FB25']
plaintext: AAAABBBBCCCC
```
To run the MapReduce DES algorithm in CTR mode execute the following:
```
first execute the server and leave it running: 
 python ./server-mapreduce-des-ctr-mode-example.py
second execute any number of clients:
 python ./mincemeat.py -p changeme localhost 

Then the server should output the following:
ciphertext (base 16 encoded): ['128586D247D57223', '7956BEE3F412FB25']

```
