from random import *
import random
import numpy
import copy

countCities = 20;
# 2D Array
cities = numpy.zeros(shape=(20, 20))
# tour
hypothesis = [int] * countCities
visitedCities = []
saveState = []

threshold = 2
lastFitness = 0
trials = 0
cityIndex = 1


# calculates fitness based on the difference between the distances
def getFitness(fitness, hypothesis, saveState, cities):
    oldDistance = getDistance(cities, saveState)
    print("Old Distance ", oldDistance, "km")
    print("")
    newDistance = getDistance(cities, hypothesis)
    print("New Distance ", newDistance, "km")
    print("")
    if (oldDistance > newDistance):
        fitness += 1
    elif (oldDistance < newDistance):
        fitness -= 1

    return fitness


# choose random City at position cityIndex
def doRandomStep():
    global visitedCities
    global saveState
    global hypothesis
    if (len(visitedCities) >= countCities):
        visitedCities.clear()
        visitedCities.append(0)
    randomNumbers = list(set(saveState) - set(visitedCities))
    randomStep = random.choice(randomNumbers)
    visitedCities.append(randomStep)
    hypothesis.remove(randomStep)
    hypothesis.insert(cityIndex, randomStep)


# next city
def increment():
    global cityIndex
    global visitedCities
    if (cityIndex < countCities - 2):
        cityIndex += 1
    else:
        visitedCities.clear()
        cityIndex = 1


# calculates distance from tour
def getDistance(cities, hypothesis):
    distance = 0
    for i in range(countCities):
        if (i < countCities - 1):
            distance += cities[hypothesis[i]][hypothesis[i + 1]]
            print("[", hypothesis[i], "]", distance, "km ", end="")
        else:
            print("[", hypothesis[i], "]")

    return distance


if __name__ == '__main__':

    for i in range(countCities):
        hypothesis[i] = i
        for j in range(countCities):
            if (j > i):
                cities[i][j] = randint(1, 100)
            elif (j < i):
                cities[i][j] = cities[j][i]

    print("=== START ===");
    while (lastFitness < threshold):

        print("_________________________________________________________")
        saveState = copy.deepcopy(hypothesis)
        doRandomStep()
        currentFitness = getFitness(lastFitness, hypothesis, saveState, cities)
        print("Old fitness ", lastFitness)
        print("Current fitness ", currentFitness)

        if (currentFitness > lastFitness):
            lastFitness = currentFitness
        elif (currentFitness < lastFitness):
            hypothesis = copy.deepcopy(saveState)
            if (trials < 3):
                increment()
            else:
                trials = 0
            visitedCities.append(saveState[cityIndex])
            
            
