from Algorithm import PackageModel


class implementation(PackageModel):
    def __init__(self):
        self.size = 10000                               # set the initial size of the table
        self.table = [None] * self.size                 # then initialize the table itself
        for i in range(self.size):                      # initialize each cell within the table
            self.table.append([])

    def hashFunction(self, item, tableSize):            #takes the item, gets the integer value and
        return hash(item) % tableSize                   #finds the index of where it ought to be

    def insert(self, item, size):
        index = self.hashFunction(item, size)           #get the index of where the item will be placed
        positionList = self.table[index]                #get the linked list of the index

        keyValue = [index, item]                        #create the new entry
        positionList.append(keyValue)                   #now add it to the end of the list