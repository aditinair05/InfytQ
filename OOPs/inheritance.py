class Rider:
    def __init__(self,trained_status,experience):
        self.__trained_status = trained_status
        self.__experience = experience
    
    def rides_vehicle(self):   
        pass
    
        
class BikeRider(Rider):
    def __init__(self, trained_status,experience,race_license):
        super().__init__(trained_status,experience)
        self.__race_license = race_license
    
    def rides_in_dome(self):
        pass

class CycleRider(Rider):
    def rides_blindfolded(self):
        pass
    
    
    
    
    
    
    
    
    
    
    
    
