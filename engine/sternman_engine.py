from abc import ABC

class SternmanEngine(ABC):
    def __init__(self, warning_light_is_on):
        # super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        return False
