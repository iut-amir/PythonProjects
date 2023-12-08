import sys
sys.path.append("/Users/a.adibzadeh/PycharmProjects/blockchain")

from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import Blockheader
from Blockchain.Backend.util.util import hash256
from Blockchain.Backend.core.database.database import BlockchainDB
from Blockchain.Backend.core.Tx import CoinBasedTx

import time


zero_hash  = '0' * 64
version = 1

class Blockchain:

    def __init__(self):
        self.genesisBlock()

    def write_on_disk(self, block):
        blockchainDB = BlockchainDB()
        blockchainDB.write(block)

    def fetch_last_block(self):
        blockchainDB = BlockchainDB()
        return blockchainDB.lastBlock()

    def genesisBlock(self):
        blockHeight = 1
        prevBlockHash = zero_hash
        self.addBlock(blockHeight, prevBlockHash)

    def addBlock(self, blockHeight, prevBlockHash):

        timestamp = int(time.time())
        coinbasedInstance = CoinBasedTx(blockHeight)
        coinbasedTx = coinbasedInstance.CoinBaseTransaction()

        merkleroot = ''
        bits = 'ffff001f'
        blockheader = Blockheader(version, prevBlockHash, merkleroot, timestamp, bits)
        blockheader.mine()
        self.write_on_disk([Block(blockHeight, 1, blockheader.__dict__, 1, coinbasedTx).__dict__])

    def main(self):
        while True:
            lastBlock = self.fetch_last_block()
            blockHeight = lastBlock['Height'] + 1
            prevBlockHash = lastBlock['Blockheader']['blockHash']
            self.addBlock(blockHeight,  prevBlockHash)


if __name__ == "__main__":

    blockchain = Blockchain()
    blockchain.main()






