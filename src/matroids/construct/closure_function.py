from functools import reduce
from operator  import and_
from typing    import Callable, TypeVar

import src.matroids.construct.independent_sets as independent_sets
import src.matroids.construct.rank_function as rank_function

T = TypeVar('T')


def from_independent_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by independent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        Callable[[set[T]], set[T]]: The gained closure function of a given matroid.
    """
    E, _ = matroid
    return from_rank_matroid((E, rank_function.from_independent_matroid(matroid)))


def from_dependent_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by dependent sets.

    Returns:
        Callable[[set[T]], set[T]]: A closure function of a given matroid.
    """
    E, _ = matroid
    return from_independent_matroid((E, independent_sets.from_dependent_matroid(matroid)))


def from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by bases.

    Args:
        matroid (tuple[set[T], list[set[T]]]): Matroid defined by bases.

    Returns:
        Callable[[set[T]], set[T]]: The closure function of a given matroid.
    """
    E, _ = matroid
    return from_rank_matroid((E, rank_function.from_bases_matroid(matroid)))


def from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        Callable[[set[T]], set[T]]: The closure function of a given matroid.
    """
    E, Cs = matroid
    # cl(X) = X ∪ { e ∈ E : ∃C ∈ Cs s.t. e ∈ C ⊆ X ∪ {e} }
    return lambda X: X | { e for e in E if any(map(lambda C: e in C and C <= X | {e}, Cs))}


def from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function.

    Returns:
        Callable[[set[T]], set[T]]: The closure function of a given matroid.
    """
    E, r = matroid
    # cl(X) = {e ∈ E | r(X) = r(X ∪ {e})}, ∀X ⊆ E
    return lambda X: {e for e in E if r(X) == r(X | {e})}


def from_flats_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        Callable[[set[T]], set[T]]: The closure function of a given matroid.
    """
    E, Fs = matroid
    # cl(X) = ∩ { F ∈ Fs : X ⊆ F }
    return lambda X: reduce(and_, (F for F in Fs if X <= F), E)


def from_open_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by open sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by open sets.

    Returns:
        Callable[[set[T]], set[T]]: The closure function of a given matroid.
    """
    E, _ = matroid
    return from_rank_matroid((E, rank_function.from_open_matroid(matroid)))


def from_hyperplanes_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by hyperplanes.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by hyperplanes.

    Returns:
        Callable[[set[T]], set[T]]: The closure function of a given matroid.
    """
    E, _ = matroid
    return from_rank_matroid((E, rank_function.from_hyperplanes_matroid(matroid)))


def from_spanning_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by spanning sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by spanning sets.

    Returns:
        Callable[[set[T]], set[T]]: The closure function of a given matroid.
    """
    E, _ = matroid
    return from_rank_matroid((E, rank_function.from_spanning_matroid(matroid)))