from .observer import AbsObserver

class ForecastKPIs(AbsObserver):
    open_tickets = 0
    closed_tickets = 0

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def display(self):
        print(f'Forecasted Open tickets: {self.open_tickets}')
        print(f'Forecasted Closed tickets: {self.closed_tickets}')

    def update(self):
        self.open_tickets = self._kpis.open_tickets * 3
        self.closed_tickets = self._kpis.closed_tickets * 5
        self.display()
