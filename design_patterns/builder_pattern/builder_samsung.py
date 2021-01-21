from abc_builder import AbsPhoneBuilder

class SamsungBuilder(AbsPhoneBuilder):

    def assemble_handset(self):
        self._phone._make = 'Samsung'
        self._phone._model = '21'

    def get_phone_plan(self):
        self._phone._operator = 'Three'
    
    def insert_sim_card(self):
        pass
