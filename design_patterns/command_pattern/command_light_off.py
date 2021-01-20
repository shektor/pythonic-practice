from abc_command import AbsCommand

class LightOff(AbsCommand):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.off()
    
    def undo(self):
        self._light.on()
