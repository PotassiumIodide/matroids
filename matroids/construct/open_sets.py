from typing    import Callable, TypeVar

import matroids.construct.flats as flats

T = TypeVar('T')


def from_independent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by independent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, _ = matroid
    return from_flats_matroid((E, flats.from_independent_matroid(matroid)))


def from_dependent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by dependent sets.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, _ = matroid
    return from_flats_matroid((E, flats.from_dependent_matroid(matroid)))


def from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by bases.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by bases.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, _ = matroid
    return from_flats_matroid((E, flats.from_bases_matroid(matroid)))


def from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, _ = matroid
    return from_flats_matroid((E, flats.from_circuits_matroid(matroid)))


def from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, _ = matroid
    return from_flats_matroid((E, flats.from_rank_matroid(matroid)))


def from_closure_matroid(matroid: tuple[set[T], Callable[[set[T]], set[T]]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by a closure function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]]): A matroid defined by a closure function.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, _ = matroid
    return from_flats_matroid((E, flats.from_closure_matroid(matroid)))


def from_flats_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, Fs = matroid
    # Os = { E - F : F ∈ Fs }
    return [E - F for F in Fs]


def from_hyperplanes_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by hyperplanes.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by hyperplanes.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, _ = matroid
    return from_flats_matroid((E, flats.from_hyperplanes_matroid(matroid)))


def from_spanning_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by spanning sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by spanning sets.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, _ = matroid
    return from_flats_matroid((E, flats.from_spanning_matroid(matroid)))