import motor
import simulate
from time import sleep

motor = motor.moons_stepper("STM17S-3RN", "0403", "6001", "TESTA", True)

simulate = simulate.moons_stepper_simulate(motor, 0, "http://localhost:3002")

motor.connect()
simulate.connect()

motor.start_jog("", 1)

sleep(5)

motor.stop_jog()
motor
