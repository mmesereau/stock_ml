from django.test import TestCase
from .constructor import percent_gain
from .algorithms import percent_change_regressor

# Create your tests here.

class constructor(TestCase):
    def setUp(self):
        results = percent_gain("MSFT")

    def test_percent_gain(self):
        results = percent_gain("MSFT")
        self.assertIsNotNone(results)

    def test_percent_change_model(self):
        rsquared = percent_change_regressor.perceptron_regressor("MSFT")
        print(rsquared)
        self.assertIsNotNone(rsquared)
