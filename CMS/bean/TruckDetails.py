from bean.VehicleDetails import VehicleDetails
class TruckDetails(VehicleDetails):
    def __init__(self):
        self.roadTax = 0.0

    def __init__(self,vehicleID,vehicleName,capacity,roadTax):
        self.roadTax = roadTax
        super().__init__(vehicleID,vehicleName,capacity)

    def getRoadTax(self):
        return str(self.roadTax)
    def setRoadTax(self,roadTax):
        self.roadTax = roadTax

    def __str__(self):
        return str(self.vehicleID)+'\t'+self.vehicleName+'\t'+str(self.capacity)+'\t'+\
             str(self.roadTax)+ str(self.getPD())
    
