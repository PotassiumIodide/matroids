from typing    import Callable, TypeVar

from matroids.core.set_operator import powset

import matroids.construct.bases as bases
import matroids.construct.closure_function as closure_function
import matroids.construct.flats as flats

T = TypeVar('T')


def from_dependent_matroid(matroid: tuple[set[T], list[set]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by dependent sets

    Args:
        matroid (tuple[set[T], list[set]]): A matroid defined by dependent sets

    Returns:
        list[set[T]]: The independent sets of a given matroid.
    """
    E, Ds = matroid
    return [I for I in powset(E) if I not in Ds]


def from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by bases.

    Args:
        matroid (tuple[set[T], list[set[T]]]): Matroid defined by bases.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, Bs = matroid
    return [I for I in powset(E) if any(map(lambda B: I <= B, Bs))]


def from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        tuple[set[T], list[set[T]]]: The independent sets of a given matroid.
    """
    E, Cs = matroid
    # Is = {I ⊆ E : C ⊈ I, ∀C ∈ Cs}
    return [I for I in powset(E) if all(map(lambda C: not (C <= I), Cs))]


def from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The independent sets of a given matroid.
    """
    E, r = matroid
    # Is = {I ⊆ E : r(I) = |I|}
    return [I for I in powset(E) if r(I) == len(I)]


def from_closure_matroid(matroid: tuple[set[T], Callable[[set[T]], set[T]]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by a closure function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]): A matroid defined by a closure function.

    Returns:
        list[set[T]]: The independent sets of a given matroid.
    """
    E, cl = matroid
    # Is = { I ⊆ E : i ∉ cl(I\{i}), ∀i ∈ I }
    return [I for I in powset(E) if all(map(lambda i: i not in cl(I - {i}), I))]


def from_flats_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        list[set[T]]: The independent sets of a given matroid.
    """
    E, _ = matroid
    return from_closure_matroid((E, closure_function.from_flats_matroid(matroid)))


def from_open_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by open sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by open sets.

    Returns:
        list[set[T]]: The independent sets of a given matroid.
    """
    E, _ = matroid
    return from_flats_matroid((E, flats.from_open_matroid(matroid)))


def from_hyperplanes_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct independent sets from a matroid deifned by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        list[set[T]]: The independent sets of a given matroid.
    """
    E, _ = matroid
    return from_flats_matroid((E, flats.from_hyperplanes_matroid(matroid)))


def from_spanning_matroid(matroid: tuple[set[T],list[set[T]]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by spanning sets.

    Args:
        matroid (tuple[set[T],list[set[T]]]): A matroid defined by spanning sets.

    Returns:
        list[set[T]]: The independent sets of a given matroid.
    """
    E, _ = matroid
    return from_bases_matroid((E, bases.from_spanning_matroid(matroid)))