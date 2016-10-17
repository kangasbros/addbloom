import xxhash

class AddBloomFilter(object):
    """docstring for AddBloomFIlter"""

    def __init__(self, max_size_exponent=20, hash_functions=3):
        super(AddBloomFilter, self).__init__()
        self.data = bytearray(2^^max_size_exponent)

