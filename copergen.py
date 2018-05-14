from numpy import random, ceil
from copy import deepcopy
from tindividuo import TIndividuo


class COperGen:

    def __init__(self, prob_cruce=0.6, prob_mut=0.01):
        self.prob_cruce = prob_cruce
        self.prob_mut = prob_mut

    def obtenPoblacion(self, pob):
        self.pob = pob.pob
        self.tamPob = pob.tamPob
        self.lcrom = pob.lcrom
        self.x_min = pob.x_min
        self.x_max = pob.x_max

    def seleccion(self):
        sel_super = []
        TAM_ELITE = int(ceil(self.tamPob * 2 / 100))

        # Se selecciona la elite
        sel_elite = [0 for i in range(0, TAM_ELITE)]
        for i in range(0, self.tamPob):
            self.pob[i].elite = False
            j = 0
            while ((j < TAM_ELITE) and (self.pob[sel_elite[j]].getAptitud()
                                        >= self.pob[i].getAptitud())):
                j += 1
            if j < TAM_ELITE:
                sel_elite[j] = i

        for i in range(0, TAM_ELITE):
            self.pob[sel_elite[i]].elite = True

        # Se seleccionan tam_pob individuos para reproducirse
        # se generan números aleatorios entre 0 y 1,
        # seleccionan individuos de acueredo con su puntuación acumulada
        for i in range(0, self.tamPob):
            if self.pob[i].elite:   # ELITISMO
                sel_super.append(i)
                print("elite: {}".format(i))
            else:
                pos_super = 0
                prob = random.random_sample()
                while (prob > self.pob[pos_super].punt_acu and
                       pos_super < self.tamPob):
                    pos_super += 1
                if pos_super < self.tamPob:
                    sel_super.append(pos_super)
                else:
                    sel_super.append(pos_super - 1)

        # se genera la población intermedia
        pob_aux = [deepcopy(self.pob[i]) for i in sel_super]
        self.pob = []  # limpiamos la poblacion original
        self.pob = [deepcopy(i) for i in pob_aux]
        del pob_aux  # liberamos espacio en memoria
        print([i.aptitud for i in self.pob])
        del sel_super
        del sel_elite

    def reproduccion(self):
        num_sel_cruce = 0  # num de individuos seleccionados a cruzar
        sel_cruce = []
        # Se eligen los individuos a cruzar
        for i in range(0, self.tamPob):
            # se generan tam_pob numeros aleatorios a_i en [0, 1)
            # se eligen para el cruce los individuos de
            # las posiciones i con a_i < prob_cruce
            if random.random_sample() < self.prob_cruce:
                sel_cruce.append(i)
                num_sel_cruce += 1

        # el número de seleccionados se hace par
        if num_sel_cruce % 2 != 0:
            num_sel_cruce -= 1

        # Se cruzan los individuos elegidos en un punto al azar
        punto_cruce = int(random.random_integers(0, self.lcrom-2))
        print("Punto de cruce {}".format(punto_cruce))

        for i in range(0, num_sel_cruce, 2):
            h1 = TIndividuo(self.lcrom, self.x_min, self.x_max, self.pob[
                sel_cruce[i]].genes[0:punto_cruce] + self.pob[
                    sel_cruce[i+1]].genes[punto_cruce:self.lcrom])
            h2 = TIndividuo(self.lcrom, self.x_min, self.x_max, self.pob[
                sel_cruce[i+1]].genes[0:punto_cruce] + self.pob[
                    sel_cruce[i]].genes[punto_cruce:self.lcrom])

            # print(self.pob[sel_cruce[i]].getAptitud(), " vs ", h1.getAptitud())
            # print(self.pob[
            #    sel_cruce[i+1]].getAptitud(), " vs ", h2.getAptitud())

            if h1.getAptitud() < self.pob[sel_cruce[i]].getAptitud() or not self.pob[sel_cruce[i]].elite:
                print("aaqui me quedé")
