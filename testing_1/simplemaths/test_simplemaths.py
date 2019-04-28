import pytest
from pytest import raises
import yaml
import os
import numpy as np
from simplemaths.simplemaths import SimpleMaths as sm


with open(os.path.join(os.path.dirname(__file__),
                       'fixtures.yml')) as fixtures_file:
    test_dict = yaml.load(fixtures_file)
    pos_test = test_dict['positive']
    neg_values = test_dict['negative']
    pos_values = pos_test['values']
    expected_parity = pos_test['parity']


class TestSimpleMaths():

    # constructor (5)
    # positive test
    def test_constructor_pos(self):
        for value in pos_values:
            sm_obj = sm(value)
            assert sm_obj.number == value

    # negative test
    def test_constructor_neg(self):
        with raises(TypeError):
            for value in neg_values:
                sm_obj = sm(value)
                
    # square and factorial (2)
    def test_square(self):
        for value in pos_values:
            sm_obj = sm(value)
            sq_test = sm.square(sm_obj)
            sq_ans = np.power(value, 2)
            assert sq_test == sq_ans

    def test_factorial(self):
        with raises(ValueError):
            for value in pos_values:
                sm_obj = sm(value)
                fac_test = sm.factorial(sm_obj)
                sq_ans = np.math.factorial(value)

    # power (2)
    def test_power(self):
        for value in pos_values:
            sm_obj = sm(value)
            cubed_test = sm.power(sm_obj)
            cubed_ans = np.power(value, 3)
            assert cubed_test == cubed_ans

    # odd_or_even (3)
    def test_odd_or_even(self):
        for i, value in enumerate(pos_values):
            sm_obj = sm(value)
            parity = sm.odd_or_even(sm_obj)
            assert parity == expected_parity[i]
    
    # square_root (4)
    def test_square_root(self):
        for value in pos_values:
            sm_obj = sm(value)
            sq_test = sm.square_root(sm_obj)
            sq_ans = pow(value,0.5)
            assert sq_test == sq_ans
