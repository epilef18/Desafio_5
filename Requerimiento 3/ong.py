import math


def factorial(fact):
    return math.factorial(fact)


def productoria(prod):
    return math.prod(prod)


def calcular(**data):

    for key, value in data.items():
        if "fact" in key:
            True
            fact = factorial(value)
            print("El factorial de {}  es {}".format(value, fact))

    for key, value in data.items():
        if "prod" in key:
            True
            prod = productoria(value)
            print("La productoria de {} es {}".format(value, prod))


calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
