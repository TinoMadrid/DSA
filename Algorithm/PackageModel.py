class Package:

    def __init__(self, packageID, address, city, state, zip, deliveryDeadline, wgt, specialNotes, timestamp, isLoaded):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryDeadline = deliveryDeadline
        self.wgt = wgt
        self.specialNotes = specialNotes
        self.timestamp = timestamp
        self.isLoaded = isLoaded
