from abc import ABC

class Carrigan(ABC):
    
    def __init__(self, wear_arr=[0] * 4):
        self.wear = wear_arr

    def needs_service(self):
        count = 0
        for num in self.wear:
            if num >= 0.9:
                count += 1
        
        return count >= 1