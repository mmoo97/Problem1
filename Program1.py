# Mitchell Moore
# January 26, 2019
# CS355/555-2E Probability and Statistics

import threading
from random import *


class Person:

    def __init__(self, name, male, group, hasSpouse, spouse, children):
        self.name = name
        self.male = male
        self.group = group
        self.spouse = spouse
        self.children = children
        self.hasSpouse = hasSpouse


people = []


def gen1():

    """
    generates 10,000 people for generation 1.
    :return:
    """
    men = []
    women = []

    for mDNA in range(100):

        for members in range(50):

            men.append(Person("Adam" + str(members), True, mDNA+1, False, None, None))

            women.append(Person("Eve" + str(members), False, mDNA+1, False, None, None))

    first10k = men + women

    people.append(first10k)


def nextgen(currentgen, gennum):

    marry(currentgen[gennum], maleminority(currentgen[gennum]))
    makebabies(currentgen[gennum])

    print("Generation:", str(gennum) + ",", "Population:", len(people[gennum]))


def maleminority(arr):

    count = 0

    while arr[count].male is True:
        count = count + 1

    if len(arr)/2 >= count:
        return True

    else:
        return False


def marry(gen, lessmales):

        gensize = len(gen)

        partition = 0

        while gen[partition].male is True:
            partition = partition + 1

        if len(gen) % 2 != 0 and len(gen) > 1:
            gen.remove(gen[-1])
            gensize = len(gen)

        if lessmales is True:

            for l in range(partition):

                husband = gen[l]

                wife = gen[randint(partition, gensize - 1)]

                if wife.hasSpouse is False:

                    husband.spouse = wife
                    husband.hasSpouse = True
                    wife.spouse = husband
                    wife.hasSpouse = True

                else:
                    count = partition
                    while wife.hasSpouse is True and count < len(gen):

                        wife = gen[count]
                        count = count + 1

                    husband.spouse = wife
                    husband.hasSpouse = True
                    wife.spouse = husband
                    wife.hasSpouse = True

        else:

            for l in range(partition, gensize):

                wife = gen[l]

                husband = gen[randint(0, partition)]

                if husband.hasSpouse is False:

                    wife.spouse = husband
                    wife.hasSpouse = True
                    husband.spouse = wife
                    husband.hasSpouse = True

                else:
                    count = 0
                    while husband.hasSpouse is True and count <= partition:
                        husband = gen[count]
                        count = count + 1

                    wife.spouse = husband
                    wife.hasSpouse = True
                    husband.spouse = wife
                    husband.hasSpouse = True


def makebabies(gen):

    males = []
    females = []

    for i in range(len(gen)):

        if gen[i].hasSpouse is True and gen[i].male is True:

            for t in range(famsize()):

                boy = isboy()

                if boy is True:

                    males.append(Person("Billy" + str(t + 1), True, gen[i].spouse.group, False, None, None))

                else:

                    females.append(Person("Suzie" + str(t + 1), False, gen[i].spouse.group, False, None, None))

    newgen = males + females

    people.append(newgen)


def famsize():

    randnum = randint(1, 12)

    if randnum == 1:
        return 0

    elif 3 >= randnum >= 2:
        return 1

    elif 10 >= randnum >= 4:
        return 2

    elif 11 <= randnum <= 12:
        return 3


def isboy():

    randnum = randint(1,2)

    if randnum == 1:
        return True

    else:
        return False


def death():

    people.remove(people[0])


def main():

    gen1()
    numgens = 1
    tick = 0

    while numgens < 60:

        try:

            print("...")

            nextgen(people, tick)
            numgens = numgens + 1

            tick = tick + 1
        except IndexError:
            print("Generation:", str(numgens - 1) + ",", "Population:", len(people[numgens - 1]))
            break


# for i in range(len(people)):
#
#     print(len(people))

main()


def genertioninfo(generation):

    for g in range(len(people[generation])):

        print(people[generation][g].name, people[generation][g].male, people[generation][g].group)


try:
    genertioninfo(60)
except IndexError:
    print("\n...Generation doesn't exist")


# Observations: The mDNA groups are random as far as which ones stay and don't but
# always the population decreases to zero after around 30 generations. Once the probability is changed,
# the population lasted closer to 50 generations on average.
