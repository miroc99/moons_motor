from moons_motor.motor import MoonsStepper, StepperModules, StepperCommand
from moons_motor.simulate import MoonsStepperSimulate
from time import sleep

motor = MoonsStepper(StepperModules.STM17S_3RN, "1A86", "7523", "", False)


# simulate = MoonsStepperSimulate(motor, 0, "http://localhost:3002")
def progressCallback(progress):
    print(f"Progress: {progress * 100}%")


def check_status(response):
    print("Checking status...")
    result = MoonsStepper.process_response(response=response)
    print(f"Status check result: {result["value"]}")
    print("=========Status========")
    print(MoonsStepper.decode_status(status_code=result["value"]))


MoonsStepper.list_all_ports()
motor.connect()
# simulate.connect()

# motor.change_jog_speed("", 0.2)
# motor.stop_and_kill()
# motor.start_jog("", 0.2)
print(
    motor.get_status(
        motor_address="@", command=StepperCommand.REQUEST_STATUS, callback=check_status
    )
)
# print(motor.get_temperature(""))

# motor.stop_jog()
sleep(3)
motor.disconnect()
