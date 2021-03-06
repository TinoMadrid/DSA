from Algorithm.PackageModel import Package


# the package table is hardcoded since I had ran into many issues trying to read the file dynamically
# this would be O(n) for both time and space complexity since this too grows linearly with the size of the input
# the packageTable, addressTable, and the distanceTable
def readFile(packageTable):
    newPck1 = Package(1, "195 W Oakland Ave", "Salt Lake City", "UT", 84115, "10:30 AM", 21, None, None, False)
    newPck2 = Package(2, "2530 S 500 E", "Salt Lake City", "UT", 84106, "EOD", 44, None, None, False)
    newPck3 = Package(3, "233 Canyon Rd", "Salt Lake City", "UT", 84103, "EOD", 2, "Can only be on truck 2", None,
                      False)
    newPck4 = Package(4, "380 W 2880 S", "Salt Lake City", "UT", 84115, "EOD", 4, None, None, False)
    newPck5 = Package(5, "410 S State St", "Salt Lake City", "UT", 84111, "EOD", 5, None, None, False)
    newPck6 = Package(6, "3060 Lester St", "West Valley City", "UT", 84119, "10:30 AM", 88,
                      "Delayed on flight---will not arrive to depot until 9:05 am", None, False)
    newPck7 = Package(7, "1330 2100 S", "Salt Lake City", "UT", 84106, "EOD", 8, None, None, False)
    newPck8 = Package(8, "300 State St", "Salt Lake City", "UT", 84103, "EOD", 9, None, None, False)
    newPck9 = Package(9, "300 State St", "Salt Lake City", "UT", 84103, "EOD", 2, "Wrong address listed", None, False)
    newPck10 = Package(10, "600 E 900", "Salt Lake City", "UT", 84105, "EOD", 1, None, None, False)

    newPck11 = Package(11, "2600 Taylorsville Blvd", "Salt Lake City", "UT", 84118, "EOD", 1, None, None, False)
    newPck12 = Package(12, "3575 W Valley Central Station bus Loop", "West Valley City", "UT", 84119, "EOD", 1, None,
                       None, False)
    newPck13 = Package(13, "2010 W 500 S", "Salt Lake City", "UT", 84104, "10:30 AM", 2, None, None, False)
    newPck14 = Package(14, "4300 S 1300 E", "Millcreek", "UT", 84117, "10:30 AM", 88, "Must be delivered with 15 and 19",
                       None, False)
    newPck15 = Package(15, "4580 S 2300 E", "Holladay", "UT", 84117, "9:00 AM", 4, None, None, False)
    newPck16 = Package(16, "4580 S 2300 E", "Holladay", "UT", 84117, "10:30 AM", 88, "Must be delivered with 13 and 19",
                       None, False)
    newPck17 = Package(17, "3148 S 1100 W", "Salt Lake City", "UT", 84119, "EOD", 2, None, None, False)
    newPck18 = Package(18, "1488 4800 S", "Salt Lake City", "UT", 84123, "EOD", 6, "Can only be on truck 2", None,
                       False)
    newPck19 = Package(19, "177 W Price Ave", "Salt Lake City", "UT", 84115, "EOD", 37, None, None, False)
    newPck20 = Package(20, "3595 Main St", "Salt Lake City", "UT", 84115, "10:30 AM", 37, "Must be delivered with 13 and 15",
                       None, False)

    newPck21 = Package(21, "3595 Main St", "Salt Lake City", "UT", 84115, "EOD", 3, None, None, False)
    newPck22 = Package(22, "6351 South 900 East", "Murray", "UT", 84121, "EOD", 2, None, None, False)
    newPck23 = Package(23, "5100 South 2700 West", "Salt Lake City", "UT", 84118, "EOD", 5, None, None, False)
    newPck24 = Package(24, "5025 State St", "Murray", "UT", 84107, "EOD", 7, None, None, False)
    newPck25 = Package(25, "5383 South 900 East #104", "Salt Lake City", "UT", 84117, "10:30 AM", 7,
                       "Delayed on flight---will not arrive to depot until 9:05 am", None, False)
    newPck26 = Package(26, "5383 South 900 East #104", "Salt Lake City", "UT", 84117, "EOD", 25, None, None, False)
    newPck27 = Package(27, "1060 Dalton Ave S", "Salt Lake City", "UT", 84104, "EOD", 5, None, None, False)
    newPck28 = Package(28, "2835 Main St", "Salt Lake City", "UT", 84115, "EOD", 7,
                       "Delayed on flight---will not arrive to depot until 9:05 am", None, False)
    newPck29 = Package(29, "1330 2100 S", "Salt Lake City", "UT", 84106, "10:30 AM", 2, None, None, False)
    newPck30 = Package(30, "300 State St", "Salt Lake City", "UT", 84103, "10:30 AM", 1, None, None, False)

    newPck31 = Package(31, "3365 S 900 W", "Salt Lake City", "UT", 84119, "10:30 AM", 1, None, None, False)
    newPck32 = Package(32, "3365 S 900 W", "Salt Lake City", "UT", 84119, "EOD", 1,
                       "Delayed on flight---will not arrive to depot until 9:05 am", None, False)
    newPck33 = Package(33, "2530 S 500 E", "Salt Lake City", "UT", 84106, "EOD", 1, None, None, False)
    newPck34 = Package(34, "4580 S 2300 E", "Holladay", "UT", 84117, "10:30 AM", 2, None, None, False)
    newPck35 = Package(35, "1060 Dalton Ave S", "Salt Lake City", "UT", 84104, "EOD", 88, None, None, False)
    newPck36 = Package(36, "2300 Parkway Blvd", "West Valley City", "UT", 84119, "EOD", 88, "Can only be on truck 2",
                       None, False)
    newPck37 = Package(37, "410 S State St", "Salt Lake City", "UT", 84111, "10:30 AM", 2, None, None, False)
    newPck38 = Package(38, "410 S State St", "Salt Lake City", "UT", 84111, "EOD", 9, "Can only be on truck 2", None,
                       False)
    newPck39 = Package(39, "2010 W 500 S", "Salt Lake City", "UT", 84104, "EOD", 9, None, None, False)
    newPck40 = Package(40, "380 W 2880 S", "Salt Lake City", "UT", 84115, "10:30 AM", 45, None, None, False)

    packageTable.insert(newPck1.packageID, newPck1)
    packageTable.insert(newPck2.packageID, newPck2)
    packageTable.insert(newPck3.packageID, newPck3)
    packageTable.insert(newPck4.packageID, newPck4)
    packageTable.insert(newPck5.packageID, newPck5)
    packageTable.insert(newPck6.packageID, newPck6)
    packageTable.insert(newPck7.packageID, newPck7)
    packageTable.insert(newPck8.packageID, newPck8)
    packageTable.insert(newPck9.packageID, newPck9)
    packageTable.insert(newPck10.packageID, newPck10)

    packageTable.insert(newPck11.packageID, newPck11)
    packageTable.insert(newPck12.packageID, newPck12)
    packageTable.insert(newPck13.packageID, newPck13)
    packageTable.insert(newPck14.packageID, newPck14)
    packageTable.insert(newPck15.packageID, newPck15)
    packageTable.insert(newPck16.packageID, newPck16)
    packageTable.insert(newPck17.packageID, newPck17)
    packageTable.insert(newPck18.packageID, newPck18)
    packageTable.insert(newPck19.packageID, newPck19)
    packageTable.insert(newPck20.packageID, newPck20)

    packageTable.insert(newPck21.packageID, newPck21)
    packageTable.insert(newPck22.packageID, newPck22)
    packageTable.insert(newPck23.packageID, newPck23)
    packageTable.insert(newPck24.packageID, newPck24)
    packageTable.insert(newPck25.packageID, newPck25)
    packageTable.insert(newPck26.packageID, newPck26)
    packageTable.insert(newPck27.packageID, newPck27)
    packageTable.insert(newPck28.packageID, newPck28)
    packageTable.insert(newPck29.packageID, newPck29)
    packageTable.insert(newPck30.packageID, newPck30)

    packageTable.insert(newPck31.packageID, newPck31)
    packageTable.insert(newPck32.packageID, newPck32)
    packageTable.insert(newPck33.packageID, newPck33)
    packageTable.insert(newPck34.packageID, newPck34)
    packageTable.insert(newPck35.packageID, newPck35)
    packageTable.insert(newPck36.packageID, newPck36)
    packageTable.insert(newPck37.packageID, newPck37)
    packageTable.insert(newPck38.packageID, newPck38)
    packageTable.insert(newPck39.packageID, newPck39)
    packageTable.insert(newPck40.packageID, newPck40)

    ############################################################################################################
    distanceTable = [[] for i in range(27)]
    addressTable = [[] for i in range(27)]

    distanceTable[0].append(0.0)
    distanceTable[0].append(7.2)
    distanceTable[0].append(3.8)
    distanceTable[0].append(11.0)
    distanceTable[0].append(2.2)
    distanceTable[0].append(3.5)
    distanceTable[0].append(10.9)
    distanceTable[0].append(8.6)
    distanceTable[0].append(7.6)

    distanceTable[0].append(2.8)
    distanceTable[0].append(6.4)
    distanceTable[0].append(3.2)
    distanceTable[0].append(7.6)
    distanceTable[0].append(5.2)
    distanceTable[0].append(4.4)
    distanceTable[0].append(3.7)
    distanceTable[0].append(7.6)
    distanceTable[0].append(2.0)

    distanceTable[0].append(3.6)
    distanceTable[0].append(6.5)
    distanceTable[0].append(1.9)
    distanceTable[0].append(3.4)
    distanceTable[0].append(2.4)
    distanceTable[0].append(6.4)
    distanceTable[0].append(2.4)
    distanceTable[0].append(5.0)
    distanceTable[0].append(3.6)
    ############################################################################################################
    distanceTable[1].append(7.2)
    distanceTable[1].append(0.0)
    distanceTable[1].append(7.1)
    distanceTable[1].append(6.4)
    distanceTable[1].append(6.0)
    distanceTable[1].append(4.8)
    distanceTable[1].append(1.6)
    distanceTable[1].append(2.8)
    distanceTable[1].append(4.8)

    distanceTable[1].append(6.3)
    distanceTable[1].append(7.3)
    distanceTable[1].append(5.3)
    distanceTable[1].append(4.8)
    distanceTable[1].append(3.0)
    distanceTable[1].append(4.6)
    distanceTable[1].append(4.5)
    distanceTable[1].append(7.4)
    distanceTable[1].append(6.0)

    distanceTable[1].append(5.0)
    distanceTable[1].append(4.8)
    distanceTable[1].append(9.5)
    distanceTable[1].append(10.9)
    distanceTable[1].append(8.3)
    distanceTable[1].append(6.9)
    distanceTable[1].append(10.0)
    distanceTable[1].append(4.4)
    distanceTable[1].append(13.0)

    distanceTable[2].extend((3.8, 7.1, 0.0, 9.2, 4.4, 2.8, 8.6, 6.3, 5.3, 1.6, 10.4, 3.0, 5.3, 6.5, 5.6, 5.8, 5.7, 4.1,
                             3.6, 4.3, 3.3, 5.0, 6.1, 9.7, 6.1, 2.8, 7.4))
    distanceTable[3].extend((
        11.0, 6.4, 9.2, 0.0, 5.6, 6.9, 8.6, 4.0, 11.1, 7.3, 1.0, 6.4, 11.1, 3.9, 4.3, 4.4, 7.2, 5.3,
        6.0, 10.6, 5.9, 7.4, 4.7, 0.6, 6.4, 10.1, 10.1))
    distanceTable[4].extend((2.2, 6.0, 4.4, 5.6, 0.0, 1.9, 7.9, 5.1, 7.5, 2.6, 6.5, 1.5, 7.5, 3.2, 2.4, 2.7, 1.4, 0.5,
                             1.7, 6.5, 3.2, 5.2, 2.5, 6.0, 4.2, 5.4, 5.5))
    distanceTable[5].extend((3.5, 4.8, 2.8, 6.9, 1.9, 0.0, 6.3, 4.3, 4.5, 1.5, 8.7, 0.8, 4.5, 3.9, 3.0, 3.8, 5.7, 1.9,
                             1.1, 3.5, 4.9, 6.9, 4.2, 9.0, 5.9, 3.5, 7.2))
    distanceTable[6].extend((10.9, 1.6, 8.6, 8.6, 7.9, 6.3, 0.0, 4.0, 4.2, 8.0, 8.6, 6.9, 4.2, 4.2, 8.0, 5.8, 7.2, 7.7,
                             6.6, 3.2, 11.2, 12.7, 10.0, 8.2, 11.7, 5.1, 14.2))
    distanceTable[7].extend((8.6, 2.8, 6.3, 4.0, 5.1, 4.3, 4.0, 0.0, 7.7, 9.3, 4.6, 4.8, 7.7, 1.6, 3.3, 3.4, 3.1, 5.1,
                             4.6, 6.7, 8.1, 10.4, 7.8, 4.2, 9.5, 6.2, 10.7))
    distanceTable[8].extend((7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.0, 4.8, 11.9, 4.7, 0.6, 7.6, 7.8, 6.6, 7.2, 5.9,
                             5.4, 1.0, 8.5, 10.3, 7.8, 11.5, 9.5, 2.8, 14.1))
    distanceTable[9].extend((2.8, 6.3, 1.6, 7.3, 2.6, 1.5, 8.0, 9.3, 4.8, 0.0, 9.4, 1.1, 5.1, 4.6, 3.7, 4.0, 6.7, 2.3,
                             1.8, 4.1, 3.8, 5.8, 4.3, 7.8, 4.8, 3.2, 6.0))
    distanceTable[10].extend((6.4, 7.3, 10.4, 1.0, 6.5, 8.7, 8.6, 4.6, 11.9, 9.4, 0.0, 7.3, 12.0, 4.9, 5.2, 5.4, 8.1,
                              6.2, 6.9, 11.5, 6.9, 8.3, 4.1, 0.4, 4.9, 11.0, 6.8))
    distanceTable[11].extend((3.2, 5.3, 3.0, 6.4, 1.5, 0.8, 6.9, 4.8, 4.7, 1.1, 7.3, 0.0, 4.7, 3.5, 2.6, 2.9, 6.3, 1.2,
                              1.0, 3.7, 4.1, 6.2, 3.4, 6.9, 5.2, 3.7, 6.4))
    distanceTable[12].extend((
        7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.6, 5.1, 12.0, 4.7, 0.0, 7.3, 7.8, 6.6, 7.2, 5.9,
        5.4, 1.0, 8.5, 10.3, 7.8, 11.5, 9.5, 2.8, 14.1))
    distanceTable[13].extend((5.2, 3.0, 6.5, 3.9, 3.2, 3.9, 4.2, 1.6, 7.6, 4.6, 4.9, 3.5, 7.3, 0.0, 1.3, 1.5, 4.0, 3.2,
                              3.0, 6.9, 6.2, 8.2, 5.5, 4.4, 7.2, 6.4, 10.5))
    distanceTable[14].extend((4.4, 4.6, 5.6, 4.3, 2.4, 3.0, 8.0, 3.3, 7.8, 3.7, 5.2, 2.6, 7.8, 1.3, 0.0, 0.6, 6.4, 2.4,
                              2.2, 6.8, 5.3, 7.4, 4.6, 4.8, 6.3, 6.5, 8.8))
    distanceTable[15].extend((3.7, 4.5, 5.8, 4.4, 2.7, 3.8, 5.8, 3.4, 6.6, 4.0, 5.4, 2.9, 6.6, 1.5, 0.6, 0.0, 5.6, 1.6,
                              1.7, 6.4, 4.9, 6.9, 4.2, 5.6, 5.9, 5.7, 8.4))
    distanceTable[16].extend((7.6, 7.4, 5.7, 7.2, 1.4, 5.7, 7.2, 3.1, 7.2, 6.7, 8.1, 6.3, 7.2, 4.0, 6.4, 5.6, 0.0, 7.1,
                              6.1, 7.2, 10.6, 12.0, 9.4, 7.5, 11.1, 6.2, 13.6))
    distanceTable[17].extend((2.0, 6.0, 4.1, 5.3, 0.5, 1.9, 7.7, 5.1, 5.9, 2.3, 6.2, 1.2, 5.9, 3.2, 2.4, 1.6, 7.1, 0.0,
                              1.6, 4.9, 3.0, 5.0, 2.3, 5.5, 4.0, 5.1, 5.2))
    distanceTable[18].extend((3.6, 5.0, 3.6, 6.0, 1.7, 1.1, 6.6, 4.6, 5.4, 1.8, 6.9, 1.0, 5.4, 3.0, 2.2, 1.7, 6.1, 1.6,
                              0.0, 4.4, 4.6, 6.6, 3.9, 6.5, 5.6, 4.3, 6.9))
    distanceTable[19].extend((
        6.5, 4.8, 4.3, 10.6, 6.5, 3.5, 3.2, 6.7, 1.0, 4.1, 11.5, 3.7, 1.0, 6.9, 6.8, 6.4, 7.2, 4.9,
        4.4, 0.0, 7.5, 9.3, 6.8, 11.4, 8.5, 1.8, 13.1))
    distanceTable[20].extend((
        1.9, 9.5, 3.3, 5.9, 3.2, 4.9, 11.2, 8.1, 8.5, 3.8, 6.9, 4.1, 8.5, 6.2, 5.3, 4.9, 10.6, 3.0,
        4.6, 7.5, 0.0, 2.0, 2.9, 6.4, 2.8, 6.0, 4.1))
    distanceTable[21].extend((3.4, 10.9, 5.0, 7.4, 5.2, 6.9, 12.7, 10.4, 10.3, 5.8, 8.3, 6.2, 10.3, 8.2, 7.4, 6.9, 12.0,
                              5.0, 6.6, 9.3, 2.0, 0.0, 4.4, 7.9, 3.4, 7.9, 4.7))
    distanceTable[22].extend((2.4, 8.3, 6.1, 4.7, 2.5, 4.2, 10.0, 7.8, 7.8, 4.3, 4.1, 3.4, 7.8, 5.5, 4.6, 4.2, 9.4, 2.3,
                              3.9, 6.8, 2.9, 4.4, 0.0, 4.5, 1.7, 6.8, 3.1))
    distanceTable[23].extend((
        6.4, 6.9, 9.7, 0.6, 6.0, 9.0, 8.2, 4.2, 11.5, 7.8, 0.4, 6.9, 11.5, 4.4, 4.8, 5.6, 7.5, 5.5,
        6.5, 11.4, 6.4, 7.9, 4.5, 0.0, 5.4, 10.6, 7.8))
    distanceTable[24].extend((2.4, 10.0, 6.1, 6.4, 4.2, 5.9, 11.7, 9.5, 9.5, 4.8, 4.9, 5.2, 9.5, 7.2, 6.3, 5.9, 11.1,
                              4.0, 5.6, 8.5, 2.8, 3.4, 1.7, 5.4, 0.0, 7.0, 1.3))
    distanceTable[25].extend((
        5.0, 4.4, 2.8, 10.1, 5.4, 3.5, 5.1, 6.2, 2.8, 3.2, 11.0, 3.7, 2.8, 6.4, 6.5, 5.7, 6.2, 5.1,
        4.3, 1.8, 6.0, 7.9, 6.8, 10.6, 7.0, 0.0, 8.3))
    distanceTable[26].extend((3.6, 13.0, 7.4, 10.1, 5.5, 7.2, 14.2, 10.7, 14.1, 6.0, 6.8, 6.4, 14.1, 10.5, 8.8, 8.4,
                              13.6, 5.2, 6.9, 13.1, 4.1, 4.7, 3.1, 7.8, 1.3, 8.3, 0.0))
    ############################################################################################################
    addressTable[0].extend(("Western Governors University 4001 South 700 East(84107)",
                            " Western Governors University 4001 South 700 East",
                            " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                            " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                            " Salt Lake City Division of Health Services 177 W Price Ave",
                            " South Salt Lake Public Works 195 W Oakland Ave",
                            " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                            " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                            " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                            " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                            " Salt Lake County Mental Health 3148 S 1100 W",
                            " Salt Lake County/United Police Dept 3365 S 900 W",
                            " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                            " Housing Auth. of Salt Lake County 3595 Main St",
                            " Utah DMV Administrative Office 380 W 2880 S",
                            " Third District Juvenile Court 410 S State St",
                            " Cottonwood Regional Softball Complex 4300 S 1300 E", " Holiday City Office 4580 S 2300 E",
                            " Murray City Museum 5025 State St",
                            " Valley Regional Softball Complex 5100 South 2700 West",
                            " City Center of Rock Springs 5383 South 900 East #104",
                            " Rice Terrace Pavilion Park 600 E 900",
                            " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[1].extend(("International Peace Gardens 1060 Dalton Ave S(84104)",
                            " Western Governors University 4001 South 700 East",
                            " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                            " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                            " Salt Lake City Division of Health Services 177 W Price Ave",
                            " South Salt Lake Public Works 195 W Oakland Ave",
                            " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                            " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                            " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                            " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                            " Salt Lake County Mental Health 3148 S 1100 W",
                            " Salt Lake County/United Police Dept 3365 S 900 W",
                            " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                            " Housing Auth. of Salt Lake County 3595 Main St",
                            " Utah DMV Administrative Office 380 W 2880 S",
                            " Third District Juvenile Court 410 S State St",
                            " Cottonwood Regional Softball Complex 4300 S 1300 E", " Holiday City Office 4580 S 2300 E",
                            " Murray City Museum 5025 State St",
                            " Valley Regional Softball Complex 5100 South 2700 West",
                            " City Center of Rock Springs 5383 South 900 East #104",
                            " Rice Terrace Pavilion Park 600 E 900",
                            " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[2].extend(("Sugar House Park 1330 2100 S(84106)", " Western Governors University 4001 South 700 East",
                            " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                            " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                            " Salt Lake City Division of Health Services 177 W Price Ave",
                            " South Salt Lake Public Works 195 W Oakland Ave",
                            " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                            " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                            " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                            " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                            " Salt Lake County Mental Health 3148 S 1100 W",
                            " Salt Lake County/United Police Dept 3365 S 900 W",
                            " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                            " Housing Auth. of Salt Lake County 3595 Main St",
                            " Utah DMV Administrative Office 380 W 2880 S",
                            " Third District Juvenile Court 410 S State St",
                            " Cottonwood Regional Softball Complex 4300 S 1300 E", " Holiday City Office 4580 S 2300 E",
                            " Murray City Museum 5025 State St",
                            " Valley Regional Softball Complex 5100 South 2700 West",
                            " City Center of Rock Springs 5383 South 900 East #104",
                            " Rice Terrace Pavilion Park 600 E 900",
                            " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[3].extend(("Taylorsville-Bennion Heritage City Gov Off 1488 4800 S(84123)",
                            " Western Governors University 4001 South 700 East",
                            " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                            " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                            " Salt Lake City Division of Health Services 177 W Price Ave",
                            " South Salt Lake Public Works 195 W Oakland Ave",
                            " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                            " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                            " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                            " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                            " Salt Lake County Mental Health 3148 S 1100 W",
                            " Salt Lake County/United Police Dept 3365 S 900 W",
                            " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                            " Housing Auth. of Salt Lake County 3595 Main St",
                            " Utah DMV Administrative Office 380 W 2880 S",
                            " Third District Juvenile Court 410 S State St",
                            " Cottonwood Regional Softball Complex 4300 S 1300 E", " Holiday City Office 4580 S 2300 E",
                            " Murray City Museum 5025 State St",
                            " Valley Regional Softball Complex 5100 South 2700 West",
                            " City Center of Rock Springs 5383 South 900 East #104",
                            " Rice Terrace Pavilion Park 600 E 900",
                            " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[4].extend(("Salt Lake City Division of Health Services 177 W Price Ave(84115)",
                            " Western Governors University 4001 South 700 East",
                            " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                            " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                            " Salt Lake City Division of Health Services 177 W Price Ave",
                            " South Salt Lake Public Works 195 W Oakland Ave",
                            " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                            " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                            " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                            " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                            " Salt Lake County Mental Health 3148 S 1100 W",
                            " Salt Lake County/United Police Dept 3365 S 900 W",
                            " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                            " Housing Auth. of Salt Lake County 3595 Main St",
                            " Utah DMV Administrative Office 380 W 2880 S",
                            " Third District Juvenile Court 410 S State St",
                            " Cottonwood Regional Softball Complex 4300 S 1300 E", " Holiday City Office 4580 S 2300 E",
                            " Murray City Museum 5025 State St",
                            " Valley Regional Softball Complex 5100 South 2700 West",
                            " City Center of Rock Springs 5383 South 900 East #104",
                            " Rice Terrace Pavilion Park 600 E 900",
                            " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[5].extend(("South Salt Lake Public Works 195 W Oakland Ave(84115)",
                            " Western Governors University 4001 South 700 East",
                            " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                            " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                            " Salt Lake City Division of Health Services 177 W Price Ave",
                            " South Salt Lake Public Works 195 W Oakland Ave",
                            " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                            " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                            " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                            " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                            " Salt Lake County Mental Health 3148 S 1100 W",
                            " Salt Lake County/United Police Dept 3365 S 900 W",
                            " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                            " Housing Auth. of Salt Lake County 3595 Main St",
                            " Utah DMV Administrative Office 380 W 2880 S",
                            " Third District Juvenile Court 410 S State St",
                            " Cottonwood Regional Softball Complex 4300 S 1300 E", " Holiday City Office 4580 S 2300 E",
                            " Murray City Museum 5025 State St",
                            " Valley Regional Softball Complex 5100 South 2700 West",
                            " City Center of Rock Springs 5383 South 900 East #104",
                            " Rice Terrace Pavilion Park 600 E 900",
                            " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[6].extend(("Salt Lake City Streets and Sanitation 2010 W 500 S(84104)",
                            " Western Governors University 4001 South 700 East",
                            " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                            " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                            " Salt Lake City Division of Health Services 177 W Price Ave",
                            " South Salt Lake Public Works 195 W Oakland Ave",
                            " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                            " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                            " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                            " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                            " Salt Lake County Mental Health 3148 S 1100 W",
                            " Salt Lake County/United Police Dept 3365 S 900 W",
                            " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                            " Housing Auth. of Salt Lake County 3595 Main St",
                            " Utah DMV Administrative Office 380 W 2880 S",
                            " Third District Juvenile Court 410 S State St",
                            " Cottonwood Regional Softball Complex 4300 S 1300 E", " Holiday City Office 4580 S 2300 E",
                            " Murray City Museum 5025 State St",
                            " Valley Regional Softball Complex 5100 South 2700 West",
                            " City Center of Rock Springs 5383 South 900 East #104",
                            " Rice Terrace Pavilion Park 600 E 900",
                            " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[7].extend(("Deker Lake 2300 Parkway Blvd(84119)", " Western Governors University 4001 South 700 East",
                            " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                            " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                            " Salt Lake City Division of Health Services 177 W Price Ave",
                            " South Salt Lake Public Works 195 W Oakland Ave",
                            " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                            " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                            " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                            " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                            " Salt Lake County Mental Health 3148 S 1100 W",
                            " Salt Lake County/United Police Dept 3365 S 900 W",
                            " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                            " Housing Auth. of Salt Lake County 3595 Main St",
                            " Utah DMV Administrative Office 380 W 2880 S",
                            " Third District Juvenile Court 410 S State St",
                            " Cottonwood Regional Softball Complex 4300 S 1300 E", " Holiday City Office 4580 S 2300 E",
                            " Murray City Museum 5025 State St",
                            " Valley Regional Softball Complex 5100 South 2700 West",
                            " City Center of Rock Springs 5383 South 900 East #104",
                            " Rice Terrace Pavilion Park 600 E 900",
                            " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[8].extend(("Salt Lake City Ottinger Hall 233 Canyon Rd(84103)",
                            " Western Governors University 4001 South 700 East",
                            " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                            " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                            " Salt Lake City Division of Health Services 177 W Price Ave",
                            " South Salt Lake Public Works 195 W Oakland Ave",
                            " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                            " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                            " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                            " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                            " Salt Lake County Mental Health 3148 S 1100 W",
                            " Salt Lake County/United Police Dept 3365 S 900 W",
                            " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                            " Housing Auth. of Salt Lake County 3595 Main St",
                            " Utah DMV Administrative Office 380 W 2880 S",
                            " Third District Juvenile Court 410 S State St",
                            " Cottonwood Regional Softball Complex 4300 S 1300 E", " Holiday City Office 4580 S 2300 E",
                            " Murray City Museum 5025 State St",
                            " Valley Regional Softball Complex 5100 South 2700 West",
                            " City Center of Rock Springs 5383 South 900 East #104",
                            " Rice Terrace Pavilion Park 600 E 900",
                            " South Wheeler Historic Farm 6351 South 900 East"))

    addressTable[9].extend(("Columbus Library 2530 S 500 E(84106)", " Western Governors University 4001 South 700 East",
                            " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                            " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                            " Salt Lake City Division of Health Services 177 W Price Ave",
                            " South Salt Lake Public Works 195 W Oakland Ave",
                            " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                            " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                            " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                            " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                            " Salt Lake County Mental Health 3148 S 1100 W",
                            " Salt Lake County/United Police Dept 3365 S 900 W",
                            " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                            " Housing Auth. of Salt Lake County 3595 Main St",
                            " Utah DMV Administrative Office 380 W 2880 S",
                            " Third District Juvenile Court 410 S State St",
                            " Cottonwood Regional Softball Complex 4300 S 1300 E", " Holiday City Office 4580 S 2300 E",
                            " Murray City Museum 5025 State St",
                            " Valley Regional Softball Complex 5100 South 2700 West",
                            " City Center of Rock Springs 5383 South 900 East #104",
                            " Rice Terrace Pavilion Park 600 E 900",
                            " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[10].extend(("Taylorsville City Hall 2600 Taylorsville Blvd(84118)",
                             " Western Governors University 4001 South 700 East",
                             " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                             " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                             " Salt Lake City Division of Health Services 177 W Price Ave",
                             " South Salt Lake Public Works 195 W Oakland Ave",
                             " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                             " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                             " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                             " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                             " Salt Lake County Mental Health 3148 S 1100 W",
                             " Salt Lake County/United Police Dept 3365 S 900 W",
                             " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                             " Housing Auth. of Salt Lake County 3595 Main St",
                             " Utah DMV Administrative Office 380 W 2880 S",
                             " Third District Juvenile Court 410 S State St",
                             " Cottonwood Regional Softball Complex 4300 S 1300 E",
                             " Holiday City Office 4580 S 2300 E", " Murray City Museum 5025 State St",
                             " Valley Regional Softball Complex 5100 South 2700 West",
                             " City Center of Rock Springs 5383 South 900 East #104",
                             " Rice Terrace Pavilion Park 600 E 900",
                             " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[11].extend(("South Salt Lake Police 2835 Main St(84115)",
                             " Western Governors University 4001 South 700 East",
                             " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                             " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                             " Salt Lake City Division of Health Services 177 W Price Ave",
                             " South Salt Lake Public Works 195 W Oakland Ave",
                             " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                             " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                             " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                             " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                             " Salt Lake County Mental Health 3148 S 1100 W",
                             " Salt Lake County/United Police Dept 3365 S 900 W",
                             " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                             " Housing Auth. of Salt Lake County 3595 Main St",
                             " Utah DMV Administrative Office 380 W 2880 S",
                             " Third District Juvenile Court 410 S State St",
                             " Cottonwood Regional Softball Complex 4300 S 1300 E",
                             " Holiday City Office 4580 S 2300 E", " Murray City Museum 5025 State St",
                             " Valley Regional Softball Complex 5100 South 2700 West",
                             " City Center of Rock Springs 5383 South 900 East #104",
                             " Rice Terrace Pavilion Park 600 E 900",
                             " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[12].extend(("Council Hall 300 State St(84103)", " Western Governors University 4001 South 700 East",
                             " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                             " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                             " Salt Lake City Division of Health Services 177 W Price Ave",
                             " South Salt Lake Public Works 195 W Oakland Ave",
                             " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                             " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                             " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                             " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                             " Salt Lake County Mental Health 3148 S 1100 W",
                             " Salt Lake County/United Police Dept 3365 S 900 W",
                             " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                             " Housing Auth. of Salt Lake County 3595 Main St",
                             " Utah DMV Administrative Office 380 W 2880 S",
                             " Third District Juvenile Court 410 S State St",
                             " Cottonwood Regional Softball Complex 4300 S 1300 E",
                             " Holiday City Office 4580 S 2300 E", " Murray City Museum 5025 State St",
                             " Valley Regional Softball Complex 5100 South 2700 West",
                             " City Center of Rock Springs 5383 South 900 East #104",
                             " Rice Terrace Pavilion Park 600 E 900",
                             " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[13].extend(("Redwood Park 3060 Lester St(84119)", " Western Governors University 4001 South 700 East",
                             " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                             " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                             " Salt Lake City Division of Health Services 177 W Price Ave",
                             " South Salt Lake Public Works 195 W Oakland Ave",
                             " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                             " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                             " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                             " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                             " Salt Lake County Mental Health 3148 S 1100 W",
                             " Salt Lake County/United Police Dept 3365 S 900 W",
                             " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                             " Housing Auth. of Salt Lake County 3595 Main St",
                             " Utah DMV Administrative Office 380 W 2880 S",
                             " Third District Juvenile Court 410 S State St",
                             " Cottonwood Regional Softball Complex 4300 S 1300 E",
                             " Holiday City Office 4580 S 2300 E", " Murray City Museum 5025 State St",
                             " Valley Regional Softball Complex 5100 South 2700 West",
                             " City Center of Rock Springs 5383 South 900 East #104",
                             " Rice Terrace Pavilion Park 600 E 900",
                             " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[14].extend(("Salt Lake County Mental Health 3148 S 1100 W(84119)",
                             " Western Governors University 4001 South 700 East",
                             " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                             " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                             " Salt Lake City Division of Health Services 177 W Price Ave",
                             " South Salt Lake Public Works 195 W Oakland Ave",
                             " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                             " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                             " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                             " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                             " Salt Lake County Mental Health 3148 S 1100 W",
                             " Salt Lake County/United Police Dept 3365 S 900 W",
                             " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                             " Housing Auth. of Salt Lake County 3595 Main St",
                             " Utah DMV Administrative Office 380 W 2880 S",
                             " Third District Juvenile Court 410 S State St",
                             " Cottonwood Regional Softball Complex 4300 S 1300 E",
                             " Holiday City Office 4580 S 2300 E", " Murray City Museum 5025 State St",
                             " Valley Regional Softball Complex 5100 South 2700 West",
                             " City Center of Rock Springs 5383 South 900 East #104",
                             " Rice Terrace Pavilion Park 600 E 900",
                             " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[15].extend(("Salt Lake County/United Police Dept 3365 S 900 W(84119)",
                             " Western Governors University 4001 South 700 East",
                             " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                             " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                             " Salt Lake City Division of Health Services 177 W Price Ave",
                             " South Salt Lake Public Works 195 W Oakland Ave",
                             " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                             " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                             " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                             " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                             " Salt Lake County Mental Health 3148 S 1100 W",
                             " Salt Lake County/United Police Dept 3365 S 900 W",
                             " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                             " Housing Auth. of Salt Lake County 3595 Main St",
                             " Utah DMV Administrative Office 380 W 2880 S",
                             " Third District Juvenile Court 410 S State St",
                             " Cottonwood Regional Softball Complex 4300 S 1300 E",
                             " Holiday City Office 4580 S 2300 E", " Murray City Museum 5025 State St",
                             " Valley Regional Softball Complex 5100 South 2700 West",
                             " City Center of Rock Springs 5383 South 900 East #104",
                             " Rice Terrace Pavilion Park 600 E 900",
                             " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[16].extend(("West Valley Prosecutor 3575 W Valley Central Station bus Loop(84119)",
                             " Western Governors University 4001 South 700 East",
                             " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                             " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                             " Salt Lake City Division of Health Services 177 W Price Ave",
                             " South Salt Lake Public Works 195 W Oakland Ave",
                             " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                             " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                             " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                             " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                             " Salt Lake County Mental Health 3148 S 1100 W",
                             " Salt Lake County/United Police Dept 3365 S 900 W",
                             " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                             " Housing Auth. of Salt Lake County 3595 Main St",
                             " Utah DMV Administrative Office 380 W 2880 S",
                             " Third District Juvenile Court 410 S State St",
                             " Cottonwood Regional Softball Complex 4300 S 1300 E",
                             " Holiday City Office 4580 S 2300 E", " Murray City Museum 5025 State St",
                             " Valley Regional Softball Complex 5100 South 2700 West",
                             " City Center of Rock Springs 5383 South 900 East #104",
                             " Rice Terrace Pavilion Park 600 E 900",
                             " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[17].extend(("Housing Auth. of Salt Lake County 3595 Main St(84115)",
                             " Western Governors University 4001 South 700 East",
                             " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                             " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                             " Salt Lake City Division of Health Services 177 W Price Ave",
                             " South Salt Lake Public Works 195 W Oakland Ave",
                             " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                             " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                             " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                             " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                             " Salt Lake County Mental Health 3148 S 1100 W",
                             " Salt Lake County/United Police Dept 3365 S 900 W",
                             " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                             " Housing Auth. of Salt Lake County 3595 Main St",
                             " Utah DMV Administrative Office 380 W 2880 S",
                             " Third District Juvenile Court 410 S State St",
                             " Cottonwood Regional Softball Complex 4300 S 1300 E",
                             " Holiday City Office 4580 S 2300 E", " Murray City Museum 5025 State St",
                             " Valley Regional Softball Complex 5100 South 2700 West",
                             " City Center of Rock Springs 5383 South 900 East #104",
                             " Rice Terrace Pavilion Park 600 E 900",
                             " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[18].extend(("Utah DMV Administrative Office 380 W 2880 S(84115)",
                             " Western Governors University 4001 South 700 East",
                             " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                             " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                             " Salt Lake City Division of Health Services 177 W Price Ave",
                             " South Salt Lake Public Works 195 W Oakland Ave",
                             " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                             " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                             " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                             " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                             " Salt Lake County Mental Health 3148 S 1100 W",
                             " Salt Lake County/United Police Dept 3365 S 900 W",
                             " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                             " Housing Auth. of Salt Lake County 3595 Main St",
                             " Utah DMV Administrative Office 380 W 2880 S",
                             " Third District Juvenile Court 410 S State St",
                             " Cottonwood Regional Softball Complex 4300 S 1300 E",
                             " Holiday City Office 4580 S 2300 E", " Murray City Museum 5025 State St",
                             " Valley Regional Softball Complex 5100 South 2700 West",
                             " City Center of Rock Springs 5383 South 900 East #104",
                             " Rice Terrace Pavilion Park 600 E 900",
                             " South Wheeler Historic Farm 6351 South 900 East"))

    addressTable[19].extend(("Third District Juvenile Court 410 S State St(84111)",
                             " Western Governors University 4001 South 700 East",
                             " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                             " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                             " Salt Lake City Division of Health Services 177 W Price Ave",
                             " South Salt Lake Public Works 195 W Oakland Ave",
                             " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                             " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                             " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                             " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                             " Salt Lake County Mental Health 3148 S 1100 W",
                             " Salt Lake County/United Police Dept 3365 S 900 W",
                             " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                             " Housing Auth. of Salt Lake County 3595 Main St",
                             " Utah DMV Administrative Office 380 W 2880 S",
                             " Third District Juvenile Court 410 S State St",
                             " Cottonwood Regional Softball Complex 4300 S 1300 E",
                             " Holiday City Office 4580 S 2300 E", " Murray City Museum 5025 State St",
                             " Valley Regional Softball Complex 5100 South 2700 West",
                             " City Center of Rock Springs 5383 South 900 East #104",
                             " Rice Terrace Pavilion Park 600 E 900",
                             " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[20].extend(("Cottonwood Regional Softball 4300 S 1300 E(84117)",
                             " Western Governors University 4001 South 700 East",
                             " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                             " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                             " Salt Lake City Division of Health Services 177 W Price Ave",
                             " South Salt Lake Public Works 195 W Oakland Ave",
                             " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                             " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                             " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                             " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                             " Salt Lake County Mental Health 3148 S 1100 W",
                             " Salt Lake County/United Police Dept 3365 S 900 W",
                             " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                             " Housing Auth. of Salt Lake County 3595 Main St",
                             " Utah DMV Administrative Office 380 W 2880 S",
                             " Third District Juvenile Court 410 S State St",
                             " Cottonwood Regional Softball Complex 4300 S 1300 E",
                             " Holiday City Office 4580 S 2300 E", " Murray City Museum 5025 State St",
                             " Valley Regional Softball Complex 5100 South 2700 West",
                             " City Center of Rock Springs 5383 South 900 East #104",
                             " Rice Terrace Pavilion Park 600 E 900",
                             " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[21].extend(("Holiday City Office 4580 S 2300 E(84117)",
                             " Western Governors University 4001 South 700 East",
                             " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                             " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                             " Salt Lake City Division of Health Services 177 W Price Ave",
                             " South Salt Lake Public Works 195 W Oakland Ave",
                             " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                             " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                             " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                             " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                             " Salt Lake County Mental Health 3148 S 1100 W",
                             " Salt Lake County/United Police Dept 3365 S 900 W",
                             " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                             " Housing Auth. of Salt Lake County 3595 Main St",
                             " Utah DMV Administrative Office 380 W 2880 S",
                             " Third District Juvenile Court 410 S State St",
                             " Cottonwood Regional Softball Complex 4300 S 1300 E",
                             " Holiday City Office 4580 S 2300 E", " Murray City Museum 5025 State St",
                             " Valley Regional Softball Complex 5100 South 2700 West",
                             " City Center of Rock Springs 5383 South 900 East #104",
                             " Rice Terrace Pavilion Park 600 E 900",
                             " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[22].extend(("Murray City Museum 5025 State St(84107)",
                             " Western Governors University 4001 South 700 East",
                             " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                             " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                             " Salt Lake City Division of Health Services 177 W Price Ave",
                             " South Salt Lake Public Works 195 W Oakland Ave",
                             " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                             " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                             " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                             " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                             " Salt Lake County Mental Health 3148 S 1100 W",
                             " Salt Lake County/United Police Dept 3365 S 900 W",
                             " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                             " Housing Auth. of Salt Lake County 3595 Main St",
                             " Utah DMV Administrative Office 380 W 2880 S",
                             " Third District Juvenile Court 410 S State St",
                             " Cottonwood Regional Softball Complex 4300 S 1300 E",
                             " Holiday City Office 4580 S 2300 E", " Murray City Museum 5025 State St",
                             " Valley Regional Softball Complex 5100 South 2700 West",
                             " City Center of Rock Springs 5383 South 900 East #104",
                             " Rice Terrace Pavilion Park 600 E 900",
                             " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[23].extend(("Valley Regional Softball Complex 5100 South 2700 West(84118)",
                             " Western Governors University 4001 South 700 East",
                             " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                             " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                             " Salt Lake City Division of Health Services 177 W Price Ave",
                             " South Salt Lake Public Works 195 W Oakland Ave",
                             " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                             " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                             " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                             " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                             " Salt Lake County Mental Health 3148 S 1100 W",
                             " Salt Lake County/United Police Dept 3365 S 900 W",
                             " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                             " Housing Auth. of Salt Lake County 3595 Main St",
                             " Utah DMV Administrative Office 380 W 2880 S",
                             " Third District Juvenile Court 410 S State St",
                             " Cottonwood Regional Softball Complex 4300 S 1300 E",
                             " Holiday City Office 4580 S 2300 E", " Murray City Museum 5025 State St",
                             " Valley Regional Softball Complex 5100 South 2700 West",
                             " City Center of Rock Springs 5383 South 900 East #104",
                             " Rice Terrace Pavilion Park 600 E 900",
                             " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[24].extend(("City Center of Rock Springs 5383 South 900 East #104(84117)",
                             " Western Governors University 4001 South 700 East",
                             " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                             " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                             " Salt Lake City Division of Health Services 177 W Price Ave",
                             " South Salt Lake Public Works 195 W Oakland Ave",
                             " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                             " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                             " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                             " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                             " Salt Lake County Mental Health 3148 S 1100 W",
                             " Salt Lake County/United Police Dept 3365 S 900 W",
                             " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                             " Housing Auth. of Salt Lake County 3595 Main St",
                             " Utah DMV Administrative Office 380 W 2880 S",
                             " Third District Juvenile Court 410 S State St",
                             " Cottonwood Regional Softball Complex 4300 S 1300 E",
                             " Holiday City Office 4580 S 2300 E", " Murray City Museum 5025 State St",
                             " Valley Regional Softball Complex 5100 South 2700 West",
                             " City Center of Rock Springs 5383 South 900 East #104",
                             " Rice Terrace Pavilion Park 600 E 900",
                             " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[25].extend(("Rice Terrace Pavilion Park 600 E 900 South(84105)",
                             " Western Governors University 4001 South 700 East",
                             " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                             " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                             " Salt Lake City Division of Health Services 177 W Price Ave",
                             " South Salt Lake Public Works 195 W Oakland Ave",
                             " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                             " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                             " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                             " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                             " Salt Lake County Mental Health 3148 S 1100 W",
                             " Salt Lake County/United Police Dept 3365 S 900 W",
                             " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                             " Housing Auth. of Salt Lake County 3595 Main St",
                             " Utah DMV Administrative Office 380 W 2880 S",
                             " Third District Juvenile Court 410 S State St",
                             " Cottonwood Regional Softball Complex 4300 S 1300 E",
                             " Holiday City Office 4580 S 2300 E", " Murray City Museum 5025 State St",
                             " Valley Regional Softball Complex 5100 South 2700 West",
                             " City Center of Rock Springs 5383 South 900 East #104",
                             " Rice Terrace Pavilion Park 600 E 900",
                             " South Wheeler Historic Farm 6351 South 900 East"))
    addressTable[26].extend(("Wheeler Historic Farm 6351 South 900 East(84121)",
                             " Western Governors University 4001 South 700 East",
                             " International Peace Gardens 1060 Dalton Ave S", " Sugar House Park 1330 2100 S",
                             " Taylorsville-Bennion Heritage City Gov Off 1488 4800 S",
                             " Salt Lake City Division of Health Services 177 W Price Ave",
                             " South Salt Lake Public Works 195 W Oakland Ave",
                             " Salt Lake City Streets and Sanitation 2010 W 500 S", " Deker Lake 2300 Parkway Blvd",
                             " Salt Lake City Ottinger Hall 233 Canyon Rd", " Columbus Library 2530 S 500 E",
                             " Taylorsville City Hall 2600 Taylorsville Blvd", " South Salt Lake Police 2835 Main St",
                             " Council Hall 300 State St", " Redwood Park 3060 Lester St",
                             " Salt Lake County Mental Health 3148 S 1100 W",
                             " Salt Lake County/United Police Dept 3365 S 900 W",
                             " West Valley Prosecutor 3575 W Valley Central Station bus Loop",
                             " Housing Auth. of Salt Lake County 3595 Main St",
                             " Utah DMV Administrative Office 380 W 2880 S",
                             " Third District Juvenile Court 410 S State St",
                             " Cottonwood Regional Softball Complex 4300 S 1300 E",
                             " Holiday City Office 4580 S 2300 E", " Murray City Museum 5025 State St",
                             " Valley Regional Softball Complex 5100 South 2700 West",
                             " City Center of Rock Springs 5383 South 900 East #104",
                             " Rice Terrace Pavilion Park 600 E 900",
                             " South Wheeler Historic Farm 6351 South 900 East"))

    return distanceTable, addressTable, packageTable


