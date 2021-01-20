from abc import ABCMeta
from abc_observer import AbsObserver


class AbsSubject(metaclass=ABCMeta):
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer not derived from AbsObserver')
        self._observers |= {observer}  # Modify a set by union

    def detach(self, observer):
        self._observers -= {observer}  # Modify a set by difference
    
    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)
