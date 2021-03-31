from Algorithm import PackageModel

count = 0  # keeps track of the entries and uses it as key


class implementation(PackageModel.Package):
    def __init__(self):
        self.size = 100                                 #set the initial size of the table
        self.table = []                                 #then initialize the table itself
        for i in range(self.size):                      #initialize each cell within the table
            self.table.append([])                       #add lists to each cell within the table

    def hashFunction(self, item, tableSize):            #takes the item, gets the integer value and
        return hash(item) % tableSize                   #finds the index of where it ought to be

    def insert(self, item, numberOfItems):
        index = self.hashFunction(item, 100)            #get the index of where the item will be placed
        positionList = self.table[index]                #get the list of the index

        keyValue = [numberOfItems, item]                #create the new entry
        numberOfItems += 1                              #add count to the tracker
        positionList.append(keyValue)                   #now add it to the end of the list