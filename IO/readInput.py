from pathlib import Path


def readFile(f, dataVar):
    for line in open(f):
        dataVar += line
    return dataVar

def read():
    file = Path(__file__).parent / "../assets/WGUPSDistanceTable.csv"
    temp = " "
    unfilteredGraphData = readFile(file, temp)
    print(unfilteredGraphData)