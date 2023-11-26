import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    return hashlib.sha256(
        f"{index}{previous_hash}{timestamp}{data}".encode()
    ).hexdigest()

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", "0000")

def create_next_block(last_block, data):
    index = last_block.index + 1
    timestamp = time.time()
    hash = calculate_hash(index, last_block.hash, timestamp, data)
    return Block(index, last_block.hash, timestamp, data, hash)

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Adding blocks to the blockchain
for i in range(1, 4):
    new_block = create_next_block(previous_block, f"Block {i}")
    blockchain.append(new_block)
    previous_block = new_block

# Display blockchain
for block in blockchain:
    print(f"Block {block.index}: {block.hash}")
