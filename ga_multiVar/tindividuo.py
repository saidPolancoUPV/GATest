import numpy as np
from funTest import fun1 as f


class TIndividuo:
    """tipo individuo que contrandrá las características para realizar las
    operaciones genéticas. Cada individuo será el encargado de autoevaluarse,
    de acuerdo a la función objetivo"""

    def __init__(self, lcrom, x_min, x_max, nvar, genes=[]):
        """ Constructor de la clase individuo.
        :param lcrom: el tamaño del cromosoma a ser decodificado
        :param x_min: el límite inferior del rango a ser evaluado
        :param x_max: el límite superior del rango a ser evaluado
        :param genes: (opcional) cadena de bits (genes) del individuo
        :returns: nothing"""
        self.lcrom = lcrom
        self.x_min = x_min
        self.x_max = x_max
        self.nvar = nvar

        if genes:
            self.genes = genes  # cadena de bits (genotipo)
        else:
            self._genera_indiv()
        self.elite = False      # indicativo de pertenecer a la elite
        self.aptitud = self._adaptacion()

    def _genera_indiv(self):
        self.genes = [[1 if np.random.random_sample() < 0.5 else 0
                      for x in range(0, self.lcrom)] for y in range(0,
                                                                    self.nvar)]

    def _adaptacion(self):
        self.x = [self._decod(i) for i in self.genes]

        r = f(self.x)

        return r

    def _decod(self, gen):
        return float(self.x_min
                     + int(''.join(str(e) for e in gen), base=2)
                     * ((self.x_max - self.x_min)/(2 ** self.lcrom - 1)))

    def getAptitud(self, ban=False):
        if not hasattr(self, 'aptitud') or ban:
            self.aptitud = self._adaptacion()
        return self.aptitud


if __name__ == '__main__':
    i2 = TIndividuo(15, -40.0, 40.0, 2, [[0, 1, 1, 1, 1, 1, 1, 1, 1,
                                          1, 1, 1, 1, 1, 1],
                                        [0, 1, 1, 1, 1, 1, 1, 1, 1,
                                         1, 1, 1, 1, 1, 1]])
    i = TIndividuo(15, -40.0, 40.0, 2)
    print(i.x)
    print(i.aptitud)
    print(i2.x)
    print(i2.aptitud)
