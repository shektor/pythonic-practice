from .observer import AbsObserver

class CurrentKPIs(AbsObserver):
    open_tickets = 0
    closed_tickets = 0

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def display(self):
        print(f'Open tickets: {self.open_tickets}')
        print(f'Closed tickets: {self.closed_tickets}')

    def update(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.display()
