from abc import ABC

from homework_02 import exceptions


class Vehicle(ABC):
    default_weight = 1000
    default_fuel = 10
    default_fuel_consumption = 25

    def __init__(self, weight, fuel, fuel_consumption, started=False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if self.fuel > 0:
            self.started = True
        else:
            raise exceptions.LowFuelError

    def move(self, distance):
        expected_fuel = self.fuel - distance * self.fuel_consumption
        self.fuel = expected_fuel
        if self.fuel < self.fuel_consumption:
            raise exceptions.NotEnoughFuel
