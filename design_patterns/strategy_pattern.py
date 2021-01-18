class Order():
    def __init__(self, weight):
        self._weight = weight
    
    @property
    def weight(self):
        return self._weight

# Context

class ShippingCost():
    def __init__(self, strategy):
        self._strategy = strategy
    
    def calculate(self, order):
        return self._strategy.calculate_cost(order)

# Strategy Interface

from abc import ABCMeta, abstractmethod

class AbsStrategy(metaclass=ABCMeta):
    
    @abstractmethod
    def calculate_cost(self, order):
        """Calculate the shipping cost."""

# Concrete strategies

class FedExStrategy(AbsStrategy):
    def calculate_cost(self, order):
        return order.weight * 3


class UPSStrategy(AbsStrategy):
    def calculate_cost(self, order):
        return order.weight * 4


if __name__ == '__main__':
    order = Order(weight=2)
    strategy = UPSStrategy()
    shipping_cost = ShippingCost(strategy)
    cost = shipping_cost.calculate(order)

    print(f'{cost}')
