from typing    import Callable, TypeVar

from matroids.core.set_operator import powset

import matroids.construct.independent_sets as independent_sets
import matroids.construct.circuits as circuits

T = TypeVar('T')


def from_independent_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by independent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        Callable[set[T], int]: The rank function of a given matroid.
    """
    E, Is = matroid
    # r(X) = max{|I|: I ∈ Is, I ⊆ X}, ∀X ⊆ E.
    return lambda X: max(map(len, (I for I in Is if I <= X)))


def from_dependent_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by dependent sets.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_dependent_matroid(matroid)))


def from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by bases.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by bases.

    Returns:
        Callable[[set[T]], int]: A rank function of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_bases_matroid(matroid)))


def from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_circuits_matroid(matroid)))


def from_nulity_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by a nulity function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]]): A matroid defined by a nulity function.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, n = matroid
    # r(X) = |X| - n(X), ∀X ⊆ E.
    return lambda X: len(X) - n(X)


def from_closure_matroid(matroid: tuple[set[T], Callable[[set[T]], set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by a closure function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]]): A matroid defined by a closure function.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, cl = matroid
    # r(X) = min{ |I| : X ⊆ cl(I) }, ∀X ⊆ E.
    return lambda X: min(len(I) for I in powset(E) if X <= cl(I))


def from_flats_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_flats_matroid(matroid)))


def from_open_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by open sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by open sets.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_open_matroid(matroid)))


def from_hyperplanes_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by hyperplanes.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by hyperplanes.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_hyperplanes_matroid(matroid)))


def from_spanning_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by spanning sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by spanning sets.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_spanning_matroid(matroid)))