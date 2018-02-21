"""The Simulation class holds all simulation parameters."""

import numpy as np


class Simulation:

    def __init__(self, dt, duration, jd0):
        self.__mu = np.float64(398600.4418e9)  # [m^3/s^2] GM_Earth
        self.dt = dt
        self.duration = duration
        self.t = 0
        self.jd = jd0

    def step(self, spacecraft):
        self.t += self.dt
        spacecraft.update_forces()
        print(self.t)

    @property
    def mu(self):
        return self.__mu
