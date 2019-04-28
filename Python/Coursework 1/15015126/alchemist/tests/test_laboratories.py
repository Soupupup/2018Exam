# importing the necessary modules for testing and the code that is the
# subject of testing
from ..laboratory import Laboratory
import yaml
import unittest
import os

# loading the fixtures file that will be the input to the code
with open(os.path.join(os.path.dirname(__file__),
                       'fixtures.yml')) as fixtures_file:
    test_dict = yaml.load(fixtures_file)
    # setting up the shelves
    test_lower = test_dict['two_shelf']['lower']
    test_upper = test_dict['two_shelf']['upper']
    # running the experiment with the shelves
    test_lab = Laboratory(test_lower, test_upper)


# begin unit tests
class TestStringMethods(unittest.TestCase):

    # testing whether two reactable products can be reacted in the function
    def test_can_react(self):
        assert Laboratory.can_react("A", "antiA")

    # testing whether code correctly indicate the two unreactable products can't
    # react together
    def test_cannot_react(self):
        assert not Laboratory.can_react("A", "antiB")

    # testing if code works for antiantiproducts
    def test_antianti(self):
        assert Laboratory.can_react("antiB", "antiantiB")

    # testing if after one reaction, the states of shelves are correct
    def test_do_a_reactions(self):
        # extracting the expected states of the shelves after one reaction
        lower_react = test_dict['lower_react']
        upper_react1 = test_dict['upper_react1']
        upper_react2 = test_dict['upper_react2']

        new_lower, new_upper = Laboratory.do_a_reaction(
            test_lab, test_lower, test_upper)
        with self.subTest():
            assert new_lower == lower_react
        with self.subTest():
            # testing both possible scenarios
            assert new_upper == upper_react1 or new_upper == upper_react2

    # testing if after a full experiment, the states of shelves are correct
    def test_run_full_experiment(self):
        # extracting the expected states of the shelves after full experiment
        lower_expect = test_dict['lower_final']
        upper_expect1 = test_dict['upper_final1']
        upper_expect2 = test_dict['upper_final2']

        final_lower, final_upper = test_lab.run_full_experiment()
        with self.subTest():
            # testing both possible scenarios
            assert final_upper == upper_expect1 or final_upper == upper_expect2
        with self.subTest():
            assert final_lower == lower_expect

    # testing if the number of reactions are correctly counted
    def test_reaction_count(self):

        count_expect = test_dict['totalcount']  # the expected value
        count_test = test_lab.run_full_experiment(True) # the output count
        assert count_expect[0] == count_test

