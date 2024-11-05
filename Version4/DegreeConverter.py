import numpy as np
from numpy.polynomial.polynomial import Polynomial


class DegreeConverter:
    def __init__(self):
        angles = np.array([0, 30, 45, 60, 90])
        measures = np.array([1023, ])
        self.p = Polynomial.fit(measures, angles)

    def calculate(self, bit_value: int) -> int:
        return self.p(bit_value)
    