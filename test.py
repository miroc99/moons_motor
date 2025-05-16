from moons_motor.motor import MoonsStepper, StepperModules, StepperCommand
from time import sleep

motor_ctrl = MoonsStepper(
    StepperModules.STM17S_3RN, VID="1A86", PID="7523", SERIAL_NUM=""
)
homed = False


def homing_callback(x):
    global homed
    print(f"Homing callback: {x}")
    homed = True


motor_ctrl.connect()
sleep(1)
motor_ctrl.send_command(command=StepperCommand.STOP_KILL)
motor_ctrl.home(onComplete=lambda x: homing_callback(x))

while not homed:
    sleep(0.01)
# # motor_ctrl.send("JS0.1")
# # motor_ctrl.send("@CJ")
# motor_ctrl.send_command(address="", command=StepperCommand.JOG)
# # sleep(1)
# for i in range(10):
#     # motor_ctrl.change_jog_speed("", 2 * i)
#     # motor_ctrl.send(f"JS{2 * i}")
#     motor_ctrl.send_command(
#         command=StepperCommand.change_jog_speed, value=1.2 * i + 0.1
#     )
#     # motor_ctrl.get_position("@", lambda x: print(f"Position: {x}"))
#     motor_ctrl.get_status(
#         "@", StepperCommand.position, callback=lambda x: print(f"Status: {x}")
#     )
#     sleep(0.5)
# motor_ctrl.send_command(command=StepperCommand.stop_kill)
# # # motor_ctrl.stop_and_kill()
# # motor_ctrl.send("SK")
# motor_ctrl.send_command(StepperCommand.encoder_position, 0)
# motor_ctrl.send_command(StepperCommand.set_position, 0)
# sleep(1)

# motor_ctrl.send_command(command=StepperCommand.POSITION)


def status_callback(x):
    result = MoonsStepper.process_response(response=x)
    address = result["address"]
    command = result["command"]
    value = result["value"]
    print(f"Status callback: Address: {address}, Command: {command}, Value: {value}")


motor_ctrl.get_status("@", StepperCommand.VOLTAGE, callback=status_callback)

sleep(1)
motor_ctrl.disconnect()
