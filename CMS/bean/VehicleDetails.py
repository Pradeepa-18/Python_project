from bean.PackageDetails import PackageDetails
class VehicleDetails:
    def __init__(self,vehicleID,vehicleName,capacity):
        self.vehicleID = vehicleID
        self.vehicleName = vehicleName
        self.capacity = capacity
        self.packageDetails = []
        
    def addPackage(self,pd):
        self.packageDetails.append(pd)
        print(pd.getPackageID()," Package Added Successfully in the Vehicle List")
        
    def getVehicleID(self):
        return self.vehicleID
    def setVehicleID(self,vehicleID):
        self.vehicleID = vehicleID
        
    def setVehicleName(self,vehicleName):
        self.vehicleName = vehicleName
    def getVehicleName(self):
        return self.vehicleName
    
    def setCapacity(self,capacity):
        self.capacity = capacity
    def getCapacity(self):
        return self.capacity

    def getPD(self):
        return self.packageDetails

    def __str__(self):
        return str(self.vehicleID)+'\t'+self.vehicleName+'\t'+str(self.capacity)+str(getPD())
