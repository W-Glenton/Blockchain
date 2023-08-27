import random
from Block import *
import pickle
import os
from hashlib import sha256
class Blockchain:

    def __init__ (self, POW_difficulty=100000000000000000000000000000000000000000000000000000000000000000000000):
        self.blocks=[]
        self.POW_difficulty=POW_difficulty
        os.environ["PYTHONHASHSEED"]="0"
        

    def hashed(self):
        string=""

        for i in self.blocks:
            string=string+str(i.hasher())
        b = bytes(string, 'utf-8')
        hashed = int(sha256(b).hexdigest(), 16)

        return hashed
        

    def add_block(self, block):
        hashblock=self.blocks[len(self.blocks)-1]
        minhash=self.POW_difficulty
        run = True

        while run:
            integer=str(random.randint(1, 100000000000000000000000000))
            integerbytes = bytes(integer, 'utf-8')
            blockhash=str(hashblock.hasher())
            blockhashbytes = bytes(blockhash, 'utf-8')
            combined=blockhashbytes+integerbytes
            finishedhash=int(sha256(combined).hexdigest(), 16)
            if finishedhash<0:
                finishedhash=finishedhash*-1
            if finishedhash<minhash:
                run=False
                
        block.addkey(int(integer))
        block.addhash(finishedhash)
        block.addminhash(minhash)
        self.blocks.append(block)
        print("Block added. Current Block Height: ", self.get_block_height())
        

    def get_block_height(self):
        return len(self.blocks)

    def save_chain(self, name="null"):
        valid, breaks, hashed=self.validate()
        if valid:
            if name == "null":
                hashed=str(hashed)
                f=open(hashed,"wb")
            else:
                f=open(name,"wb")
            pickle.dump(self,f)
            f.close()
        return valid

    def load_chain(self, name=""):
        f=open(name, "rb")
        chain=pickle.load(f)
        f.close()
        valid, breaks, hashed=chain.validate()
        if valid:
            return chain
        else:
            return False

    def getblock(self, index):
        return self.blocks[index]

    def genesis(self, block):

        if len(self.blocks)==0:
            self.blocks.append(block)
            print("Block added. Current Block Height: ", self.get_block_height())

    def blockchecker(self,blockindex):

        block=self.blocks[blockindex]
        
        if blockindex==0: #genesis block assumed always to be correct
            return True

        integer=str(block.getkey())
        integer = bytes(integer, 'utf-8')
        blockhash=str(self.blocks[blockindex-1].hasher())
        blockhashbytes = bytes(blockhash, 'utf-8')
        combined=blockhashbytes+integer
        finishedhash=int(sha256(combined).hexdigest(), 16)

        if finishedhash<0:
            finishedhash=finishedhash*-1
        if (block.gethash() == finishedhash) and (block.gethash() < block.getminhash()): #if the stored block hash and key are derived from previous block and the stored hash is less than the minimum hash when the block was mined
            return True

        else:
            print(block.gethash(), finishedhash)#
            print(block.gethash()<block.getminhash())#
            
            return False

    def validate(self):
        breaks=[]
        valid = True
        for i in range(len(self.blocks)):
            if i == 0:
                valid = True
            else:
                if not self.blockchecker(i):
                    valid = False
                    breaks.append(i-1)
        return valid, breaks, self.hashed()

    def to_csv(self, name="blockchainCSV.csv"):
        filelist=["Block Number, Date, Time, giveVal, receiveVal, giveBasis, receiveBasis, other_party_name, memo"]
        valid, breaks, hashed=self.validate()
        if valid:
            for i in range(len(self.blocks)):
                for j in self.blocks[i].getTxList():
                    attributeList=j.getlistformat()
                    line=""
                    line=line+str(i)
                    line=line+","
                    for k in attributeList:
                        line=line+str(k)
                        line=line+","
                    filelist.append(line)
            f=open(name,"w")
            for line in filelist:
                f.write(line)
                f.write("\n")
            f.close()

        return valid

    














