import pytest
import numpy as np
import somemath
import simple_app

def test_power():
    assert somemath.power(2, 3) == 8

def test_evens():
    assert somemath.evens(1,9)[1] == 4

def test_note():
    home = simple_app.HomeScreen()
    assert home.note == "I am a note"