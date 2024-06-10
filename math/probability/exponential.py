#!/usr/bin/env python3
"""
Representing Poisson distribution
"""

import math

class Exponential:
    """
    Class Poisson distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Class constructor
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Probability Mass Function for Poisson
        """
        try:
            k = int(k)
        except (ValueError, TypeError):
            return 0
        if k < 0:
            return 0
        pmf = (self.lambtha ** k * math.exp(-self.lambtha)) / math.factorial(k)
        return pmf

    def cdf(self, k):
        """
        Cumulative Distribution Function for Poisson
        """
        try:
            k = int(k)
        except (ValueError, TypeError):
            return 0
        if k < 0:
            return 0
        cdf = sum((self.lambtha ** i * math.exp(-self.lambtha)) / math.factorial(i) for i in range(k + 1))
        return cdf

# Test script
if __name__ == "__main__":
    import numpy as np

    np.random.seed(0)
    data = np.random.poisson(5., 100).tolist()
    p1 = Exponential(data)
    print('Lambtha:', p1.lambtha)
    print('PMF for k=3:', p1.pmf(3))
    print('CDF for k=3:', p1.cdf(3))

    p2 = Exponential(lambtha=5)
    print('Lambtha:', p2.lambtha)
    print('PMF for k=3:', p2.pmf(3))
    print('CDF for k=3:', p2.cdf(3))
