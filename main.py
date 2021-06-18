##############################################################################
##############################################################################
# Florentino Madrid 001228177
# (self, packageID, address, city, state, zip, deliveryDeadline, wgt, specialNotes):
##############################################################################
##############################################################################

from Algorithm.hashImplementation import hashTable
from IO import readInput

currTimeForTruckOne = 8.10
currTimeForTruckTwo = 9.05
loadTwoDone = False
allMileage = 0


# This function formatTime is to set the time variable to only 2 decimals to the right since time is stored as an int
def formatTime(number):
    return round(number, 2)


# this calculates the time that has elapsed when driving to another destination
# this is O(1) since there isn't any significant overhead
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


# since time is kept in a decimal format, this function ensures to keep it within time constraints
# this function is also in constant time of O(1)
def convertDecimalToTime(number, isTruckOne):
    decimals = number % 1
    global currTimeForTruckOne
    global currTimeForTruckTwo
    if decimals > 0.59:
        newTime = number + 1
        if isTruckOne:
            currTimeForTruckOne = newTime - 0.59
            formatTime(currTimeForTruckOne)
            return currTimeForTruckOne
        else:
            currTimeForTruckTwo = newTime - 0.59
            formatTime(currTimeForTruckOne)
            return currTimeForTruckTwo
    if isTruckOne:
        formatTime(currTimeForTruckTwo)
        return currTimeForTruckOne
    else:
        formatTime(currTimeForTruckTwo)
        return currTimeForTruckTwo


def interface(packageTable, isTruckOne, loadedTruck, totalDistanceTraveled):
    t1 = 1
    if isTruckOne:
        t1
    else:
        t1 = 2
    print("Press 1 to continue deliveries, 2 for package info, 3 for time, 4 to print truck contents , 5 to quit program, 6 to show mileage traveled so far")
    choice = int(input())
    if choice == 1:
        None
    elif choice == 2:
        readInput.printPackageInfo(packageTable)
    elif choice == 3:
        print("Select truck 1 or 2 to see it's current time")
        selectedTruck = int(input())
        if selectedTruck == 1:
            t = formatTime(currTimeForTruckOne)
            print("%.2f" % t)
        elif selectedTruck == 2:
            t = formatTime(currTimeForTruckTwo)
            print("%.2f" % t)
        else:
            print("Invalid truck selection")
    elif choice == 4:
        if isTruckOne:
            t1
        else:
            t1 = 2
        print("Note that calls to load trucks are sequential, truck 1 is loaded first then truck 2")
        print("Truck", t1, "contents")
        for i in range(len(loadedTruck)):
            print(loadedTruck[i])
    elif choice == 5:
        exit(0)
    elif choice == 6:
        print("Truck ", t1, "has traveled", totalDistanceTraveled)
    else:
        print("Invalid input")


# this function is the core algorithm used to determine shortest path from the truck's current position to the next package.
# Since there are 2 loops within here the worst case for time complexity is O(n^2)
# Space complexity here is O(n), this function is used with 1 truck at a time.
# This also applies to both the distance, address, and package information since these grow linearly with the size of the input data
def nearestNeighbor(loadedTruck, distanceTable, addressTable, packageTable, isTruckOne):
    truckPosition = "4001 South 700 East"  # starting position WGU address
    totalDistanceTraveled = 0
    findSmallest = 99
    dictionaryForSmallestDistanceInTruck = {'PackageID': 0, 'PackageDistance': 0}
    global currTimeForTruckOne
    global loadTwoDone
    global allMileage

    interface(packageTable, isTruckOne, loadedTruck, totalDistanceTraveled)

    while len(loadedTruck) >= 1:  # last item in list is the truck address

        for i in range(len(loadedTruck)):
            potentialPackage = packageTable.lookup(loadedTruck[i])  # do package lookup
            packageDistance = readInput.address_lookup(truckPosition, potentialPackage.address, addressTable,
                                                       distanceTable)  # retrieve distance
            potentialPackage.isLoaded = True
            if packageDistance < findSmallest:  # now check if the package distance is smaller than previous
                findSmallest = packageDistance  # update the min value if it is
                dictionaryForSmallestDistanceInTruck[
                    'PackageID'] = potentialPackage.packageID  # then set the dictionary variable
                dictionaryForSmallestDistanceInTruck['PackageDistance'] = packageDistance
                if currTimeForTruckOne >= 10.30 and loadTwoDone == False:  # check to see if load two is ready to go
                    if isTruckOne:
                        loadTwoDone = True
                        readInput.truckOneLoadTwo(loadedTruck)
        interface(packageTable, isTruckOne, loadedTruck, totalDistanceTraveled)

        # after finding the next smallest, go there and update truck address
        package = packageTable.lookup(
            dictionaryForSmallestDistanceInTruck['PackageID'])  # get package address from packageID

        tempTimeStamp = timeWhenPackageIsDelivered(findSmallest, 18, isTruckOne)
        tStamp = convertDecimalToTime(tempTimeStamp, isTruckOne)
        package.timestamp = formatTime(tStamp)

        truckPosition = package.address  # set the truck new address
        loadedTruck.remove(dictionaryForSmallestDistanceInTruck['PackageID'])  # now remove the package from the truck
        findSmallest = 99  # reset the minValue
        totalDistanceTraveled = totalDistanceTraveled + dictionaryForSmallestDistanceInTruck[
            'PackageDistance']  # add distance to total distance traveled
        if loadedTruck == 1:
            allMileage = allMileage + totalDistanceTraveled

    allMileage = allMileage + totalDistanceTraveled


if __name__ == '__main__':
    print("Welcome to WGU package delivery program! Press 1 to continue or 0 to exit")
    selection = int(input())

    if selection == 1:
        testHash = hashTable()
        loadedTruckOne, loadedTruckTwo, distanceData, addressData, packageData = readInput.read(testHash)
        nearestNeighbor(loadedTruckOne, distanceData, addressData, packageData, True)
        nearestNeighbor(loadedTruckTwo, distanceData, addressData, packageData, False)
        print("Total distance traveled", allMileage)
        readInput.printPackageInfo(packageData)