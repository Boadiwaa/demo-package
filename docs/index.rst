My Package of Trigonometric and Bessel Functions
*************************************************

acsefunctions
==============

This package consists of 2 modules: taylors_series and bessel_group used for trigonometric 
and Bessel functions respectively, for use on :obj:`scalar and numpy array` objects.
The trigonometric functions were created using Taylors series. [1]_ The Bessel function was implemented based on Euler's definition. [2]_

For examples see :func:`acsefunctions.taylors_series.trig_functions.exp()` and :func:`acsefunctions.taylors_series.trig_functions.sinh()` for more information.

**Functions in the taylors_series module:**
--------------------------------------------------------

.. automodule:: acsefunctions.taylors_series
  :members: trig_functions

.. automodule:: acsefunctions.taylors_series.trig_functions
   :members: exp, sinh, cosh, tanh

**Functions in the bessel_group module:**
------------------------------------------------------
.. automodule:: acsefunctions.bessel_group.bessel_function
   :members: factorial, gamma_function, bessel

.. rubric::
.. [1] https://mathworld.wolfram.com/TaylorSeries.html
.. [2] https://mathworld.wolfram.com/BesselFunctionoftheFirstKind.html

.. toctree::
   :maxdepth: 2
   :caption: Contents:

