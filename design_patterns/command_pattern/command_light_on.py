from abc_command import AbsCommand

class LightOn(AbsCommand):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.on()
    
    def undo(self):
        self._light.off()
