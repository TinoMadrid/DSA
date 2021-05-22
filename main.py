##############################################################################
##############################################################################
# Florentino Madrid 001228177
# (self, packageID, address, city, state, zip, deliveryDeadline, wgt, specialNotes):
##############################################################################
##############################################################################
import math
from Algorithm.hashImplementation import hashTable
from IO import readInput


def euclideanDistance(x, y):
    measuredDistance = 0.0
    for i in range(len(x) - 1):
        measuredDistance += pow((float(x[i]) - float(y[i])), 2)
        measuredDistance = math.sqrt(measuredDistance)
    return measuredDistance


def nearestNeighbor(loadedTruck, distanceTable, addressTable, packageTable):
    truckPosition = "4001 South 700 East"  # starting position WGU address
    totalDistanceTraveled = 0
    findSmallest = 99
    dictionaryForSmallestDistanceInTruck = {'PackageID': 0, 'PackageDistance': 0}

    while len(loadedTruck) > 1:                                     #last item in list is the truck address
        for i in range(len(loadedTruck)-1):
            potentialPackage = packageTable.lookup(loadedTruck[i])  #do package lookup
            packageDistance = readInput.address_lookup(truckPosition, potentialPackage.address, addressTable, distanceTable) # retrieve distance
            if packageDistance < findSmallest:                      #now check if the package distance is smaller than previous
                findSmallest = packageDistance                      #update the min value
                dictionaryForSmallestDistanceInTruck['PackageID'] = potentialPackage.packageID  # if it is, set the dictionary variable
                dictionaryForSmallestDistanceInTruck['PackageDistance'] = packageDistance
        # after finding the next smallest, go there and update truck address
        package = packageTable.lookup(dictionaryForSmallestDistanceInTruck['PackageID'])    # get package address from packageID
        truckPosition = package.address                                                           # set the truck new address
        loadedTruck.remove(dictionaryForSmallestDistanceInTruck['PackageID'])                      # now remove the package from the truck
        findSmallest = 99                                                                           # reset the minValue
        totalDistanceTraveled = totalDistanceTraveled + dictionaryForSmallestDistanceInTruck['PackageDistance']    #add distance to total distance traveled
        #####################################
        #####################################
        #####################################
        #####################################
        # Leaving off of here to compare indices with addresses for distance lookups on second iteration to find the next smallest distance package
        #####################################
        #####################################
        #####################################
        #####################################
    print(totalDistanceTraveled)
if __name__ == '__main__':
    testHash = hashTable()
    loadedTruckOne, loadedTruckTwo, distanceData, addressData, packageData = readInput.read(testHash)
    nearestNeighbor(loadedTruckOne, distanceData, addressData, packageData)
    nearestNeighbor(loadedTruckTwo, distanceData, addressData, packageData)
