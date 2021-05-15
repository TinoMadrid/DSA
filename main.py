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
    """
    **Nearest neighbor algorithm instructions
    1:Initialize all vertices as unvisited.
    2:Select an arbitrary vertex, set it as the current vertex u. Mark u as visited.
    3:Find out the shortest edge connecting the current vertex u and an unvisited vertex v.
    4:Set v as the current vertex u. Mark v as visited.
    5:If all the vertices in the domain are visited, then terminate. Else, go to step 3.

    Loop through the packages assigned to the truck (since the order was determined by the algorithm above)
        a. For each package, have the truck figure out what the next best address is to go to (shortest distance)
            i. Nearest neighbor algorithm works well for this and will come in under 140 miles.
    """
    visitedVertices = []
    calculatedDistances = []
    totalDistanceTraveled = 0
    selectedPackageID = 0
    i = 0
    # timestamp packages for delivery deadlines (distance/speed for time variable (in control of when truck leaves), add timestamp to package table) can add field to null initialize
    while i < len(loadedTruck):
        for potentialNextDestinationID in loadedTruck:
            if i == len(loadedTruck)-1:

                tempList = calculatedDistances
                tempList.sort()
                secondSmallest = tempList[1]                                            #grabbing second smallest since 0 represents the self address

                nextDestination = calculatedDistances.index(secondSmallest)

                selectedPackageID = loadedTruck[nextDestination]                        # lookup packageID from index of the min value in calculatedDistances list
                calculatedDistances = []                                                # reset the calculated distance values
                totalDistanceTraveled += nextDestination                                # add to total distance traveled
                loadedTruck.remove(selectedPackageID)                                   # remove packageID from truck
                nextAddress = packageTable.lookup(selectedPackageID)
                loadedTruck[-1] = nextAddress.address                                   # update the truck's address
                i = 0                                                                   # reset the iterator to find next closest destination

                break  # break from for loop to start over in while

            currentPosition = loadedTruck[-1]                                           # last item in the truck is the current address
            potentialPackage = packageTable.lookup(potentialNextDestinationID)
            if potentialPackage is not None:
                distance = readInput.address_lookup(currentPosition, potentialPackage.address, addressTable, distanceTable)
                calculatedDistances.append(distance)
            i += 1
    print(calculatedDistances)
    print("Min of calcDist: ", min(calculatedDistances))
    print(totalDistanceTraveled)

    # add truck address starting at hub then update the address as packages are delivered
    # use loop that does min value search for package, when found remember package info


if __name__ == '__main__':
    testHash = hashTable()
    loadedTruckOne, loadedTruckTwo, distanceData, addressData, packageData = readInput.read(testHash)
    nearestNeighbor(loadedTruckOne, distanceData, addressData, packageData)
    # nearestNeighbor(loadedTruckTwo, distanceData, addressData, packageData)
