from datetime import datetime
from hashlib import sha256
class Tx:

    
    def __init__ (self, date=datetime.now().date(), time=datetime.now().time(), giveBasis="null", giveVal="null", receiveBasis="null", receiveVal="null", other_party_name="null", memo="null"):
        self.date=date
        self.time=time
        self.giveVal=giveVal
        self.receiveVal=receiveVal
        self.giveBasis=giveBasis
        self.receiveBasis=receiveBasis
        self.other_party_name=other_party_name
        self.memo=memo

    def __hash__(self):
        string=""
        string = string + str(self.date)+str(self.time)+ str(self.giveVal)+str(self.receiveVal)
        string = string + str(self.giveBasis)+str(self.receiveBasis)+ str(self.other_party_name)+str(self.memo)
        b = bytes(string, 'utf-8')
        hashed = int(sha256(b).hexdigest(), 16)

        return hashed

    def hasher(self):
        string=""
        string = string + str(self.date)+str(self.time)+ str(self.giveVal)+str(self.receiveVal)
        string = string + str(self.giveBasis)+str(self.receiveBasis)+ str(self.other_party_name)+str(self.memo)
        b = bytes(string, 'utf-8')
        hashed = int(sha256(b).hexdigest(), 16)

        return hashed

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time

    def getGiveBasis(self):
        return self.giveBasis

    def getReceiveBasis(self):
        return self.receiveBasis

    def getGiveVal(self):
        return self.giveVal

    def getReceiveVal(self):
        return self.receiveVal

    def getOther_Party_Name(self):
        return self.other_party_name

    def getmemo(self):
        return self.memo

    def getlistformat(self):
        return [self.date, self.time,self.giveVal,self.receiveVal,
                self.giveBasis, self.receiveBasis, self.other_party_name,
                self.memo]


    
        

