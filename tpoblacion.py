from tindividuo import TIndividuo
import numpy as np
import matplotlib as plt


class TPoblacion:

    def __init__(self, tamPob, lcrom, x_min, x_max):
        self.pob = [TIndividuo(lcrom, x_min, x_max) for i in range(0, tamPob)]

        for i in self.pob:
            print(i.getAptitud())

tp = TPoblacion(10, 15, 0, 32)
