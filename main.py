##############################################################################
##############################################################################
#Florentino Madrid 001228177
#(self, packageID, address, city, state, zip, deliveryDeadline, wgt, specialNotes):
##############################################################################
##############################################################################
from IO import readInput
from Algorithm import hashTable

if __name__ == '__main__':
    testImplement = hashTable.implementation()
    readInput.read(testImplement)

    print(testImplement.table)
    print(testImplement.lookup(0))