from Algorithm import PackageModel


class implementation(PackageModel):
    def __init__(self):
        self.size = 10000
        self.table = [None] * self.size
        for i in range(self.size):
            self.table.append([])

    def insert(self, newEntry):
        print("in insert")
        # hash = hashFunction(key)
        # index = hash % array_size

    def hash(self, key):
        # iterate through the key and select the odd indexed position values
        # then get their numeric ascii codes to do the hash
        hashValue = 0
        for i in range(0, len(key) - 1):
            if (i % 2 != 0):
                hashValue += key[i] - 'A'
            else:
                hashValue
        return hashValue
