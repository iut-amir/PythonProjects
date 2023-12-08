class Script:
    def __init__(self, cmds = None):
        if cmds is None:
            self.cmds = []
        else:
            self.cmds = cmds
    @classmethod
    def p2publickey_script(cls, h160):
    # takes hash160 and returns the pay2publicKey Script
        return Script ([0x76, 0xa9, h160, 0x88, 0xac])



