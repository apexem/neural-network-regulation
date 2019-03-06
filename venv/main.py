import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import control

class DCMotor:

    def __init__(self, voltage, resistance,
                 inductance, inertia,
                 friction, electro_force,
                 torque):
        self.voltage = voltage
        self.resistance = resistance
        self.inductance = inductance
        self.inertia = inertia # moment of inertia of the rotor
        self.friction = friction # viscous friction constant
        self.electromotive_force = electromotive_force # electromotive force constant
        self.torque = torque #motor torque constant

    def create_tf(self):
        K = self.torque
        J = self.inertia
        R = self.resistance
        b = self.friction
        L = self.inductance

        nominator = [K]
        denominator = [J*L, J*R+L*b, R*b, K*K]
        self.transfer_function = control.TransferFunction(nominator, denominator)

    def plot_step_response(self):
        time_series = range(0, 1000)
        step_response = control.step_response(self.transfer_function, time_series)
        plt.plot(step_response)
        plt.show()

print("Hello World!")
motor = DCMotor(123, 54, 1, 3, 4, 10, 6)
motor.plot_step_response()

