from abc import ABC
class ParkingManagementInterface(ABC):
    def addVehicle(self,vehicle):
        None
    def setVisitorVehicleOutTime(self,regNumber,outTime):
        None
    def getParkedResidentVehicleCount(self):
        None
    def displayAllVehicles(self):
        None
