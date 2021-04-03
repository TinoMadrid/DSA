from Algorithm import PackageModel

count = 0  # keeps track of the entries and uses it as key


class implementation(PackageModel.Package):
    def __init__(self):
        self.size = 100                                 #set the initial size of the table
        self.table = []                                 #then initialize the table itself
        for i in range(self.size):                      #initialize each cell within the table
            self.table.append([])                       #add lists to each cell within the table

    def hashFunction(self, count, tableSize):           #takes the item, gets the integer value and
        return hash(count) % tableSize                  #finds the index of where it ought to be

    def insert(self, numberOfItems, item):
        index = self.hashFunction(count, 100)           #get the index of where the item will be placed
        positionList = self.table[index]                #get the list of the index

        isItemInList = self.update(item)
        if(isItemInList == False):
            keyValue = [numberOfItems, item]            #create the new entry
            positionList.append(keyValue)               #now add it to the end of the list

    def update(self, item):
        found = False
        index = self.hashFunction(item, 100)            #find the location in the list of lists
        positionList = self.table[index]                #obtain the list in the given index

        i = 0
        while i < len(positionList)-1:                  #iterate thru the list if items exist
            if(positionList[i] == item):
                self.table[i+1] = item                  #overwrite the old entry
                found = True
        return found

    def lookup(self, key):
        index = self.hashFunction(key, 100)             #grab the hash value for the index
        positionList = self.table[index]                #then retrieve the list at that index

        for i in positionList:
            if(i[0] == key):
                return i[1]
        return None                                     #otherwise return null