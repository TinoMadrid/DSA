import readInput
from pathlib import Path

def read():
    file = Path(__file__).parent / "assets/WGUPSDistanceTable.csv"
    readInput.readFile(file)

if __name__ == '__main__':
    read()
