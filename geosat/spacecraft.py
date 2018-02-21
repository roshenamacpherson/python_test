"""The Spacecraft class defines a full spacecraft.
It includes all mass properties, as well as sensors,
actuators, controllers, filters, etc."""
import numpy as np


class Spacecraft:
    def __init__(self):
        self.mass = 0
        self.forces = np.zeros((3, 1))
        self.pos_eci = np.zeros((3, 1))
        self.vel_eci = np.zeros((3, 1))

    def update_forces(self):
        self.forces = np.zeros((3, 1))


