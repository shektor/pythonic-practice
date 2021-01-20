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

    def update(self, values):
        self.open_tickets = values[0] * 3
        self.closed_tickets = values[1] * 5
        self.display()
