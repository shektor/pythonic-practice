from abc_builder import AbsPhoneBuilder

class IPhoneBuilder(AbsPhoneBuilder):

    def assemble_handset(self):
        self._phone._make = 'iPhone'
        self._phone._model = '13'

    def get_phone_plan(self):
        self._phone._operator = 'Vodafone'
    
    def insert_sim_card(self):
        pass