''' Output :- 
=== START ===
_________________________________________________________
[ 0 ] 75.0 km [ 1 ] 110.0 km [ 2 ] 202.0 km [ 3 ] 294.0 km [ 4 ] 361.0 km [ 5 ] 375.0 km [ 6 ] 404.0 km [ 7 ] 413.0 km [ 8 ] 502.0 km [ 9 ] 555.0 km [ 10 ] 650.0 km [ 11 ] 651.0 km [ 12 ] 736.0 km [ 13 ] 764.0 km [ 14 ] 839.0 km [ 15 ] 905.0 km [ 16 ] 966.0 km [ 17 ] 1051.0 km [ 18 ] 1101.0 km [ 19 ]
Old Distance  1101.0 km

[ 0 ] 81.0 km [ 15 ] 105.0 km [ 1 ] 140.0 km [ 2 ] 232.0 km [ 3 ] 324.0 km [ 4 ] 391.0 km [ 5 ] 405.0 km [ 6 ] 434.0 km [ 7 ] 443.0 km [ 8 ] 532.0 km [ 9 ] 585.0 km [ 10 ] 680.0 km [ 11 ] 681.0 km [ 12 ] 766.0 km [ 13 ] 794.0 km [ 14 ] 877.0 km [ 16 ] 938.0 km [ 17 ] 1023.0 km [ 18 ] 1073.0 km [ 19 ]
New Distance  1073.0 km

Old fitness  0
Current fitness  1
_________________________________________________________
[ 0 ] 81.0 km [ 15 ] 105.0 km [ 1 ] 140.0 km [ 2 ] 232.0 km [ 3 ] 324.0 km [ 4 ] 391.0 km [ 5 ] 405.0 km [ 6 ] 434.0 km [ 7 ] 443.0 km [ 8 ] 532.0 km [ 9 ] 585.0 km [ 10 ] 680.0 km [ 11 ] 681.0 km [ 12 ] 766.0 km [ 13 ] 794.0 km [ 14 ] 877.0 km [ 16 ] 938.0 km [ 17 ] 1023.0 km [ 18 ] 1073.0 km [ 19 ]
Old Distance  1073.0 km

[ 0 ] 82.0 km [ 7 ] 174.0 km [ 15 ] 198.0 km [ 1 ] 233.0 km [ 2 ] 325.0 km [ 3 ] 417.0 km [ 4 ] 484.0 km [ 5 ] 498.0 km [ 6 ] 521.0 km [ 8 ] 610.0 km [ 9 ] 663.0 km [ 10 ] 758.0 km [ 11 ] 759.0 km [ 12 ] 844.0 km [ 13 ] 872.0 km [ 14 ] 955.0 km [ 16 ] 1016.0 km [ 17 ] 1101.0 km [ 18 ] 1151.0 km [ 19 ]
New Distance  1151.0 km

Old fitness  1
Current fitness  0
_________________________________________________________
[ 0 ] 81.0 km [ 15 ] 105.0 km [ 1 ] 140.0 km [ 2 ] 232.0 km [ 3 ] 324.0 km [ 4 ] 391.0 km [ 5 ] 405.0 km [ 6 ] 434.0 km [ 7 ] 443.0 km [ 8 ] 532.0 km [ 9 ] 585.0 km [ 10 ] 680.0 km [ 11 ] 681.0 km [ 12 ] 766.0 km [ 13 ] 794.0 km [ 14 ] 877.0 km [ 16 ] 938.0 km [ 17 ] 1023.0 km [ 18 ] 1073.0 km [ 19 ]
Old Distance  1073.0 km

[ 0 ] 81.0 km [ 15 ] 137.0 km [ 6 ] 166.0 km [ 1 ] 201.0 km [ 2 ] 293.0 km [ 3 ] 385.0 km [ 4 ] 452.0 km [ 5 ] 479.0 km [ 7 ] 488.0 km [ 8 ] 577.0 km [ 9 ] 630.0 km [ 10 ] 725.0 km [ 11 ] 726.0 km [ 12 ] 811.0 km [ 13 ] 839.0 km [ 14 ] 922.0 km [ 16 ] 983.0 km [ 17 ] 1068.0 km [ 18 ] 1118.0 km [ 19 ]
New Distance  1118.0 km

Old fitness  1
Current fitness  0
_________________________________________________________
[ 0 ] 81.0 km [ 15 ] 105.0 km [ 1 ] 140.0 km [ 2 ] 232.0 km [ 3 ] 324.0 km [ 4 ] 391.0 km [ 5 ] 405.0 km [ 6 ] 434.0 km [ 7 ] 443.0 km [ 8 ] 532.0 km [ 9 ] 585.0 km [ 10 ] 680.0 km [ 11 ] 681.0 km [ 12 ] 766.0 km [ 13 ] 794.0 km [ 14 ] 877.0 km [ 16 ] 938.0 km [ 17 ] 1023.0 km [ 18 ] 1073.0 km [ 19 ]
Old Distance  1073.0 km

[ 0 ] 81.0 km [ 15 ] 105.0 km [ 1 ] 151.0 km [ 16 ] 182.0 km [ 2 ] 274.0 km [ 3 ] 366.0 km [ 4 ] 433.0 km [ 5 ] 447.0 km [ 6 ] 476.0 km [ 7 ] 485.0 km [ 8 ] 574.0 km [ 9 ] 627.0 km [ 10 ] 722.0 km [ 11 ] 723.0 km [ 12 ] 808.0 km [ 13 ] 836.0 km [ 14 ] 927.0 km [ 17 ] 1012.0 km [ 18 ] 1062.0 km [ 19 ]
New Distance  1062.0 km

Old fitness  1
Current fitness  2
'''
