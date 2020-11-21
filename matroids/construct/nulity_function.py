from typing    import Callable, TypeVar

from matroids.core.set_operator import powset
from matroids.construct import independent_sets

T = TypeVar('T')

def from_independent_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a nulity function from a matroid defined by independent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets

    Returns:
        Callable[[set[T]], int]: The nulity function of a given matroid.
    """
    _, Is = matroid
    # n(X) = |X| - max{|I|: I ∈ Is, I ⊆ X}, ∀X ⊆ E.
    return lambda X: len(X) - max(map(len, (I for I in Is if I <= X)))


def from_dependent_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a nulity function from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by dependent sets.

    Returns:
        Callable[[set[T]], int]: The nulity function of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_dependent_matroid(matroid)))


def from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a nulity function from a matroid defined by bases.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by dependent sets.

    Returns:
        Callable[[set[T]], int]: The nulity function of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_bases_matroid(matroid)))


def from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a nulity function from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        Callable[[set[T]], int]: The nulity function of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_circuits_matroid(matroid)))


def from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> Callable[[set[T]], int]:
    """Construct a nulity function from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function

    Returns:
        Callable[[set[T]], int]: The nulity function of a given matroid.
    """
    E, r = matroid
    return lambda X: len(X) - r(X)


def from_closure_matroid(matroid: tuple[set[T], Callable[[set[T]], set[T]]]) -> Callable[[set[T]], int]:
    """Construct a nulity function from a matroid defined by a closure function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]]): A matroid defined by a closure function

    Returns:
        Callable[[set[T]], int]: The nulity function of a given matroid.
    """
    E, cl = matroid
    # n(X) = |X| - min{ |I| : X ⊆ cl(I) }.
    return lambda X: len(X) - min(len(I) for I in powset(E) if X <= cl(I))


def from_flats_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a nulity function from a matroid defined by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        Callable[[set[T]], int]: The nulity function of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_flats_matroid(matroid)))


def from_open_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a nulity function from a matroid defined by open sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by open sets.

    Returns:
        Callable[[set[T]], int]: The nulity function of a matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_open_matroid(matroid)))


def from_hyperplanes_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a nulity function from a matroid defined by hyperplanes

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by hyperplanes

    Returns:
        Callable[[set[T]], int]: The nulity function of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_hyperplanes_matroid(matroid)))


def from_spanning_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a nulity function from a matroid defined by spanning sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by spanning sets.

    Returns:
        Callable[[set[T]], int]: The nulity function of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_spanning_matroid(matroid)))