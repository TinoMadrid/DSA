import csv
from pathlib import Path
from Algorithm.PackageModel import Package


def readFile(dataVar, table):

    newPck1 = Package(1, "195 W Oakland Ave", "Salt Lake City","UT",84115,"###",21,None)
    newPck2 = Package(2, "2530 S 500 E", "Salt Lake City","UT",84106,"EOD",44,None)
    newPck3 = Package(3, "233 Canyon Rd", "Salt Lake City","UT",84103,"EOD",2,"Can only be on truck 2")
    newPck4 = Package(4, "380 W 2880 S", "Salt Lake City","UT",84115,"EOD",4,None)
    newPck5 = Package(5, "410 S State St", "Salt Lake City","UT",84111,"EOD",5,None)
    newPck6 = Package(6, "3060 Lester St", "West Valley City","UT",84119,"###",88,"Delayed on flight---will not arrive to depot until 9:05 am")
    newPck7 = Package(7, "1330 2100 S", "Salt Lake City","UT",84106,"EOD",8,None)
    newPck8 = Package(8, "300 State St", "Salt Lake City","UT",84103,"EOD",9,None)
    newPck9 = Package(9, "300 State St", "Salt Lake City","UT",84103,"EOD",2,"Wrong address listed")
    newPck10 = Package(10, "600 E 900 South", "Salt Lake City","UT",84105,"EOD",1,None)

    newPck11 = Package(11,"2600 Taylorsville Blvd","Salt Lake City","UT",84118,"EOD",1,None)
    newPck12 = Package(12,"3575 W Valley Central Station bus Loop","West Valley City","UT",84119,"EOD",1,None)
    newPck13 = Package(13,"2010 W 500 S","Salt Lake City","UT",84104,"###",2,None)
    newPck14 = Package(14,"4300 S 1300 E","Millcreek","UT",84117,"###",88, "Must be delivered with 15 and 19")
    newPck15 = Package(15,"4580 S 2300 E","Holladay","UT",84117,"9:00 AM",4,None)
    newPck16 = Package(16,"4580 S 2300 E","Holladay","UT",84117,"10:30 AM",88,"Must be delivered with 13 and 19")
    newPck17 = Package(17,"3148 S 1100 W","Salt Lake City","UT",84119,"EOD",2,None)
    newPck18 = Package(18,"1488 4800 S","Salt Lake City","UT",84123,"EOD",6,"Can only be on truck 2")
    newPck19 = Package(19,"177 W Price Ave","Salt Lake City","UT",84115,"EOD",37,None)
    newPck20 = Package(20,"3595 Main St","Salt Lake City","UT",84115,"###",37,"Must be delivered with 13 and 15")

    newPck21 = Package(21,"3595 Main St","Salt Lake City","UT",84115,"EOD",3,None)
    newPck22 = Package(22,"6351 South 900 East","Murray","UT",84121,"EOD",2,None)
    newPck23 = Package(23,"5100 South 2700 West","Salt Lake City","UT",84118,"EOD",5,None)
    newPck24 = Package(24,"5025 State St","Murray","UT",84107,"EOD",7,None)
    newPck25 = Package(25,"5383 South 900 East #104","Salt Lake City","UT",84117,"###",7,"Delayed on flight---will not arrive to depot until 9:05 am")
    newPck26 = Package(26,"5383 South 900 East #104","Salt Lake City","UT",84117,"EOD",25,None)
    newPck27 = Package(27,"1060 Dalton Ave S","Salt Lake City","UT",84104,"EOD",5,None)
    newPck28 = Package(28,"2835 Main St","Salt Lake City","UT",84115,"EOD",7,"Delayed on flight---will not arrive to depot until 9:05 am")
    newPck29 = Package(29,"1330 2100 S","Salt Lake City","UT",84106,"###",2,None)
    newPck30 = Package(30,"300 State St","Salt Lake City","UT",84103,"###",1,None)

    newPck31 = Package(31,"3365 S 900 W","Salt Lake City","UT",84119,"###",1,None)
    newPck32 = Package(32,"3365 S 900 W","Salt Lake City","UT",84119,"EOD",1,"Delayed on flight---will not arrive to depot until 9:05 am")
    newPck33 = Package(33,"2530 S 500 E","Salt Lake City","UT",84106,"EOD",1,None)
    newPck34 = Package(34,"4580 S 2300 E","Holladay","UT",84117,"###",2,None)
    newPck35 = Package(35,"1060 Dalton Ave S","Salt Lake City","UT",84104,"EOD",88,None)
    newPck36 = Package(36,"2300 Parkway Blvd","West Valley City","UT",84119,"EOD",88,"Can only be on truck 2")
    newPck37 = Package(37,"410 S State St","Salt Lake City","UT",84111,"###",2,None)
    newPck38 = Package(38,"410 S State St","Salt Lake City","UT",84111,"EOD",9,"Can only be on truck 2")
    newPck39 = Package(39,"2010 W 500 S","Salt Lake City","UT",84104,"EOD",9,None)
    newPck40 = Package(40,"380 W 2880 S","Salt Lake City","UT",84115,"10:30 AM",45,None)

    table.insert(newPck1.packageID, newPck1)
    table.insert(newPck2.packageID, newPck2)
    table.insert(newPck3.packageID, newPck3)
    table.insert(newPck4.packageID, newPck4)
    table.insert(newPck5.packageID, newPck5)
    table.insert(newPck6.packageID, newPck6)
    table.insert(newPck7.packageID, newPck7)
    table.insert(newPck8.packageID, newPck8)
    table.insert(newPck9.packageID, newPck9)
    table.insert(newPck10.packageID, newPck10)

    table.insert(newPck11.packageID, newPck11)
    table.insert(newPck12.packageID, newPck12)
    table.insert(newPck13.packageID, newPck13)
    table.insert(newPck14.packageID, newPck14)
    table.insert(newPck15.packageID, newPck15)
    table.insert(newPck16.packageID, newPck16)
    table.insert(newPck17.packageID, newPck17)
    table.insert(newPck18.packageID, newPck18)
    table.insert(newPck19.packageID, newPck19)
    table.insert(newPck20.packageID, newPck20)

    table.insert(newPck21.packageID, newPck21)
    table.insert(newPck22.packageID, newPck22)
    table.insert(newPck23.packageID, newPck23)
    table.insert(newPck24.packageID, newPck24)
    table.insert(newPck25.packageID, newPck25)
    table.insert(newPck26.packageID, newPck26)
    table.insert(newPck27.packageID, newPck27)
    table.insert(newPck28.packageID, newPck28)
    table.insert(newPck29.packageID, newPck29)
    table.insert(newPck30.packageID, newPck30)

    table.insert(newPck31.packageID, newPck31)
    table.insert(newPck32.packageID, newPck32)
    table.insert(newPck33.packageID, newPck33)
    table.insert(newPck34.packageID, newPck34)
    table.insert(newPck35.packageID, newPck35)
    table.insert(newPck36.packageID, newPck36)
    table.insert(newPck37.packageID, newPck37)
    table.insert(newPck38.packageID, newPck38)
    table.insert(newPck39.packageID, newPck39)
    table.insert(newPck40.packageID, newPck40)

    return table

def read(table):
    temp = " "
    unfilteredGraphData = readFile(temp, table)
    print(unfilteredGraphData)
    ###hardcode values in