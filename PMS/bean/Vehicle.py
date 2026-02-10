class Vehicle:
    def __init__(self):
        self.regNumber = 0
        self.ownerName = None
        self.mobileNumber = 0
    def __init__(self,regNumber,ownerName,mobileNumber):
        self.regNumber = regNumber
        self.ownerName = ownerName
        self.mobileNumber = mobileNumber
    def getRegNumber(self):
        return self.regNumber
    def getOwnerName(self):
        return self.ownerName
    def getMobileNumber(self):
        return self.mobileNumber
    def __str__(self):
        return self.regNumber + '\t'+self.ownerName +'\t'+ str(self.mobileNumber)
