# des-ctr-mapreduce-python
DES encryption in CTR mode using MapReduce

DES encryption is now a deprecated encryption standard but is often used as an example to introduce students to block ciphers. Students also learn the modes of encryption such as ECB, CBC, CTR etc... It is often said that CTR mode is a method of using a block cipher as a stream cipher. Additionally it is said the mode of operation is highly parallelizable, meaning the ciphertexts are independent of one another so separate blocks can be encrypted at the same time without needing to wait for feedback from the previous block. To demonstrate this I have created a MapReduce task to split a plaintext into blocks and encrypt them in CTR mode on any MapReduce clients that connect. This means given a 1TB file as input it would be feasible to connect a dozen or so machines and encrypt it within a few minutes, if not seconds.

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
