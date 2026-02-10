import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from bean.PackageDetails import *
from bean.TruckDetails import TruckDetails
from bean.AirCargoDetails import AirCargoDetails
from exception.InvalidVehicleError import InvalidVehicleError
from exception.VehicleCapacityAlreadyExceededError import VehicleCapacityAlreadyExceededError
from service.ManageCargoSystem import ManageCargoSystem

class CargoDemo:
    def main():
        t1 = TruckDetails(101, "Truck-A", 5, 800)
        a1 = AirCargoDetails(102, "AirCargo-A", 3, 1000)


        p1 = PackageDetails(1)
        p2 = PackageDetails(2)
        p3 = PackageDetails(3)
        p4 = PackageDetails(4)
        p5 = PackageDetails(5)

        cms = ManageCargoSystem()
        cms.setVehicleDetails(t1)
        cms.setVehicleDetails(a1)
        try:
            cms.addPackageToVehicle(p1, 101)
            cms.addPackageToVehicle(p2, 101)
            cms.addPackageToVehicle(p3, 102)
            cms.addPackageToVehicle(p4, 102)
            cms.addPackageToVehicle(p5, 102)
        except VehicleCapacityAlreadyExceededError as vce:
            print(vce)
        except InvalidVehicleError as ive:
            print(ive)

        print("FETCHING PACKAGE:",cms.fetchPackage(1))
        cms.deliverPackage(2)
        print("PENDING PACKAGES",cms.deliveryPendingPackages())
        print("UNDELIVERED PACKAGES COUNT",cms.fetchUndeliveredPackages())


    if __name__ == "__main__":
        main()

    
    
    
