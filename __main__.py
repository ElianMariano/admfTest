if __name__ == "__main__":
    import doctest
    from utils import *
    from valor_futuro import *
    from valor_presente import *
    from random import randint

    driver_path = "C:\\Users\\Elian Mariano\\Documents\\Projetos Git\\chromedriver"

    # Cria a instancia das classes
    presente = PresentValue(driver_path=driver_path)
    futuro = FutureValue(driver_path=driver_path)

    # Valores a serem calculados para o valor presente
    pValor, pTaxa, pPeriodo = randint(1, 40000), randint(1, 100), randint(1, 100)

    # Valores a serem calculados para o valor futuro
    fValor, fTaxa, fPeriodo = randint(1, 40000), randint(1, 100), randint(1, 100)

    # Armazena os valores a serem comparados
    p1, p2 = str(presente.calculate(pValor, pTaxa, pPeriodo)), "{:.2f}".format(presentValue(pValor, pTaxa, pPeriodo))
    f1, f2 = str(futuro.calculate(fValor, fTaxa, fPeriodo)), "{:.2f}".format(futureValue(fValor, fTaxa, fPeriodo))

    if p1 != p2:
        raise ValueError("Valor Presente Incorreto! (Valor Futuro: %d, Taxa: %d, Periodo: %d)" % (pValor, pTaxa, pPeriodo))
    elif f1 != f2:
        raise ValueError("Valor Futuro Incorreto! (Valor Presente: %d, Taxa: %d, Periodo: %d)" % (fValor, fTaxa, fPeriodo))

    doctest.testmod()

    print("Executado com Sucesso!")