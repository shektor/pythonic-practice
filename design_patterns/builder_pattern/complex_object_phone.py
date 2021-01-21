
class Phone():

    def __init__(self):
        self._make = None
        self._model = None
        self._operator = None

    def about(self):
        print(f'Make: {self._make}')
        print(f'Model: {self._model}')
        print(f'Operator: {self._operator}')
