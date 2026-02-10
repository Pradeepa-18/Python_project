from abc import ABC
class ManageCargoInterface(ABC):
    def addPackageToVehicle(self,packageDetails,vehicleID):
        None
    def fetchPackage(self,vehicleID):
        None
    def deliverPackage(self,vehicleID):
        None
    def deliveryPendingPackages(self):
        None
    def fetchUndeliveredPackages(self):
        None
