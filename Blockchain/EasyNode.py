from Block import *
from Blockchain import *
class EasyNode:

    def __init__ (self):
        self.TxN_list=[]
        self.block_list=[]
        self.chain = Blockchain()

    def add_Tx(self,transaction):
        out=False
        if str(type(transaction))=="<class 'Tx.Tx'>":
            self.TxN_list.append(transaction)
            out=True

        return out

    def fill_blocks(self):
        blocklist=[]
        block=Block()
        for i in self.TxN_list:
            if not block.add_tx(i):
                blocklist.append(block)
                block=Block()
                block.add_tx(i)
        blocklist.append(block)
        self.TxN_list=[]
        for i in blocklist:
            self.block_list.append(i)

    def add_to_chain(self):
        for i in self.block_list:
            self.chain.add_block(i)
        self.block_list=[]

    def check(self):
        valid, breaks, hashed= self.chain.validate()
        return valid

    def startup(self, path = "saves/", name ="tracker.txt"):
        pathname=path+name
        f=open(pathname,"r")
        for i in f:
            pasthash=i
        f.close()
        path=path+pasthash
        self.chain = self.chain.load_chain(path)

    def shutdown(self, path = "saves/", name ="tracker.txt"):
        pathname=path+name
        f=open(pathname,"w")
        f.write(str(self.chain.hashed()))
        f.close()
        pathname=path+str(self.chain.hashed())
        return self.chain.save_chain(pathname)

    def genesis(self):
        tx=Tx(memo="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.")
        block=Block()
        block.add_tx(tx)
        self.chain.genesis(block)

    def size(self):
        return self.chain.get_block_height()

    def save_readable(self, path = "saves/", name = "readable"):
        path=path+name+".csv"
        return self.chain.to_csv()
        

    
        
        
        
        


        

        
