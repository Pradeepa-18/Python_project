from utility.ManageCargoInterface import ManageCargoInterface
from bean.VehicleDetails import VehicleDetails
from exception.InvalidVehicleError import InvalidVehicleError
from exception.VehicleCapacityAlreadyExceededError import VehicleCapacityAlreadyExceededError

class ManageCargoSystem(ManageCargoInterface):
    def __init__(self):
        self.Mainvehicledetails = []
        self.MainpackageList = []
    def setVehicleDetails(self,vd):
        
        self.Mainvehicledetails.append(vd)
    
    def setpackageDetails(self,pd):
        self.MainpackageList.append(pd)

    def getVehicleDetails(self):
        return self.Mainvehicledetails
    def getpackageDetails(self):
        return self.MainpackageList

    def addPackageToVehicle(self,pd,vehicleID):
        self.flag1 = False
        for i in self.Mainvehicledetails:
            if i.getVehicleID() == vehicleID:
                self.flag1 = True
                if len(i.getPD()) < i.getCapacity():
                    pd.setStatus("UnDelivered")
                    self.MainpackageList.append(pd)
                    i.addPackage(pd)
                else:
                    raise VehicleCapacityAlreadyExceededError("VehicleCapacityAlreadyExceededError")
        if(self.flag1 == True):
            print("Successfully Added to the MainPackageList ")
        else:
            raise InvalidVehicleError("Invalid Vehicle Error")
        

    def fetchPackage(self,packageID):
        for i in self.Mainvehicledetails:
            for j in i.getPD():
                if j.getPackageID() == packageID:
                    return i
        return None
    def deliverPackage(self,packageID):
        self.flag1 = False
        for i in self.Mainvehicledetails:
            for j in i.getPD():
                if j.getPackageID() == packageID: 
                    self.flag1 = True
                    if j.getStatus() =="UnDelivered":
                        j.setStatus("Delivered")
                        print("The Given Package Status is changed to Delivered")
                    else:
                        print("The Package is Allready Delivered")
                    return
                
        if self.flag1 == False:
            print("The Given PackageID is not present")
    def deliveryPendingPackages(self):
        self.PendingPackage = []
        for i in self.Mainvehicledetails:
            for j in i.getPD():
                if j.getStatus() == "UnDelivered":
                    self.PendingPackage.append(j)
        return self.PendingPackage
    def fetchUndeliveredPackages(self):
        self.undeliveredPackages = {}
        for i in self.Mainvehicledetails:
            self.count = 0
            for j in i.getPD():
                if j.getStatus() == "UnDelivered":
                    self.count+=1
            self.undeliveredPackages[i.getVehicleID()]=self.count     
        return self.undeliveredPackages
        
    
                
        
