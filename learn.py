import hashlib
import time 

class Block:
    def __init__(self,index,data,prev_hash=""):
        self.index=index
        self.timestamp=time.time()
        self.data=data
        self.prev_hash=prev_hash
        self.nonce=0
        self.hash=self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.prev_hash) + str(self.nonce)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()
    

    def mine_block(self, difficulty):
        target = "0" * difficulty

        while self.hash[:difficulty] != target:
            self.nonce += 1                       
            self.hash = self.calculate_hash()

        print(f"Block {self.index} mined successfully! Hash: {self.hash}")


class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.prev_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                print(f"Data tampered in Block {current_block.index}!")
                return False

            if current_block.prev_hash != prev_block.hash:
                print(f"Chain broken at Block {current_block.index}!")
                return False

        print("Blockchain validity: TRUE")
        return True
if __name__ == "__main__":
    my_blockchain = Blockchain(difficulty=2)

    my_blockchain.add_block(Block(1, "Transaction Data 1"))
    my_blockchain.add_block(Block(2, "Transaction Data 2"))
    my_blockchain.add_block(Block(3, "Transaction Data 3"))

    my_blockchain.validate_chain()

    my_blockchain.chain[1].data = "Tampered Transaction Data"

    my_blockchain.validate_chain()









