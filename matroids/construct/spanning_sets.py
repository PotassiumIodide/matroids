from typing    import Callable, TypeVar

from matroids.core.set_operator import powset

import matroids.construct.rank_function as rank_function

T = TypeVar('T')


def from_independent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct spanning sets from a matroid defined by independent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        list[set[T]]: The spanning set of a given matroid.
    """
    E, _ = matroid
    return from_rank_matroid((E, rank_function.from_independent_matroid(matroid)))


def from_dependent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct spanning sets from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by dependent sets.

    Returns:
        list[set[T]]: The spanning set of a given matroid.
    """
    E, _ = matroid
    return from_rank_matroid((E, rank_function.from_dependent_matroid(matroid)))


def from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct spanning sets from a matroid defined by bases.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by bases.

    Returns:
        list[set[T]]: The spanning set of a given matroid.
    """
    E, _ = matroid
    return from_rank_matroid((E, rank_function.from_bases_matroid(matroid)))


def from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct spanning sets from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        list[set[T]]: The spanning set of a given matroid.
    """
    E, _ = matroid
    return from_rank_matroid((E, rank_function.from_circuits_matroid(matroid)))


def from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> list[set[T]]:
    """Construct spanning sets from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function

    Returns:
        list[set[T]]: The spanning set of a given matroid.
    """
    E, r = matroid
    # Ss = { S ⊆ E : r(S) = r(E) }
    return [S for S in powset(E) if r(S) == r(E)]


def from_nulity_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> list[set[T]]:
    """Construct spanning sets from a matroid defined by a nulity function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a nulity function

    Returns:
        list[set[T]]: The spanning set of a given matroid.
    """
    E, n = matroid
    # Ss = { S ⊆ E : n(E) - n(S) = |E| - |S| }
    return [S for S in powset(E) if n(E) - n(S) == len(E) - len(S)]


def from_closure_matroid(matroid: tuple[set[T], Callable[[set[T]], set[T]]]) -> list[set[T]]:
    """Construct spanning sets from a matroid defined by a closure function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]]): A matroid defined by a closure function

    Returns:
        list[set[T]]: The spanning set of a given matroid.
    """
    E, _ = matroid
    return from_rank_matroid((E, rank_function.from_closure_matroid(matroid)))


def from_flats_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct spanning sets from a matroid defined by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        list[set[T]]: The spanning set of a given matroid.
    """
    E, _ = matroid
    return from_rank_matroid((E, rank_function.from_flats_matroid(matroid)))


def from_open_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct spanning sets from a matroid defined by open sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by open sets.

    Returns:
        list[set[T]]: The spanning set of a given matroid.
    """
    E, _ = matroid
    return from_rank_matroid((E, rank_function.from_open_matroid(matroid)))


def from_hyperplanes_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct spanning sets from a matroid defined by hyperplanes.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by hyperplanes.

    Returns:
        list[set[T]]: The spanning set of a given matroid.
    """
    E, _ = matroid
    return from_rank_matroid((E, rank_function.from_hyperplanes_matroid(matroid)))