# this function is the entry point for this file and calls to create the instances of these 3 major tables
# space and time complexity for this function is constant O(1) since the parameter is an empty hash table
def read(table):
    distanceTable, addressTable, packageTable = readFile(table)

    return distanceTable, addressTable, packageTable


# this function is what finds the distance from one location to another by matching indices from the address table
# this function since it has 2 loops and a recursive call, make it O(N^2) which by far one of the worst time complexities
# essentially this function is looking for the address that is matched in the 0 position of the address table and then
# iterates through that list to find the destination, grabs the indices and uses that to look up the distance.
# space complexity for the this function is O(N^2) since each table grows exponentially with the input provided to it.
def address_lookup(fromLocation, toLocation, addressTable, distanceTable):
    tracker = 0
    for begin in addressTable:
        if fromLocation in begin[0]:
            matchingCoordinates = []
            for x in range(len(begin)):
                if toLocation in addressTable[tracker][x]:
                    matchingCoordinates.append(tracker)
                    matchingCoordinates.append(
                        x - 1)  # subtracting 1 since the first string is the next stop, and not doing so would return the index for the
                    break  # from location which anything from and to itself is 0.
            if len(matchingCoordinates) != 0:
                if matchingCoordinates[1] == 27: matchingCoordinates[1] = matchingCoordinates[1] - 1
                return distanceTable[matchingCoordinates[0]][matchingCoordinates[1]]
        tracker += 1
    return address_lookup(fromLocation, toLocation, addressTable,
                          distanceTable)  # function calls itself if the from location is located behind tracker count


