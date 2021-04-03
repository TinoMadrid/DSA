##############################################################################
##############################################################################
#Florentino Madrid 001228177
#(self, packageID, address, city, state, zip, deliveryDeadline, wgt, specialNotes):
##############################################################################
##############################################################################
from IO import readInput
from Algorithm import implementation
from Algorithm import PackageModel

if __name__ == '__main__':
    #readInput.read()
    #testImplement = implementation(1,"195 W Oakland Ave","Salt Lake City","UT",84115,"###",21, " ")
    count = 0
    testImplement = implementation.implementation()
    count = testImplement.insert("test", count)
    print(testImplement.table)
    print(testImplement.lookup(0))

