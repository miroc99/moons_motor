from moons_motor.motor import MoonsStepper, StepperModules
from moons_motor.simulate import MoonsStepperSimulate
from time import sleep

motor = MoonsStepper(StepperModules.STM17S_3RN, "0403", "6001", "TESTA", False)

simulate = MoonsStepperSimulate(motor, 0, "http://localhost:3002")

MoonsStepper.list_all_ports()
motor.connect()
simulate.connect()

motor.start_jog("", 10)

sleep(5)

motor.stop_jog()
