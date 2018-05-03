from numpy import random
from math import exp, cos, pi


class TIndividuo:
    """tipo individuo que contrandrá las características para realizar las
    operaciones genéticas. Cada individuo será el encargado de autoevaluarse,
    de acuerdo a la función objetivo"""

    def __init__(self, lcrom, x_min, x_max, genes=[]):
        """ Constructor de la clase individuo.
        :param lcrom: el tamaño del cromosoma a ser decodificado
        :param x_min: el límite inferior del rango a ser evaluado
        :param x_max: el límite superior del rango a ser evaluado
        :param genes: (opcional) cadena de bits (genes) del individuo
        :returns: nothing"""
        self.lcrom = lcrom
        self.x_min = x_min
        self.x_max = x_max

        if genes:
            self.genes = genes  # cadena de bits (genotipo)
            self._adaptacion()
        else:
                self._genera_indiv()
        self.elite = False      # indicativo de pertenecer a la elite

    def _genera_indiv(self):
        self.genes = [1 if random.random_sample() < 0.5 else 0
                      for x in range(0, self.lcrom)]
        self._adaptacion()

    def _adaptacion(self):
        self.x = float(self.x_min
                       + int(''.join(str(e) for e in self.genes), base=2)
                       * ((self.x_max - self.x_min)/(2 ** self.lcrom
                                                     - self.x_min)))
        f = 20 + exp(1) - 20 * (exp(-0.2 * abs(self.x)))
        - exp(cos(2 * pi * self.x))
        print(f)


ind = TIndividuo(25, 0, 32,)

print(ind.genes)
