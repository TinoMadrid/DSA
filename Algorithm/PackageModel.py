class Package:

    def __init__(self, packageID, address, city, state, zip, deliveryDeadline, wgt, specialNotes):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryDeadline = deliveryDeadline
        self.wgt = wgt
        self.specialNotes = specialNotes
