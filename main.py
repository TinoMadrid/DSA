##############################################################################
##############################################################################
#Florentino Madrid 001228177
#(self, packageID, address, city, state, zip, deliveryDeadline, wgt, specialNotes):
##############################################################################
##############################################################################
from IO import readInput
from Algorithm import implementation

if __name__ == '__main__':
    count = 0
    testImplement = implementation.implementation()
    readInput.read(testImplement)

    print(testImplement.table)
    print(testImplement.lookup(0))