import pytest
import numpy as np
import somemath

def test_power():
    assert somemath.power(2, 3) == 8

def test_evens():
    assert somemath.evens(1,9)[1] == 4