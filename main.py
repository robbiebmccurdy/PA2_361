import numpy as NP
from threading import Thread
from numpy import random

print("This program runs adding and subtracting of two arrays on two different threads. \n")


def addVectors(A, B):
    print("Original Array A: ", A, "\n", "Original Array B: ", B, "\n")
    addRes = NP.add(A, B)
    print("Result of Addition of A and B: ", addRes, " \n")


def subVectors(A, B):
    print("Original Array A: ", A, "\n", "Original Array B: ", B, "\n")
    subRes = NP.subtract(A, B)
    print("Result of Subtraction of A and B: ", subRes, " \n")


x = random.randint(100, size=5)
y = random.randint(100, size=5)

t1 = Thread(target=addVectors, args=(x, y))
t2 = Thread(target=subVectors, args=(x, y))

t1.start()
t2.start()

t1.join()
t2.join()
