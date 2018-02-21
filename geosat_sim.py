import numpy as np

from simulation import Simulation
from spacecraft import Spacecraft

sim_duration = 100
sim_timestep = .1
sim_jd0 = 2.458130909965370e+06
sim = Simulation(sim_timestep, sim_duration, sim_jd0)
demosat = Spacecraft()
demosat.pos_eci = np.array([-1902.66644236, -4074.60449248, -5210.55056856]) * 1000
demosat.vel_eci = np.array([0.99741468, 5.75935542, -4.86580007]) * 1000

print(demosat.pos_eci)
print(demosat.vel_eci)




