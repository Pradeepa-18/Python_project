from bean.Vehicle import Vehicle
class VisitorVehicle(Vehicle):
    def __init__(self):
        self.visitingFlatNumber = 0
        self.inTime = 0
        self.outTime = 0
    def __init__(self,regNumber,ownerName,mobileNumber,visitingFlatNumber,inTime):
        self.visitingFlatNumber = visitingFlatNumber
        self.inTime = inTime
        self.outTime = 0
        super().__init__(regNumber,ownerName,mobileNumber)
    def getVisitingFlatNumber(self):
        return self.visitingFlatNumber
    def getInTime(self):
        return self.inTime
    def setOutTime(self,outTime):
        self.outTime = outTime
    def getOutTime(self):
        return self.outTime
    def __str__(self):
        return (self.regNumber + '\t'+self.ownerName +'\t'+ str(self.mobileNumber)+\
               str(self.visitingFlatNumber)+'\t'+str(self.inTime)+'\t'+str(self.outTime))

