
class PhoneBuildDirector():

    def __init__(self, phone_builder):
        self._phone = phone_builder

    def build_phone(self):
        self._phone.new_phone()
        self._phone.assemble_handset()
        self._phone.get_phone_plan()
        self._phone.insert_sim_card()
    
    def get_phone(self):
        return self._phone.get_phone()
