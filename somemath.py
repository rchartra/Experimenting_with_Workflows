import numpy as np
import pandas as pd

def power(x, p):
    return x ** p

def evens(start, end):
    first = np.arange(start, end)
    return first[first % 2 == 0]

class MyClass():
    def __init__(self):
        self.note = "I am a class!"