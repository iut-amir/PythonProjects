class Block:
# block is a storage container that stores transactions
    def __init__(self, Height, Blocksize, Blockheader, Txcount, Txs):
        self.Height = Height
        self.Blocksize = Blocksize
        self.Blockheader = Blockheader
        self.Txcount = Txcount
        self.Txs = Txs
