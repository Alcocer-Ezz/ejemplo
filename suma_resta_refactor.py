"""Versión refactorizada: funciones para sumar y restar.

Este módulo define funciones `add` y `subtract` y una función `main`
que solicita los números al usuario y muestra los resultados.
"""

def add(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def subtract(a, b):
    """Devuelve la resta de a menos b."""
    return a - b


def get_numbers():
    """Pide dos números al usuario y devuelve una tupla (a, b).

    Lanza ValueError si la entrada no es numérica.
    """
    a = float(input('Ingrese el primer número: '))
    b = float(input('Ingrese el segundo número: '))
    return a, b


def main():
    try:
        a, b = get_numbers()
    except ValueError:
        print('Entrada inválida: por favor ingrese números.')
        return

    print('Suma:', add(a, b))
    print('Resta:', subtract(a, b))


if __name__ == '__main__':
    main()