# this load functions time and space complexity wise are 0(N) since these lists grow linearly with their inputs
# even though constraints dictate that they can only carry 16 at one time.
def truckOnePriorityLoadOne(truckOne):
    truckOne.append(15)     #900 DL
    truckOne.append(1)      #1030 DL
    truckOne.append(13)     #1030 DL
    truckOne.append(14)     #1030 DL
    truckOne.append(16)     #1030 DL
    truckOne.append(20)     #1030 DL
    truckOne.append(31)     #1030 DL
    truckOne.append(30)     #1030 DL
    truckOne.append(37)
    truckOne.append(19)

    return truckOne


def truckOneLoadTwo(truckOne):
    truckOne.append(4)
    truckOne.append(5)
    truckOne.append(7)
    truckOne.append(8)

    truckOne.append(10)
    truckOne.append(11)
    truckOne.append(12)
    truckOne.append(17)



    return truckOne


def truckTwoPriorityLoadOne(truckTwo):
    # truck leaves at 9:05
    truckTwo.append(6)      #1030 DL
    truckTwo.append(25)     #1030 DL
    truckTwo.append(29)     #1030 DL
    truckTwo.append(34)     #1030 DL

    truckTwo.append(40)     #1030 DL
    return truckTwo


def truckTwoLoadTwo(truckTwo):

    truckTwo.append(3)
    truckTwo.append(18)
    truckTwo.append(21)
    truckTwo.append(22)

    truckTwo.append(23)
    truckTwo.append(24)
    truckTwo.append(28)
    truckTwo.append(32)
    truckTwo.append(36)
    truckTwo.append(38)
    return truckTwo


def truckOneLoadThree(truckOne):
    # packages on truck one after 10:32


    truckOne.append(2)

    truckOne.append(33)
    truckOne.append(26)

    truckOne.append(35)
    truckOne.append(27)


    truckOne.append(39)
    truckOne.append(9)

    return truckOne


# this function prints package details and it too grows linearly with the packageTable size
# as well as time wise since each item needs to be iterated through
def printPackageInfo(packageTable):
    isDelivered = False
    for i in range(41):
        package = packageTable.lookup(i)

        if package is not None:
            if package.timestamp is None:
                isDelivered = False
            else:
                isDelivered = True

            if isDelivered:
                print("Package", package.packageID, "delivered at: %.2f" % package.timestamp, "Special Notes are:",
                      package.specialNotes)
            else:
                if package.isLoaded:
                    print("Package", package.packageID, "is en route", "Special Notes are:",
                          package.specialNotes)
                else:
                    print("Package", package.packageID, "is at hub", "Special Notes are:",
                          package.specialNotes)
