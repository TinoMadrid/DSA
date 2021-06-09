##############################################################################
##############################################################################
# Florentino Madrid 001228177
# (self, packageID, address, city, state, zip, deliveryDeadline, wgt, specialNotes):
##############################################################################
##############################################################################

from Algorithm.hashImplementation import hashTable
from IO import readInput

currTimeForTruckOne = 8
currTimeForTruckTwo = 9.05


def timeWhenPackageIsDelivered(distance, speed, isTruckOne):
    timeElapsed = distance / speed
    global currTimeForTruckOne
    global currTimeForTruckTwo

    if 0 <= timeElapsed <= 0.25:
        if isTruckOne:
            currTimeForTruckOne = currTimeForTruckOne + 0.15
            return currTimeForTruckOne
        else:
            currTimeForTruckTwo = currTimeForTruckTwo + 0.15
            return currTimeForTruckTwo
    elif 0.26 <= timeElapsed <= 0.5:
        if isTruckOne:
            currTimeForTruckOne = currTimeForTruckOne + 0.3
            return currTimeForTruckOne
        else:
            currTimeForTruckTwo = currTimeForTruckTwo + 0.3
            return currTimeForTruckTwo
    elif 0.51 <= timeElapsed <= 0.75:
        if isTruckOne:
            currTimeForTruckOne = currTimeForTruckOne + 0.45
            return currTimeForTruckOne
        else:
            currTimeForTruckTwo = currTimeForTruckTwo + 0.45
            return currTimeForTruckTwo
    else:
        if isTruckOne:
            currTimeForTruckOne = currTimeForTruckOne + 1
            return currTimeForTruckOne
        else:
            currTimeForTruckTwo = currTimeForTruckTwo + 1
            return currTimeForTruckTwo


def convertDecimalToTime(number, isTruckOne):
    decimals = number % 1
    global currTimeForTruckOne
    global currTimeForTruckTwo
    if decimals > 0.59:
        newTime = number + 1
        if isTruckOne:
            currTimeForTruckOne = newTime - 0.59
            return currTimeForTruckOne
        else:
            currTimeForTruckTwo = newTime - 0.59
            return currTimeForTruckTwo
    if isTruckOne:
        return currTimeForTruckOne
    else:
        return currTimeForTruckTwo


def nearestNeighbor(loadedTruck, distanceTable, addressTable, packageTable, isTruckOne):
    truckPosition = "4001 South 700 East"  # starting position WGU address
    totalDistanceTraveled = 0
    findSmallest = 99
    dictionaryForSmallestDistanceInTruck = {'PackageID': 0, 'PackageDistance': 0}
    global currTimeForTruckOne
    loadTwoDone = False

    while len(loadedTruck) > 1:  # last item in list is the truck address
        for i in range(len(loadedTruck) - 1):
            potentialPackage = packageTable.lookup(loadedTruck[i])  # do package lookup
            packageDistance = readInput.address_lookup(truckPosition, potentialPackage.address, addressTable,
                                                       distanceTable)  # retrieve distance
            if packageDistance < findSmallest:  # now check if the package distance is smaller than previous
                findSmallest = packageDistance  # update the min value if it is
                dictionaryForSmallestDistanceInTruck[
                    'PackageID'] = potentialPackage.packageID  # then set the dictionary variable
                dictionaryForSmallestDistanceInTruck['PackageDistance'] = packageDistance
            if currTimeForTruckOne >= 10.30 and loadTwoDone == False:
                if isTruckOne:
                    loadTwoDone = True
                    readInput.truckOneLoadTwo(loadedTruck)

        # after finding the next smallest, go there and update truck address
        package = packageTable.lookup(
            dictionaryForSmallestDistanceInTruck['PackageID'])  # get package address from packageID

        truckNumber = 1
        if isTruckOne:
            truckNumber = 1
        else:
            truckNumber = 2

        tempTimeStamp = timeWhenPackageIsDelivered(findSmallest, 18, isTruckOne)
        package.timestamp = convertDecimalToTime(tempTimeStamp, isTruckOne)
        print("Package:", package.packageID, "delivered at - %.2f" % package.timestamp, "by truck:", truckNumber)

        truckPosition = package.address  # set the truck new address
        loadedTruck.remove(dictionaryForSmallestDistanceInTruck['PackageID'])  # now remove the package from the truck
        findSmallest = 99  # reset the minValue
        totalDistanceTraveled = totalDistanceTraveled + dictionaryForSmallestDistanceInTruck[
            'PackageDistance']  # add distance to total distance traveled
    # print(totalDistanceTraveled)


if __name__ == '__main__':
    testHash = hashTable()
    loadedTruckOne, loadedTruckTwo, distanceData, addressData, packageData = readInput.read(testHash)
    nearestNeighbor(loadedTruckOne, distanceData, addressData, packageData, True)
    nearestNeighbor(loadedTruckTwo, distanceData, addressData, packageData, False)
