from invoker_remote_control import RemoteControl
from receiver_light import Light
from command_light_on import LightOn
from command_light_off import LightOff

remote_control = RemoteControl(
    on=LightOn(Light()),
    off=LightOff(Light())
)

remote_control.click_on()
remote_control.click_off()
