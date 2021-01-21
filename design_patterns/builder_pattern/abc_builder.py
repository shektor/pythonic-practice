from abc import ABCMeta, abstractmethod

from complex_object_phone import Phone

class AbsPhoneBuilder(metaclass=ABCMeta):

    def new_phone(self):
        self._phone = Phone()

    def get_phone(self):
        return self._phone

    @abstractmethod
    def assemble_handset(self):
        pass

    @abstractmethod
    def get_phone_plan(self):
        pass

    @abstractmethod
    def insert_sim_card(self):
        pass
