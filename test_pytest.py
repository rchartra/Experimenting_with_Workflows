import pytest
import numpy as np
import somemath
from simpleapp import HomeScreen

def test_power():
    assert somemath.power(2, 3) == 8

def test_evens():
    assert somemath.evens(1,9)[1] == 4

def test_class():
    c = somemath.MyClass()
    assert c.note == "I am a class!"

def test_note():
    home = HomeScreen()
    assert home.note == "I am a note"