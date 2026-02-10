from bean.Vehicle import Vehicle
from bean.VisitorVehicle import VisitorVehicle
from bean.ResidentVehicle import ResidentVehicle
from exception.VehicleNotFoundException import VehicleNotFoundException
from exception.ParkingSlotNotAvailableException import ParkingSlotNotAvailableException

from utility.ParkingManagementInterface import ParkingManagementInterface

class ParkingManagement:
    def __init__(self):
        self.allVehicles = []
        self.slot = 0
    def addVehicles(self,vehicle):
        if len(self.allVehicles) <=2 :
            self.allVehicles.append(vehicle)
            self.slot+=1
            return 'Vehicle parked at ParkingSlot no : '+str(self.slot)
        raise ParkingSlotNotAvailableException('No Parking Slots  Available')
    def setVisitorVehicleOutTime(self,regNumber,outTime):
        for i in self.allVehicles:
            if i.regNumber == regNumber and isinstance(i,VisitorVehicle):
                i.outTime = outTime
                return 'Vehicle with Reg Number : '+  regNumber +' updated successfully'
        raise VehicleNotFoundException ('Searched Vehicle Not Found: ')
    def getParkedResidentVehicleCount(self):
        self.count = 0
        for i in self.allVehicles:
            if isinstance(i,ResidentVehicle):
                if i.parkingStatus == True :
                    self.count+=1
        return self.count
    def displayAllVehicles(self):
        for i in self.allVehicles:
            print(i)
        
        
