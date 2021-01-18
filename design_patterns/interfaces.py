# Abstract Base Class Definition

import abc

class Phone(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def power_on(self):
        """A phone should be able to power on."""

    @abc.abstractproperty
    def power_remaining(self):
        """A phone should report the percentage of power remaining."""


# Concrete Class Implementation

class HelloMoto(Phone):

    def __init__(self):
        self._power_state = 0
        self._battery_capacity = 300
        self._battery_power = 240
    
    def power_on(self):
        self._power_state = 1

    @property
    def power_remaining(self):
        return self._battery_power / self._battery_capacity


if __name__ == '__main__':
    new_phone = HelloMoto()
    print(f'{new_phone.power_remaining}')
