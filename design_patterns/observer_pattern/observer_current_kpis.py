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

    def update(self, values):
        self.open_tickets, self.closed_tickets = values
        self.display()
