import json
import time
import hashlib
from hw import Chain



#THIS HOMEWORK TEST YOUR UNDERSTANDING OF BLOCKCHAIN PROCESSES. TAKE YOU CHAIN CLASS AND MODIFY IT IN THE FOLLOWING MANNER:

# 1.	create function in chain object that will save the chain .txt format (always re-write), you should save getChainStr() data (10 pts)
# 2.	create function in chain object that will load the chain from the file in .txt format, you can skip the genesis block(i.e. use the default generated one) (10 points)
# 3.	now, like in real life, let's split adding transactions and mining (NOTE: AFTER THIS MODIFICATION, YOUR SAVE AND LOAD will hAVE JUST GENESIS BLOCK, UNLESS YOU DO MINE() ): (20 points)
#     a.	modify recordTransaction method to just add the given transaction to the list of unconfirmed transactions(you will need to create that list too)
#     b.	add method called mine()(note no param now) that would:
#         i.	create new block where "transaction" parameter is now a list of transaction. If no transactions -- don't do anything
#         ii.	once you create the block and find nonce (proofed hash) make sure that your new block adheres to the chain requirements(modify isValidChain method), which are:
#         iii.	new block previous hash is equals to the hash of last block on the chain
#         iv.	that new block's hash has the expected difficulty (leading 0s) and that computedHash(from proofOfWork) equals to the hash of the block you are trying to validate.
#         v.	if block adheres to the chain requirements (previous step is True):
#         vi.	Add the new block to the chain
#         vii.	Empty transaction list
#         viii.	First transaction of that new block should be your name (this is your reward for mining :) )



#base code
testChain = Chain()
testChain.record_transaction("First Transaction")
testChain.record_transaction("Second Transaction")
testChain.record_transaction("Third Transaction")

print(testChain.get_chain_str())
#optional after part 3:
#test.chain.mine()

#Testing 1: save the data
testChain.save()
print(testChain.get_chain_str())

#Testing 2: load the data
loadChain = Chain()
loadChain.load()
print(loadChain.get_chain_str())

#Testing 3: Recording and mining transaction
testChain.record_transaction("Fourth Transaction")
testChain.record_transaction("Sixth Transaction")
testChain.mine()
print(testChain.get_chain_str())
testChain.record_transaction("Seventh Transaction")
testChain.mine()
testChain.save('Final Chain.txt')