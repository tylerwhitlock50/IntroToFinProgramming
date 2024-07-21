import json
import time
import hashlib

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()


class Chain:
    difficulty = 2

    def __init__(self):
        self.chain = []
        self.unconfirmed_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", time.time(), ["Genesis Block"])
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def is_valid_proof(self, block, block_hash):
        return (block_hash.startswith('0' * Chain.difficulty) and
                block_hash == block.compute_hash())

    def add_block(self, block, proof):
        previous_hash = self.get_last_block().hash

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def proof_of_work(self, block):
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Chain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def record_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        if not self.unconfirmed_transactions:
            return False

        last_block = self.get_last_block()
        new_block = Block(index=last_block.index + 1,
                          previous_hash=last_block.hash,
                          timestamp=time.time(),
                          transactions=['Tyler Whitlock'] + self.unconfirmed_transactions)

        proof = self.proof_of_work(new_block)
        if self.add_block(new_block, proof):
            self.unconfirmed_transactions = []
            return True
        return False

    def save(self, filename='chain.txt'):
        with open(filename, 'w') as file:
            file.write(self.get_chain_str())

    def load(self, filename='chain.txt'):
        with open(filename, 'r') as file:
            chain_data = file.read()
            chain_list = json.loads(chain_data)

            self.chain = [self.create_genesis_block()]  # Reinitialize chain with the genesis block

            for block_data in chain_list[1:]:  # Skipping genesis block
                block = Block(block_data['index'],
                              block_data['previous_hash'],
                              block_data['timestamp'],
                              block_data['transactions'],
                              block_data['nonce'])
                block.hash = block_data['hash']
                self.chain.append(block)

    def get_chain_str(self):
        chain_data = [block.__dict__ for block in self.chain if block is not None]
        return json.dumps(chain_data, indent=4)

    def is_valid_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.previous_hash != previous_block.hash:
                return False

            if not self.is_valid_proof(current_block, current_block.hash):
                return False

        return True

