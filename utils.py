def futureValue(value, i, t):
    percent = i / 100

    return value * ((1 + percent) ** t)

def presentValue(value, i, t):
    percent = i / 100

    return value / ((1 + percent) ** t)