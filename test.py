from moons_motor.motor import MoonsStepper, StepperModules
from time import sleep

motor_ctrl = MoonsStepper(
    StepperModules.STM17S_3RN, VID="1A86", PID="7523", SERIAL_NUM=""
)

motor_ctrl.connect()
motor_ctrl.stop_and_kill()
sleep(1)
motor_ctrl.start_jog("", 0.5)
for i in range(10):
    motor_ctrl.change_jog_speed("", 2 * i)
    motor_ctrl.get_position("@")
    sleep(0.5)
motor_ctrl.stop_and_kill()
motor_ctrl.send("EP0")
motor_ctrl.send("SP0")

motor_ctrl.get_position("@")
sleep(1)
motor_ctrl.disconnect()
