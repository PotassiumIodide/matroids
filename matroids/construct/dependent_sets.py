from typing    import Callable, TypeVar

from matroids.core.set_operator import powset

import matroids.construct.independent_sets as independent_sets
import matroids.construct.circuits as circuits

T = TypeVar('T')


def from_independent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct dependent sets from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        list[set[T]]: The dependent sets of a given matroid.
    """
    E, Is = matroid
    # Ds = {D ⊆ E : D ∉ Is}
    return [D for D in powset(E) if D not in Is]


def from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct dependent sets from a matroid defined by bases.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by bases.

    Returns:
        list[set[T]]: The dependent sets of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_bases_matroid(matroid)))


def from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct dependent sets from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, Cs = matroid
    return [D for D in powset(E) if any(map(lambda C: C <= D, Cs))]


def from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> list[set[T]]:
    """Construnct dependent sets from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, r = matroid
    # Cs = {C ⊆ E : r(C) ≠ |C|}
    return [C for C in powset(E) if r(C) != len(C)]


def from_nulity_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> list[set[T]]:
    """Construnct dependent sets from a matroid defined by a nulity function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, n = matroid
    # Cs = { C ⊆ E : n(C) ≠ 0 }
    return [C for C in powset(E) if n(C) != 0]


def from_closure_matroid(matroid: tuple[set[T],Callable[[set[T]], set[T]]]) -> list[set[T]]:
    """COnstruct dependent sets from a matroid defined by a closure function.

    Args:
        matroid (tuple[set[T],Callable[[set[T]], set[T]]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, _ = matroid
    return from_circuits_matroid((E, circuits.from_closure_matroid(matroid)))


def from_flats_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct dependent sets from a matroid defined by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_flats_matroid(matroid)))


def from_open_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct dependent sets from a matroid defined by open sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by open sets.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_open_matroid(matroid)))


def from_hyperplanes_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct dependent sets from a matroid defined by hyperplanes.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by hyperplanes.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_hyperplanes_matroid(matroid)))


def from_spanning_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct dependent sets from a matroid defined by spanning sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by spanning sets.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_spanning_matroid(matroid)))
