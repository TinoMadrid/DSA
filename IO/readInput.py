from pathlib import Path
from Algorithm.PackageModel import Package
import csv

def readFile(f, dataVar):
    count = 0
    for line in open(f):
        newPck = Package(count, "195 W Oakland Ave", "Salt Lake City", "UT", 84115, "###", 21, " ")
        dataVar += line
    return dataVar
# Read a row from the package csv file and create a Package object with it
# Add the package object to the hash table using the insert() function.

def read():
    #file = Path(__file__).parent / "../assets/WGUPSDistanceTable.csv"
    file = Path(__file__).parent / "../assets/WGUPSPackageFile.csv"
    temp = " "
    unfilteredGraphData = readFile(file, temp)
    print(unfilteredGraphData)