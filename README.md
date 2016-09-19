# des-ctr-mapreduce-python
DES encryption in CTR mode using MapReduce

DES encryption is now a deprecated encryption standard but is often used as an example to introduce students to block ciphers. Students also learn the modes of encryption such as ECB, CBC, CTR etc... It is often said that CTR mode is a method of using a block cipher as a stream cipher. Additionally it is said the mode of operation is highly parallelizable, meaning the ciphertexts are independent of one another so separate blocks can be encrypted at the same time without needing to wait for feedback from the previous block. To demonstrate this I have created a MapReduce task to split a plaintext into blocks and encrypt them in CTR mode on any MapReduce clients that connect. This means given a 1TB file as input it would be feasible to connect a dozen or so machines and encrypt it within a few minutes, if not seconds.

##Usage:
To run the traditional DES alforithm in CTR mode execute:
```
python ./des-ctr-mode-traditional.py

It should output the following:
plaintext: AAAABBBBCCCCDDDDAAAABBBBCCCC
key: 12345678
nonce: 0000
plaintext with padding: AAAABBBBCCCCDDDDAAAABBBBCCCC04
ciphertext (base 16 encoded): ['128586D247D57223', '7956BEE384628B55', '4610924B971D9157', 'D5C2B8B530FBB0D4']
plaintext: AAAABBBBCCCCDDDDAAAABBBBCCCC
```
To run the MapReduce DES algorithm in CTR mode execute the following:
```
first execute the server and leave it running: 
 python ./server-mapreduce-des-ctr-mode-example.py
second execute any number of clients:
 python ./mincemeat.py -p changeme localhost 

Then the server should output the following:
ciphertext (base 16 encoded):  {1: ("['128586D247D57223']",), 2: ("['7956BEE384628B55']",), 3: ("['4610924B971D9157']",), 4: ("['D5C2B8B530FBB0D4']",)}

```

The server divides the data into blocks and clients are issued unique blocks of plaintext and a list of counter values. Each client then encrypts a unique plaintext block while paramaterising in each of the counter values. Once all the corresponding ciphertexts are generated the ciphertexts are then loaded into a tuple with their counter value (offset in blocks) and a list of the ciphertext-counter tuples are returned.
