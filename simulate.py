import numpy as np
import matplotlib.pyplot as plt

def simulate(cadence=2.0/60.0/24.0, noise=0.001):
    # gosh, I should add a doc string!
    time = np.arange(-0.25, 0.25, cadence)
    flux = np.ones_like(time)
    noisy = noise*np.random.normal(0, 1, len(flux)) + flux
    return time, noisy
