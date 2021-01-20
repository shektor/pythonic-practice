from abc import ABCMeta, abstractmethod

class AbsCommand(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass
