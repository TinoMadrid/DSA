##############################################################################
##############################################################################
#Florentino Madrid 001228177
#(self, packageID, address, city, state, zip, deliveryDeadline, wgt, specialNotes):
##############################################################################
##############################################################################
from Algorithm.PackageModel import Package
from IO import readInput
from Algorithm import implementation
from Algorithm import PackageModel

if __name__ == '__main__':
    count = 0
    readInput.read()
    #newPck = Package(count, "195 W Oakland Ave","Salt Lake City","UT",84115,"###",21, " ")
    #count += 1

    testImplement = implementation.implementation()
    #testImplement.insert(newPck.packageID, newPck)
    print(testImplement.table)
    print(testImplement.lookup(0))