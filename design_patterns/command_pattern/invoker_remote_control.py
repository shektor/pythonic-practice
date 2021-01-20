
class RemoteControl():

    def __init__(self, on, off):
        self._on = on
        self._off = off
    
    def click_on(self):
        self._on.execute()
    
    def click_off(self):
        self._off.execute()
