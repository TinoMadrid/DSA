##############################################################################
##############################################################################
# Florentino Madrid 001228177
# (self, packageID, address, city, state, zip, deliveryDeadline, wgt, specialNotes):
##############################################################################
##############################################################################

from Algorithm.hashImplementation import hashTable
from IO import readInput

currTime = 8
def timeWhenPackageIsDelivered(distance, speed):
    timeElapsed = distance / speed
    global currTime
    if 0 <= timeElapsed <= 0.25:
        currTime = currTime + 0.15
        return currTime
    elif 0.26 <= timeElapsed <= 0.5:
        currTime = currTime + 0.3
        return currTime
    elif 0.51 <= timeElapsed <= 0.75:
        currTime = currTime + 0.45
        return currTime
    else:
        currTime = currTime + 1
        return currTime


def convertDecimalToTime(number):
    decimals = number % 1
    global currTime
    if decimals > 0.59:
        newTime = number + 1
        currTime = newTime - 0.59
        return currTime
    return currTime


def nearestNeighbor(loadedTruck, distanceTable, addressTable, packageTable):
    truckPosition = "4001 South 700 East"  # starting position WGU address
    totalDistanceTraveled = 0
    findSmallest = 99
    dictionaryForSmallestDistanceInTruck = {'PackageID': 0, 'PackageDistance': 0}
    # default time to 8AM (truck1 not truck2)
    # truck2 departs 9:05 truck3 10

    while len(loadedTruck) > 1:                                     #last item in list is the truck address
        for i in range(len(loadedTruck)-1):
            potentialPackage = packageTable.lookup(loadedTruck[i])  #do package lookup
            packageDistance = readInput.address_lookup(truckPosition, potentialPackage.address, addressTable, distanceTable) # retrieve distance
            if packageDistance < findSmallest:                      #now check if the package distance is smaller than previous
                findSmallest = packageDistance                      #update the min value if it is
                dictionaryForSmallestDistanceInTruck['PackageID'] = potentialPackage.packageID  # then set the dictionary variable
                dictionaryForSmallestDistanceInTruck['PackageDistance'] = packageDistance
        # after finding the next smallest, go there and update truck address
        package = packageTable.lookup(dictionaryForSmallestDistanceInTruck['PackageID'])    # get package address from packageID

        # add function to calculate time with distance of package divided by speed of 18 mph
        # pseudotime findsmallest/18mph yields amt of time in hrs, currTime = currTime+ pseudoElapseTime
        # function to convert decimal num to timestamp user understands then store in package details
        tempTimeStamp = timeWhenPackageIsDelivered(findSmallest, 18)
        package.timestamp = convertDecimalToTime(tempTimeStamp)
        print(package.timestamp)

        # package.timestamp = time.ctime()                                                      # timestamp package so it is delivered
        truckPosition = package.address                                                           # set the truck new address
        loadedTruck.remove(dictionaryForSmallestDistanceInTruck['PackageID'])                      # now remove the package from the truck
        findSmallest = 99                                                                           # reset the minValue
        totalDistanceTraveled = totalDistanceTraveled + dictionaryForSmallestDistanceInTruck['PackageDistance']    #add distance to total distance traveled
        # print(package.timestamp)

    #print(totalDistanceTraveled)


if __name__ == '__main__':
    testHash = hashTable()
    loadedTruckOne, loadedTruckTwo, distanceData, addressData, packageData = readInput.read(testHash)
    nearestNeighbor(loadedTruckOne, distanceData, addressData, packageData)
    nearestNeighbor(loadedTruckTwo, distanceData, addressData, packageData)
