from numpy import random, ceil
from copy import deepcopy
from tindividuo import TIndividuo


class COperGen:

    def __init__(self, prob_cruce=0.7, prob_mut=0.01):
        self.prob_cruce = prob_cruce
        self.prob_mut = prob_mut

    def obtenPoblacion(self, pob):
        self.pob = pob.pob
        self.tamPob = pob.tamPob
        self.lcrom = pob.lcrom
        self.x_min = pob.x_min
        self.x_max = pob.x_max
        self.nvar = pob.nvar

    def seleccion(self):
        sel_super = []
        TAM_ELITE = int(ceil(self.tamPob * 2 / 100))
        indASel = self.tamPob

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

        for i in range(0, indASel):
            ind1 = random.randint(0, self.tamPob)
            ind2 = random.randint(0, self.tamPob)

            sel_super.append(ind1 if self.pob[ind1].aptitud
                             > self.pob[ind2].aptitud
                             and not self.pob[ind2].elite else ind2)

        # se genera la población intermedia
        pob_aux = [deepcopy(self.pob[i]) for i in sel_super]
        self.pob = []  # limpiamos la poblacion original
        self.pob = [deepcopy(i) for i in pob_aux]
        del pob_aux  # liberamos espacio en memoria
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
        # punto_cruce = int(random.random_integers(0, self.lcrom-2))
        # print("Punto de cruce {}".format(punto_cruce))

        for i in range(0, num_sel_cruce, 2):
            i1, i2 = self.cruza(self.pob[i].genes, self.pob[i+1].genes)

            h1 = TIndividuo(self.lcrom, self.x_min, self.x_max, self.nvar, i1)
            h2 = TIndividuo(self.lcrom, self.x_min, self.x_max, self.nvar, i2)

            # print(self.pob[sel_cruce[i]].getAptitud(), "vs", h1.getAptitud())
            # print(self.pob[
            #    sel_cruce[i+1]].getAptitud(), " vs ", h2.getAptitud())

            if h1.getAptitud() > self.pob[
                sel_cruce[
                    i]].getAptitud() or not self.pob[sel_cruce[i]].elite:
                self.pob[sel_cruce[i]] = deepcopy(h1)

            if h2.getAptitud() > self.pob[
                sel_cruce[
                    i+1]].getAptitud() or not self.pob[sel_cruce[i+1]].elite:
                self.pob[sel_cruce[i+1]] = deepcopy(h2)
            del h1
            del h2
        del sel_cruce

    def cruza(self, p1, p2):
        if len(p1) != len(p2):
            raise TypeError("El tamaño de los idividuos no coincide")

        h1 = []
        h2 = []
        for i in range(0, self.nvar):
            punto_cruce = int(random.random_integers(0, self.lcrom-2))
            h1.append(p1[i][0:punto_cruce] + p2[i][punto_cruce:self.lcrom])
            h2.append(p2[i][0:punto_cruce] + p1[i][punto_cruce:self.lcrom])

        return h1, h2

    def mutacion(self):
        for i in self.pob:
            mutado = False
            for j in range(0, self.nvar):
                for k in range(0, self.lcrom):
                    if random.random_sample() < self.prob_mut and not i.elite:
                        i.genes[j][k] = 0 if i.genes[j][k] == 1 else 1
                        mutado = True
            if mutado:
                i.getAptitud(True)

    def showPob(self):
        print('*'*20)
        for i in self.pob:
            print(i.getAptitud())
