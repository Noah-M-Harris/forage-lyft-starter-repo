import unittest
from datetime import datetime

from car import carFactory


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory()
        calliope = car.create_calliope(last_service_mileage, current_mileage, last_service_date, today)
        self.assertTrue(calliope.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory()
        calliope = car.create_calliope(last_service_mileage, current_mileage, last_service_date, today)
        self.assertFalse(calliope.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = carFactory()
        calliope = car.create_calliope(last_service_mileage, current_mileage, last_service_date)
        self.assertTrue(calliope.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = carFactory()
        calliope = car.create_calliope(last_service_mileage, current_mileage, last_service_date)
        self.assertFalse(calliope.engine.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory()
        glissade = car.create_glissade(last_service_date, current_mileage, last_service_mileage, today)
        self.assertTrue(glissade.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory()
        glissade = car.create_glissade(last_service_date, current_mileage, last_service_mileage, today)
        self.assertFalse(glissade.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = carFactory()
        glissade = car.create_glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(glissade.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = carFactory()
        glissade = car.create_glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(glissade.engine.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = carFactory()
        palindrome = car.create_palindrome(warning_light_is_on, last_service_date, today)
        self.assertTrue(palindrome.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        car = carFactory()
        palindrome = car.create_palindrome(warning_light_is_on, last_service_date, today)
        self.assertFalse(palindrome.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = carFactory()
        palindrome = car.create_palindrome(warning_light_is_on, last_service_date)
        self.assertTrue(palindrome.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = carFactory()
        palindrome = car.create_palindrome(warning_light_is_on, last_service_date)
        self.assertFalse(palindrome.engine.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory()
        rorschach = car.create_rorschach(last_service_date, current_mileage, last_service_mileage, today)
        self.assertTrue(rorschach.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory()
        rorschach = car.create_rorschach(last_service_date, current_mileage, last_service_mileage, today)
        self.assertFalse(rorschach.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = carFactory()
        rorschach = car.create_rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(rorschach.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = carFactory()
        rorschach = car.create_rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(rorschach.engine.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory()
        thovex = car.create_thovex(last_service_date, current_mileage, last_service_mileage, today)
        self.assertTrue(thovex.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory()
        thovex = car.create_thovex(last_service_date, current_mileage, last_service_mileage, today)
        self.assertFalse(thovex.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = carFactory()
        thovex = car.create_thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(thovex.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = carFactory()
        thovex = car.create_thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(thovex.engine.needs_service())


if __name__ == '__main__':
    unittest.main()
