
from Blockchain.Backend.util.util import hash256

class Blockheader:

    def __init__(self, version, pervBlockhash, merkleroot, timestamp, bits):
        self.version = version
        self.pervBlockhash = pervBlockhash
        self.merkleroot = merkleroot
        self.timestamp = timestamp
        self.bits = bits
        self.nonce = 0
        self.blockHash = ""

    def mine(self):
        while self.blockHash[0:4] != "0000":

            self.blockHash = hash256((str(self.version) + self.pervBlockhash + self.merkleroot +  str(self.timestamp) +
                                     self.bits + str(self.nonce)).encode()).hex()

            self.nonce += 1

            print(f'Mining started {self.nonce}', end = "\r")
        return self.blockHash


