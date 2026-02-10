class PackageDetails:
    def __init__(self,packageID):
        self.packageID = packageID
        self.status = "Undelivered"

    def getPackageID(self):
        return self.packageID
    def setPackageID(self,packageID):
        self.packageID = packageID

    def setStatus(self,status):
        self.status = status
    def getStatus(self):
        return self.status
    #def __str__(self):
        #return str(self.packageID)+'\t'+self.status
    def __repr__(self):
        return str(self.packageID)+'\t'+self.status
