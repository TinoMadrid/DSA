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
loadTwoDone = False


def formatTime(number):
    return round(number, 2)


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
    global loadTwoDone

    while len(loadedTruck) >= 1:  # last item in list is the truck address

        for i in range(len(loadedTruck)):
            potentialPackage = packageTable.lookup(loadedTruck[i])  # do package lookup
            packageDistance = readInput.address_lookup(truckPosition, potentialPackage.address, addressTable,
                                                       distanceTable)  # retrieve distance
            if packageDistance < findSmallest:  # now check if the package distance is smaller than previous
                findSmallest = packageDistance  # update the min value if it is
                dictionaryForSmallestDistanceInTruck['PackageID'] = potentialPackage.packageID  # then set the dictionary variable
                dictionaryForSmallestDistanceInTruck['PackageDistance'] = packageDistance
                if currTimeForTruckOne >= 10.30 and loadTwoDone == False: # check to see if load two is ready to go
                    if isTruckOne:
                        loadTwoDone = True
                        readInput.truckOneLoadTwo(loadedTruck)

        # after finding the next smallest, go there and update truck address
        package = packageTable.lookup(dictionaryForSmallestDistanceInTruck['PackageID'])  # get package address from packageID

        truckNumber = 1
        if isTruckOne:
            truckNumber = 1
        else:
            truckNumber = 2

        tempTimeStamp = timeWhenPackageIsDelivered(findSmallest, 18, isTruckOne)
        tStamp = convertDecimalToTime(tempTimeStamp, isTruckOne)
        package.timestamp = formatTime(tStamp)

        truckPosition = package.address  # set the truck new address
        loadedTruck.remove(dictionaryForSmallestDistanceInTruck['PackageID'])  # now remove the package from the truck
        findSmallest = 99  # reset the minValue
        totalDistanceTraveled = totalDistanceTraveled + dictionaryForSmallestDistanceInTruck['PackageDistance']  # add distance to total distance traveled
        # print(totalDistanceTraveled)

        print("Press 1 to continue deliveries, 2 for package info, 3 for time, 4 to print truck contents , 5 to quit program")
        selection = int(input())
        if selection == 1:
            continue
        elif selection == 2:
            readInput.printPackageInfo(packageTable)
        elif selection == 3:
            print("Select truck 1 or 2 to see it's current time")
            selectedTruck = int(input())
            if selectedTruck == 1:
                t = formatTime(currTimeForTruckOne)
                print(t)
            elif selectedTruck == 2:
                t = formatTime(currTimeForTruckTwo)
                print(t)
            else:
                print("Invalid truck selection")
        elif selection == 4:
            t1 = 1
            if isTruckOne:
                t1
            else:
                t1 = 2
            print("Note that calls to load trucks are sequential, truck 1 is loaded first then truck 2")
            print("Truck", t1, "contents")
            for i in range(len(loadedTruck)):
                print(loadedTruck[i])
        elif selection == 5:
            exit(0)

        else:
            print("Invalid input")
            continue
    readInput.printPackageInfo(packageTable)


if __name__ == '__main__':
    # need to ask user what time trucks should depart

    # next need to prompt user if they wish to display package data
    print("Welcome to WGU package delivery program! Press 1 to continue or 0 to exit")
    selection = int(input())

    if selection == 1:
        testHash = hashTable()
        loadedTruckOne, loadedTruckTwo, distanceData, addressData, packageData = readInput.read(testHash)
        nearestNeighbor(loadedTruckOne, distanceData, addressData, packageData, True)
        nearestNeighbor(loadedTruckTwo, distanceData, addressData, packageData, False)

