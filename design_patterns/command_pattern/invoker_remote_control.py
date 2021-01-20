from queue import LifoQueue

class RemoteControl():

    def __init__(self, on, off):
        self._undo_commands = LifoQueue()
        self._on = on
        self._off = off
    
    def click_on(self):
        self._on.execute()
        self._undo_commands.put(self._on)
    
    def click_off(self):
        self._off.execute()
        self._undo_commands.put(self._off)

    def undo_command(self):
        if not self._undo_commands.empty():
            self._undo_commands.get().undo()
