import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from bean.Vehicle import Vehicle
from bean.VisitorVehicle import VisitorVehicle
from bean.ResidentVehicle import ResidentVehicle
from service.ParkingManagement import ParkingManagement
from exception.VehicleNotFoundException import VehicleNotFoundException
from exception.ParkingSlotNotAvailableException import ParkingSlotNotAvailableException

class Driver:
    if __name__ == '__main__':
        pms = ParkingManagement()
        v1 = VisitorVehicle('TN49A2222','Senthil',1212121212,201,9)
        v2 = VisitorVehicle('TN49B4444','Ragavan',1414141414,202,8)
        v3 = ResidentVehicle('TN49A2222','Srimathi',1278907878,204,True)
        v4 = ResidentVehicle('TN59A2222','mathi',1289787878,205,True)
        try:
            print(pms.addVehicles(v1))
            print(pms.addVehicles(v2))
            print(pms.addVehicles(v3))
            print(pms.addVehicles(v4))
        except ParkingSlotNotAvailableException as pse:
            print(pse)
        try:
            print(pms.setVisitorVehicleOutTime('TN49B4444',9))
            print(pms.setVisitorVehicleOutTime('TN4545455',6))
        except VehicleNotFoundException as vse:
            print(vse)
        print('Number Of Resident Vehicle Parked: '+ str(pms.getParkedResidentVehicleCount()))
        pms.displayAllVehicles()
        
