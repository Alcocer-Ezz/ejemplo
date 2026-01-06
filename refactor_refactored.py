from typing import Iterable, Union


def _iter_values(data: Iterable) -> Iterable[int]:
    for item in data:
        if isinstance(item, (list, tuple)):
            for sub in item:
                yield sub
        else:
            yield item


def sumar_elementos(data: Iterable[Union[int, str, list, tuple]]) -> int:
    """Suma los elementos convertibles a entero en `data`.

    - Acepta listas/tuplas con elementos simples o niveles anidados de profundidad 1.
    - Ignora valores no convertibles en lugar de lanzar excepciones.

    Args:
        data: Iterable que contiene enteros, strings numéricos o sublistas/tuplas.

    Returns:
        Suma entera de los valores convertibles.
    """
    if data is None:
        return 0
    total = 0
    for val in _iter_values(data):
        try:
            total += int(val)
        except (TypeError, ValueError):
            continue
    return total


if __name__ == "__main__":
    ejemplo = [1, "2", [3, "x", 4], (5,)]
    print("Suma (refactorizada):", sumar_elementos(ejemplo))
