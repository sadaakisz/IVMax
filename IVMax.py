import numpy as np
import random
from copy import deepcopy as dc

PokemonList=[]
PokemonList.append(Pokemon("Torchic", [45, 60, 40, 70, 50, 45]))
PokemonList.append(Pokemon("Squirtle", [44, 48, 65, 50, 64, 43]))
PokemonList.append(Pokemon("Turtwig", [55, 68, 64, 45, 55, 31]))

class Pokemon():
    def __init__(self, name, stats):
        self.name=name
        self.stats=dc(stats)

def Pairs(N):
    # Retorna una lista en orden aleatoria de la segunda mitad de los individuos
    # ej: N=8 -> [7, 6, 5, 4]
    randomN=random.sample(range(int(N/2), N), int(N/2))
    pair={}
    # Puebla el diccionario con los pares
    # ej: {0: 7, 7: 0, 1: 6, 6: 1...}
    for i in range(int(N/2)):
        pair[i]=randomN[i]
        pair[randomN[i]]=i
    return pair

def Inicialization(N):
    global Subjects
    global Best
    Subjects = {}
    for i in range(N):
        Subjects[i] = np.random.choice(32,6,replace=True)
    print('---Inicialization----')
    Show(N)

#Compara la idoneidad de 2 individuos, escogiendo al de mayor idoneidad
def Selection(N):
    Pair = Pairs(N)
    print('Pair',Pair)
    for k,v in Pair.items():
        if Fitness(Subjects[k]) >= Fitness(Subjects[v]):
            Subjects[v] = Subjects[k]
    Show(N)

#Calcula idoneidad según la suma de los IVs de un individuo
def Fitness(iv_group):
    iv_sum = 0
    for i, _ in enumerate(iv_group):
        iv_sum += iv_group[i]
    return iv_sum

#Cruza a 2 individuos, asignando el punto de corte de los IVs y generando
#2 hijos
def Breed(N):
    Pair = Pairs(N)
    print('Pair:', Pair)
    item = 0
    for k,v in Pair.items():
        if item % 2 == 0:
            cut_point = random.randint(1,4) #pto de corte de 1-4 porque se tienen 6 IVs
            print('cut point',cut_point)
            Child1 = []
            Child2 = []
            Parent1 = Subjects[k]
            Parent2 = Subjects[v]
            Child1.extend(Parent1[0:cut_point])
            Child1.extend(Parent2[cut_point:])
            Child2.extend(Parent2[0:cut_point])
            Child2.extend(Parent1[cut_point:])
            Subjects[k] = Child1
            Subjects[v] = Child2
        item = item+1
    Show(N)

#Muta la mitad de individuos (50%-variable) en una posicion aleatoria con un valor entre 0-31
def Mutation(N):
    print('-----Mutation ----')
    for i in range(int(N/2)):
        ChooseSubj = random.randint(0,N-1)
        ChoosePos = random.randint(0,5)
        ChooseVal = random.randint(0, 31)
        Subjects[ChooseSubj][ChoosePos] = ChooseVal
        print('The subject {}, in the position {}, with a value of {}, was mutated'.format(ChooseSubj, ChoosePos, ChooseVal))
    Show(N)

def Show(N):
    for i in range(N):
        print(Subjects[i],'f(x)=',Fitness(Subjects[i]))

def ShowBest(N):
    index=-1
    maxFit=0
    for i in range(N):
        if maxFit<Fitness(Subjects[i]):
            maxFit=Fitness(Subjects[i])
            index=i
    print("Best Subject:",Subjects[index])
    return Subjects[index]

#def ShowStats(iv_group):


N=6
generations=5
Inicialization(N)
for i in range(generations):
    print('\nGeneration {}:'.format(i+1))
    Selection(N)
    Breed(N)
    Mutation(N)
    ShowBest(N)