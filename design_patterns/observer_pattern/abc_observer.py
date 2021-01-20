from abc import ABCMeta, abstractmethod

class AbsObserver(metaclass=ABCMeta):

    @abstractmethod
    def update(self, value):
        pass
