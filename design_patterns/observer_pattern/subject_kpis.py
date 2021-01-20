from .abc_subject import AbsSubject

class KPIs(AbsSubject):
    _open_tickets = 0
    _closed_tickets = 0

    @property
    def open_tickets(self):
        return self._open_tickets

    @property
    def closed_tickets(self):
        return self._closed_tickets

    def set_kpis(self, open_tickets, closed_tickets):
        self._open_tickets = open_tickets
        self._closed_tickets = closed_tickets
        self.notify(open_tickets, closed_tickets)
