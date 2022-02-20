from Tx import *
from hashlib import sha256
class Block:

    def __init__ (self, block_size=5):
        self.Tx_list=[]
        self.block_size=block_size
        self.validator_key=-1
        self.validator_hash=-1
        self.minhash=-1


    def hasher(self):

        string=""
        for i in self.Tx_list:
            string=string + str(i.hasher())
        
        string=string+ str(self.block_size)
        string=string+ str(self.validator_key)
        string=string+ str(self.validator_hash)
        string=string+ str(self.minhash)
        b = bytes(string, 'utf-8')
        hashed = int(sha256(b).hexdigest(), 16)

        return hashed
        


    def add_tx(self, Tx):
        out=False
        if len(self.Tx_list)< self.block_size:
            self.Tx_list.append(Tx)
            out=True
        return out

    def addkey(self, key):
        self.validator_key=key

    def getkey(self):
        return self.validator_key

    def gethash(self):
        return self.validator_hash
    def getminhash(self):
        return self.minhash

    def addhash(self, hashed):
        self.validator_hash=hashed

    def addminhash(self, minhash):
        self.minhash=minhash

    def getTxList(self):
        return self.Tx_list
