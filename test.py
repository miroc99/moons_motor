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


def check_status(response):
    global homed
    print("Checking status...")
    result = MoonsStepper.process_response(response=response)
    print(f"Status check result: {result["value"]}")
    print("=========Status========")
    print(MoonsStepper.decode_status(status_code=result["value"]))


def status_callback(x):
    result = MoonsStepper.process_response(response=x)
    print(f"Status callback received: {result}")
    address = result["address"]
    command = result["command"]
    value = result["value"]
    print(f"Status callback: Address: {address}, Command: {command}, Value: {value}")


# motor_ctrl.home(motor_address="@", onComplete=homing_callback)
# while not homed:
#     sleep(0.1)
# print("Homing completed.")
motor_ctrl.send_command(address="@", command=StepperCommand.JOG)
motor_ctrl.send_command(address="1", command=StepperCommand.JOG)
sleep(2)
motor_ctrl.get_status(
    motor_address="@", command=StepperCommand.REQUEST_STATUS, callback=check_status
)
motor_ctrl.get_status(
    motor_address="1", command=StepperCommand.REQUEST_STATUS, callback=check_status
)
sleep(3)
motor_ctrl.disconnect()
