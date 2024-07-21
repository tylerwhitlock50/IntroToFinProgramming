"""
Bitcoin with Python and Cryptography

"""

import json
import time
import uuid
import hashlib

class Block:
    def __init__(self, transactions, timestamp, previous_id=None):
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_id = previous_id
        self.block_id = str(uuid.uuid4())
        self.nonce = 0
        self.hash = self.compute_hash()

    def get_block_string(self):
        return json.dumps(self.__dict__, sort_keys=True)
    
    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
class Chain:
    def __init__(self, difficulty=1):
        self.difficulty = difficulty
        self.chain = []
        self.create_genesis_block()
        
    def create_genesis_block(self):
        genesis_block = Block('Genesis Block', time.time(), previous_id='Brink of the bailout of banks')
        self.proof_of_work(genesis_block)
        self.chain.append(genesis_block)
        
    def add_block(self, transactions):
        previous_block = self.get_last_block()
        new_block = Block(transactions, time.time(), previous_id=previous_block.hash)
        self.proof_of_work(new_block)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(block.get_block_string())
    
    def get_last_block(self):
        return self.chain[-1]
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Check if current block's hash is valid
            if current_block.hash != current_block.compute_hash():
                return False, f"Block {i} has invalid hash"
            
            # Check if current block's previous hash matches the previous block's hash
            if current_block.previous_id != previous_block.hash:
                return False, f"Block {i} has invalid previous hash"
        
        return True
    
    def proof_of_work(self, block):
        while not block.hash.startswith('0' * self.difficulty):
            block.nonce += 1
            block.hash = block.compute_hash()

# Create a chain
print('x' * 50)
print('Starting the chain')
chain = Chain(difficulty=2)
chain.add_block('First Block')
chain.add_block('Second Block')
chain.add_block('Third Block')
chain.print_chain()
#print(chain.is_chain_valid())

