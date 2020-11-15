from typing    import Callable, TypeVar

from utils.set_operator import powset

import src.matroids.construct.independent_sets as independent_sets

T = TypeVar('T')


def from_independent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by independent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, Is = matroid
    # Bs = { B ∈ Is : B ⊈ I, ∀I ∈ Is\{B} }
    return [B for B in Is if all(map(lambda I: not B < I, Is))]


def from_dependent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): Matroid defined by dependent sets.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_dependent_matroid(matroid)))


def from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_circuits_matroid(matroid)))


def from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> list[set[T]]:
    """Construct bases from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]]], int]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, r = matroid
    # Bs = { B ⊆ E : |B| = r(B) = r(E) }
    return [B for B in powset(E) if (len(B) == r(B)) and (len(B) == r(E)) ]


def from_closure_matroid(matroid: tuple[set[T], Callable[[set[T]], set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by a closure function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_closure_matroid(matroid)))


def from_flats_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_flats_matroid(matroid)))


def from_open_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by open sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by open sets.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_open_matroid(matroid)))


def from_hyperplanes_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by hyperplanes.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by hyperplanes.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_hyperplanes_matroid(matroid)))


def from_spanning_matroid(matroid: tuple[set[T],list[set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by spanning sets.

    Args:
        matroid (tuple[set[T],list[set[T]]]): A matroid defined by spanning sets.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, Ss = matroid
    # Bs: The minimal set of Ss.
    return [B for B in Ss if all(map(lambda S: not S < B, Ss))]