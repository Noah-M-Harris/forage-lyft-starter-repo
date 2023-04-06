from abc import ABC, abstractmethod
from datetime import datetime


from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.battery.nubbin import Nubbin
from engine.battery.spindler import Spindler

class Car(ABC):
    def __init__(self, engine, battery):
        # self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery

    # @abstractmethod
    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        return False


class carFactory:
    def create_calliope(last_service_mileage, current_mileage, last_service_date, current_date=datetime.today().date()):
        # create battery, engine
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = Spindler(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_glissade(last_service_mileage, current_mileage, last_service_date, current_date=datetime.today().date()):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = Spindler(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_palindrome(warning_light_on, last_service_date, current_date=datetime.today().date()):
        engine = SternmanEngine(warning_light_on)
        battery = Spindler(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_rorschach(last_service_mileage, current_mileage, last_service_date, current_date=datetime.today().date()):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = Nubbin(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = Nubbin(last_service_date, current_date)
        return Car(engine, battery)