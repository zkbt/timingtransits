import numpy as np
import matplotlib.pyplot as plt

def simulate(cadence=2.0/60.0/24.0, noise=0.001):
    time = np.arange(-0.25, 0.25, cadence)
    