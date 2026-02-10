from bean.VehicleDetails import VehicleDetails
class AirCargoDetails(VehicleDetails):
    def __init__(self):
        self.airForce = 0.0

    def __init__(self,vehicleID,vehicleName,capacity,airForce):
        self.airForce = airForce
        super().__init__(vehicleID,vehicleName,capacity)

    def getairForce(self):
        return str(self.airForce)
    def setairForce(self,airForce):
        self.airForce = airForce

    def __str__(self):
        return str(self.vehicleID)+'\t'+self.vehicleName+'\t'+str(self.capacity)+'\t'+\
             str(self.airForce)+ str(self.getPD())
