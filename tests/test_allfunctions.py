import numpy as np
from taylors_series.trig_functions import exp, sinh, cosh, tanh
from bessel_group.bessel_function import factorial, gamma_function, bessel


class TestTrigFunctions:
    def test_exp_scalar(self):
        x_value = 10.0
        result = exp(x_value, terms=30)
        expected = np.exp(x_value)
        assert np.allclose(result, expected)

    def test_exp_array(self):
        x_value = [1.0, 2.0, 3.0]
        result = exp(x_value)
        expected = np.array([2.71828183, 7.3890561, 20.08553692])
        assert np.allclose(result, expected)

    def test_sinh_scalar(self):
        x_value = 30.0
        result = sinh(x_value, terms=3000)
        expected = np.sinh(x_value)
        assert np.allclose(result, expected)

    def test_sinh_array(self):
        x_value = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        result = sinh(x_value)
        expected = np.array(
            [1.17520119, 3.62686041, 10.01787493, 27.2899172, 74.20321058]
        )
        assert np.allclose(result, expected)

    def test_cosh(self):
        x_value = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        result = cosh(x_value)
        expected = np.array(
            [1.54308063, 3.76219569, 10.067662, 27.30823284, 74.20994852]
        )
        assert np.allclose(result, expected)

    def test_tanh(self):
        x_value = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        result = tanh(x_value)
        expected = np.array([0.76159416, 0.96402758, 0.99505475,
                            0.9993293, 0.9999092])
        assert np.allclose(result, expected)


class TestBesselGroup:
    def test_factorial(self):
        x_value = [0, 1, 2, 3, 4, 5]
        result = factorial(x_value)
        expected = np.array([1.0, 1.0, 2.0, 6.0, 24.0, 120.0])
        assert np.allclose(result, expected)

    def test_gamma_function(self):
        x_value = [1, 1.5, 2, 2.5, 3, 4]
        result = gamma_function(x_value)
        expected = np.array(
            [1.05088491, 0.87972523, 0.99916542, 1.32925696,
                1.99999916, 6.00000083]
        )
        assert np.allclose(result, expected)

    def test_bessel(self):
        x_value = [0, 1, 2, 3, 4, 5]
        result = bessel(1, x_value)
        expected = np.array(
            [0.0, 0.4404682, 0.57755987, 0.34031109, -0.06437481, -0.32549533]
        )
        assert np.allclose(result, expected)
