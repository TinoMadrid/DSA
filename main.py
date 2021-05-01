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
    i = 0
    #timestamp packages for delivery deadlines (distance/speed for time variable (in control of when truck leaves), add timestamp to package table) can add field to null initialize
    while(i < len(loadedTruck)):
        for potentialNextDestinationID in loadedTruck:
            if(i == len(loadedTruck)):
                break
            currentPosition = loadedTruck[-1] #last item in the truck is the current address
            potentialPackage = packageTable.lookup(potentialNextDestinationID)
            if potentialPackage is not None:
                distance = readInput.address_lookup(currentPosition, potentialPackage.address, addressTable, distanceTable)
                calculatedDistances.append(distance)
            i+=1
    #calculatedDistances = [x for x in calculatedDistances if x != 0]
    print(calculatedDistances)
    print(len(calculatedDistances))
    print(len(loadedTruck))
            #calculatedDistances.append(euclideanDistance(packageTable.lookup(selectedPackageID), packageTable.lookup(potentialNextDestinationID)))
            #add truck address starting at hub then update the address as packages are delivered
            #use loop that does min value search for package, when found remember package info


if __name__ == '__main__':
    testHash = hashTable()
    loadedTruckOne, loadedTruckTwo, distanceData, addressData, packageData = readInput.read(testHash)
    nearestNeighbor(loadedTruckOne, distanceData, addressData, packageData)
    #nearestNeighbor(loadedTruckTwo, distanceData, addressData, packageData)