from EasyNode import *
from Tx import *

# EasyNode demo

"""
Easynode makes running a blockchain easy and intuitive. Using EasyNode,
you should only need to know how to use EasyNode and the Tx class.
"""

# starting up a new chain

node=EasyNode() #starts a blockchain instance 
node.genesis()  #adds the genesis block


# adding transactions
newTx=Tx(memo=random.randint(1,1000000)) #create a transaction

node.add_Tx(newTx) #adds transaction to the node's holding list
#it has not yet been added to a block or to the chain

##############################################################
#Disregard this, just adding some more randomised transactions
for i in range(99):
    newTx=Tx(memo=random.randint(1,1000000))#create transaction
    node.add_Tx(newTx)
##############################################################

# There are now 100 transactions in the holding list
# They have not yet been added to blocks

# To add held transactions to blocks:
node.fill_blocks()


# This next part can be slow
# We need to add the blocks to the chain
node.add_to_chain()
# This will now mine the blocks, adding them to the chain
# using a proof of work algorithm similar to that of bitcoin.

#To check how many blocks are in the chain:

print(node.size())

# Let's check the chain is valid

print(node.check())

# We want to use the chain another time, this is how to save it
# at the end of your session:

node.shutdown()
# Now, if we want, we can stop python and go outside like a normal person

# Loading a saved chain

newnode=EasyNode()
newnode.startup()
# easy!

# Let's check the loaded chain to make sure it is still valid

print(newnode.check())

# Now, perhaps we want an easily readable record of the contents of the chain
newnode.save_readable()
#That's all it takes

print("done")

