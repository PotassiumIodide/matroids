from typing    import Callable, TypeVar

from matroids.core.set_operator import powset

import matroids.construct.bases as bases

T = TypeVar('T')


def from_independent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct hyperplanes from a matroid defined by independent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        list[set[T]]: The hyperplanes of a given matroid.
    """
    E, _ = matroid
    return from_bases_matroid((E, bases.from_independent_matroid(matroid)))


def from_dependent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct hyperplanes from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by dependent sets.

    Returns:
        list[set[T]]: The hyperplanes of a given matroid.
    """
    E, _ = matroid
    return from_bases_matroid((E, bases.from_dependent_matroid(matroid)))


def from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct hyperplanes from a matroid defined by bases.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by bases.

    Returns:
        list[set[T]]: The hyperplanes of a given matroid.
    """
    E, Bs = matroid
    # Hs is the maximal set in { H ⊆ E : B ⊈ H, ∀B ∈ Bs }
    set_containing_no_bases = [X for X in powset(E) if all(map(lambda B: not (B <= X), Bs))]
    # Maximalization
    return [H for H in set_containing_no_bases if all(map(lambda X: not (H < X), set_containing_no_bases))]


def from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct hyperplanes from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        list[set[T]]: The hyperplanes of a given matroid.
    """
    E, _ = matroid
    return from_bases_matroid((E, bases.from_circuits_matroid(matroid)))


def from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]],int]]) -> list[set[T]]:
    """Construct hyperplanes from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The hyperplanes of a given matroid.
    """
    E, _ = matroid
    return from_bases_matroid((E, bases.from_rank_matroid(matroid)))


def from_nulity_matroid(matroid: tuple[set[T], Callable[[set[T]],int]]) -> list[set[T]]:
    """Construct hyperplanes from a matroid defined by a nulity function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a nulity function.

    Returns:
        list[set[T]]: The hyperplanes of a given matroid.
    """
    E, _ = matroid
    return from_bases_matroid((E, bases.from_nulity_matroid(matroid)))


def from_closure_matroid(matroid: tuple[set[T], Callable[[set[T]],set[T]]]) -> list[set[T]]:
    """Construct hyperplanes from a matroid defined by a closure function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]]): A matroid defined by a closure function.

    Returns:
        list[set[T]]: The hyperplanes of a given matroid.
    """
    E, _ = matroid
    return from_bases_matroid((E, bases.from_closure_matroid(matroid)))


def from_flats_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct hyperplanes from a matroid defined by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        list[set[T]]: The hyperplanes of a given matroid.
    """
    E, Fs = matroid
    # Hs = { H ∈ Fs\{E} : H ⊈ F, ∀F ∈ Fs\{E} }
    return [H for H in Fs if ((H != E) and all(map(lambda F: (not H < F) or (F == E), Fs)))]


def from_open_matroid(matroid: tuple[set[T], Callable[[set[T]],set[T]]]) -> list[set[T]]:
    """Construct hyperplanes from a matroid defined by open sets.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]]): A matroid defined by open sets.

    Returns:
        list[set[T]]: The hyperplanes of a given matroid.
    """
    E, _ = matroid
    return from_bases_matroid((E, bases.from_open_matroid(matroid)))


def from_spanning_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct hyperplanes from a matroid defined by spanning sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by spanning sets.

    Returns:
        list[set[T]]: The hyperplanes of a given matroid.
    """
    E, Ss = matroid
    # Hs is the maximal set of the non-spanning sets { N ⊆ E : N ∉ Ss }
    non_spannings = [N for N in powset(E) if N not in Ss]
    # Maximalization
    return [H for H in non_spannings if all(map(lambda X: not (H < X), non_spannings))]