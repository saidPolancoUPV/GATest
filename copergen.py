from numpy import random, ceil
from copy import deepcopy


class COperGen:

    def obtenPoblacion(self, pob):
        self.pob = pob.pob
        self.tamPob = pob.tamPob

    def seleccion(self):
        sel_super = []
        TAM_ELITE = int(ceil(self.tamPob * 2 / 100))

        # Se selecciona la elite
        sel_elite = [0 for i in range(0,TAM_ELITE)]
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
            if self.pob[i].elite: # ELITISMO
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
        for i in pob_aux:
            print(pob_aux.genes)
