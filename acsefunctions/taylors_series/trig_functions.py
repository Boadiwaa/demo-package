import numpy as np


def exp(x, terms=20):
    """
    Compute e^x using Taylor series expansion.

    Parameters
    ----------
    int or float or list of integers or np.array
        x: The exponent value for e^x. Can be a scalar or a numpy array.
        terms: Number of terms in the Taylor series to consider
                (higher = more accurate).

    Returns
    -------
    np.float or np.array
        Approximate value of e^x. Can be a scalar or a numpy array.

    Examples
    --------
    >>> exp(2.0)
    array(7.3890561)

    >>> exp([1.0, 2.0, 3.0])
    array([ 2.71828183,  7.3890561 , 20.08553692])
    """
    x = np.asarray(x)
    result = np.ones_like(x)
    term = np.ones_like(x)

    for n in range(1, terms):
        term *= x / n
        result += term

    return result


def sinh(x, terms=20):
    """
    Compute sinh(x) using Taylor series expansion.

    Parameters
    ----------
    int or float or list of integers or np.array
        x: The input value for sinh(x). Can be a scalar or a numpy array.
    int
        terms: Number of terms in the Taylor series to consider
                (higher = more accurate).

    Returns
    -------
    np.float or np.array
        Approximate value of sinh(x). Can be a scalar or a numpy array.

    Examples
    --------
    >>> sinh(5,terms = 30)
    array(74.20321058)

    >>> sinh([1.0, 2.0, 3.0, 4.0, 5.0])
    array([ 1.17520119,  3.62686041, 10.01787493, 27.2899172 , 74.20321058])
    """
    x = np.asarray(x, dtype=float)
    result = np.zeros_like(x)
    term = x.copy()

    for n in range(1, terms):
        result += term
        term *= x * x / ((2 * n) * (2 * n + 1))

    return result


def cosh(x, terms=20):
    """
    Compute cosh(x) using Taylor series expansion.

    Parameters
    ----------
    int or float or list of integers or np.array
        x: The input value for cosh(x). Can be a scalar or a numpy array.
    int
        terms: Number of terms in the Taylor series to consider
                (higher = more accurate).

    Returns
    -------
    np.float or np.array
        Approximate value of cosh(x). Can be a scalar or a numpy array.

    Examples
    --------
    >>> cosh(1)
    array(1.54308063)

    >>> cosh([1.0, 2.0, 3.0, 4.0, 5.0])
    array([ 1.54308063,  3.76219569, 10.067662  , 27.30823284, 74.20994852])
    """
    x = np.asarray(x, dtype=float)
    result = np.ones_like(x)
    term = np.ones_like(x)

    for n in range(1, terms):
        term *= x * x / ((2 * n - 1) * (2 * n))
        result += term

    return result


def tanh(x, terms=20):
    """
    Compute tanh(x) using Taylor series expansion by
    dividing sinh(x) by cosh(x).

    Parameters
    ----------
    int or float or list of integers or np.array
        x: The input value for tanh(x). Can be a scalar or a numpy array.
    int
        terms: Number of terms in the Taylor series for sinh(x) and cosh(x)
                to consider (higher = more accurate).

    Returns
    -------
    np.float or np.array
        Approximate value of tanh(x). Can be a scalar or a numpy array.

    Examples
    --------
    >>> tanh(1)
    np.float64(0.7615941559557649)

    >>> tanh([1.0, 2.0, 3.0, 4.0, 5.0])
    array([0.76159416, 0.96402758, 0.99505475, 0.9993293 , 0.9999092 ])
    """
    x = np.asarray(x, dtype=float)
    sinh_x = sinh(x, terms)
    cosh_x = cosh(x, terms)

    return sinh_x / cosh_x

# NB: ChatGPT was used to assist in providing array-compatible
# versions of these functions


if __name__ == "__main__":
    import doctest
    doctest.testmod()
