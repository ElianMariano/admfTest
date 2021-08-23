if __name__ == "__main__":
    from utils import *

    if 2 != 2:
        raise ValueError("Valor Presente Incorreto!")
    elif 3 != 3:
        raise ValueError("Valor Futuro Incorreto!")

    import doctest
    doctest.testmod()