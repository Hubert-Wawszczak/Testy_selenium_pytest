
def oblicz_sqrt(liczba):
    if liczba < 0:
        raise ValueError("Nie można obliczyć pierwiastka kwadratowego z liczby ujemnej.")
    return liczba ** 0.5
