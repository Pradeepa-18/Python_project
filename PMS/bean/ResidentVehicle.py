from bean.Vehicle import Vehicle;
class ResidentVehicle(Vehicle):
    def __init__(self):
        self.flatNumber = 0
        self.parkingStatus = False
    def __init__(self,regNumber,ownerName,mobileNumber,flatNumber,parkingStatus):
        self.flatNumber = flatNumber
        self.parkingStatus = parkingStatus
        super().__init__(regNumber,ownerName,mobileNumber)
    def getflatNumber(self):
        return self.flatNumber
    def getparkingStatus(self):
        return self.parkingStatus

    def __str__(self):
        return self.regNumber + '\t'+self.ownerName +'\t'+ str(self.mobileNumber)+\
               str(self.flatNumber)+'\t'+str(self.parkingStatus)

    
