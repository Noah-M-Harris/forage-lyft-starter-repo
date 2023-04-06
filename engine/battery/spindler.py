from datetime import datetime
from abc import ABC

class Spindler(ABC):
    def __init__(self, last_service_date, current_date):
        self.update(last_service_date, current_date)

    def update(self, last, curr):
        self.last = last
        self.curr = curr

    def needs_service(self):
        self.update(self.last, datetime.today().date())
        service_threshold_date = self.last.replace(year=self.last + 2)
        
        if service_threshold_date < self.last:
            return True
        return False