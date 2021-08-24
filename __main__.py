import doctest
import sys
from valor_futuro import *
from valor_presente import *

driver = sys.argv[1]

# Função que testa o valor futuro
def futureValueTest(value, i, t):
    """
    Dado o valor, a taxa e o período, calcula o valor futuro

    :param: value: float
    :param: i: float
    :param: t: float
    :return: float

    >>> futureValueTest(23, 4, 12)
    36.82

    >>> futureValueTest(76, 44, 13)
    8700.13

    >>> futureValueTest(74000, 23, 35)
    103731490.95

    >>> futureValueTest(22, 5, 56)
    338.08

    >>> futureValueTest(74, 2, 64)
    262.81

    >>> futureValueTest(3246, 1.5, 23)
    4571.59

    >>> futureValueTest(2334, 34, 43)
    681721799.01

    >>> futureValueTest(956, 21, 45)
    5079249.62

    >>> futureValueTest(742, 14, 32)
    49131.4

    >>> futureValueTest(745, 25, 3)
    1455.08

    >>> futureValueTest(621, 41, 26)
    4707480.49

    >>> futureValueTest(6246, 35, 14)
    417133.18
    """

    futuro = FutureValue(driver_path=driver)
    return futuro.calculate(value, i, t)

# Função que testa o valor presente
def presentValueTest(value, i, t):
    """
    Dado o valor, a taxa e o período, calcula o valor presente

    :param: value: float
    :param: i: float
    :param: t: float
    :return: float

    >>> presentValueTest(20, 3, 10)
    14.88

    >>> presentValueTest(85, 40, 15)
    0.55

    >>> presentValueTest(74000, 12, 24)
    4875.28

    >>> presentValueTest(22, 5, 8)
    14.89

    >>> presentValueTest(54, 23, 2)
    35.69

    >>> presentValueTest(3246, 11, 23)
    294.39

    >>> presentValueTest(84, 9, 14)
    25.14

    >>> presentValueTest(956, 21, 45)
    0.18

    >>> presentValueTest(742, 14, 32)
    11.21

    >>> presentValueTest(745, 25, 3)
    381.44

    >>> presentValueTest(621, 41, 26)
    0.08

    >>> presentValueTest(6246, 35, 14)
    93.53
    """

    presente = PresentValue(driver_path=driver)
    return presente.calculate(value, i, t)

if __name__ == "__main__":
    doctest.testmod()