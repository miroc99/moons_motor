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
motor_ctrl.send_command(command="IFD")


def status_callback(x):
    result = MoonsStepper.process_response(response=x)
    print(f"Status callback received: {result}")
    address = result["address"]
    command = result["command"]
    value = result["value"]
    print(f"Status callback: Address: {address}, Command: {command}, Value: {value}")


# sleep(0.1)
sleep(1)
motor_ctrl.get_status("@", StepperCommand.VOLTAGE, callback=status_callback)
motor_ctrl.get_status("@", StepperCommand.POSITION, callback=status_callback)

motor_ctrl.send_command(command=StepperCommand.MOVE_FIXED_DISTANCE, value=5000)

motor_ctrl.get_status("@", StepperCommand.JOG_SPEED, callback=status_callback)
motor_ctrl.send_command(command=StepperCommand.JOG)
motor_ctrl.get_status("@", StepperCommand.VOLTAGE, callback=status_callback)
motor_ctrl.get_status("@", StepperCommand.POSITION, callback=status_callback)
motor_ctrl.get_status("@", StepperCommand.POSITION, callback=status_callback)
motor_ctrl.get_status("@", StepperCommand.TEMPERATURE, callback=status_callback)
motor_ctrl.get_status("@", StepperCommand.JOG_SPEED, callback=status_callback)
motor_ctrl.send_command(command=StepperCommand.JOG_SPEED, value=5)
sleep(3)
motor_ctrl.get_status("@", StepperCommand.TEMPERATURE, callback=status_callback)
motor_ctrl.send_command(command=StepperCommand.STOP_JOG)
motor_ctrl.get_status("@", StepperCommand.JOG_SPEED, callback=status_callback)
motor_ctrl.send_command(command=StepperCommand.CHANGE_JOG_SPEED, value=5)
sleep(3)
motor_ctrl.disconnect()
