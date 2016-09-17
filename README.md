# des-ctr-mapreduce-python
DES encryption in CTR mode using MapReduce

##Usage:
To run the traditional DES alforithm in CTR mode execute:
```
python ./des-ctr-mode-traditional.py
```

To run the MapReduce DES algorithm in CTR mode execute the following:
```
first execute the server and leave it running: 
 python ./server-mapreduce-des-ctr-mode-example.py
second execute any number of clients:
 python ./mincemeat.py -p changeme localhost 
```
