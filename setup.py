from setuptools import setup, find_packages

setup(
    name="moons_motor",
    version="0.1.0",
    description="A simple motor control library for the Moons stepper motor driver",
    author="miroc99",
    packages=find_packages(include=["pyserial", "python-socketio", "rich"]),
)
