from abc import ABC

class Carrigan(ABC):
    
    def __init__(self, wear_arr=[0] * 4):
        self.wear = wear_arr

    def needs_service(self):
        return sum(self.wear) >= 3