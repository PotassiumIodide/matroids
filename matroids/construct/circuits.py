from typing    import Callable, TypeVar

from matroids.core.set_operator import powset

import matroids.construct.dependent_sets as dependent_sets

T = TypeVar('T')


def from_independent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct circuits from a matroid defined by independent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        list[set[T]]: The circuits of a given matroid.
    """
    E, Is = matroid
    # Ds = { D ⊆ E : D ∈ Is }
    Ds = [D for D in powset(E) if D not in Is]
    # Cs = { C ∈ Ds : D ⊈ C, ∀D ∈ Ds\{C} }
    return [C for C in Ds if all(map(lambda D: not D < C, Ds))]


def from_dependent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct circuits from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by dependent sets.

    Returns:
        tuple[set[T], list[set[T]]]: The circuits of a given matroid.
    """
    E, Ds = matroid
    # Cs = { C ∈ Ds : D ⊈ C, ∀D ∈ Ds\{C} }
    return [ C for C in Ds if all(map(lambda D: not D < C, Ds)) ]


def from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct circuits from a matroid defined by bases

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by bases.

    Returns:
        list[set[T]]: The circuits of a given matroid.
    """
    E, _ = matroid
    return from_dependent_matroid((E, dependent_sets.from_bases_matroid(matroid)))


def from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> list[set[T]]:
    """Construct circuits from a matroid defined by a rank function

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The circuits of a given matroid.
    """
    E, r = matroid
    # Cs = { C ⊆ E : C ≠ ∅ and r(C\{c}) = |C| - 1 = r(C), ∀c ∈ C }
    return [C for C in powset(E) if (C != set()) and all(map(lambda c: (r(C - {c}) == len(C) - 1) and (len(C) - 1 == r(C)), C))]


def from_closure_matroid(matroid: tuple[set[T], Callable[[set[T]], set[T]]]) -> list[set[T]]:
    """Construct circuits from a matroid defined by a closure function

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]]): A matroid defined by a closure function.

    Returns:
        list[set[T]]: The circuits of a given matroid.
    """
    E, cl = matroid
    # Ds' = { D ⊆ E : D ≠ ∅ and d ∈ cl(D\{d}), ∀d ∈ D }
    # Cs: The minimal set of Ds' (Note that all the members in Ds are dependent but Ds' does NOT include all of the dependent sets.)
    Ds_ = [D_ for D_ in powset(E) if D_ and all(map(lambda d_: d_ in cl(D_ - {d_}), D_))]
    return [C for C in Ds_ if all(map(lambda D_: not D_ < C, Ds_))]


def from_flats_matroid(matroid: tuple[set[T],list[set[T]]]) -> list[set[T]]:
    """Construct circuits from a matroid defined by flats.

    Args:
        matroid (tuple[set[T],list[set[T]]]): A matroid defined by flats.

    Returns:
        list[set[T]]: The circuits of a given matroid.
    """
    E, _ = matroid
    return from_dependent_matroid((E, dependent_sets.from_flats_matroid(matroid)))


def from_open_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct circuits from a matroid defined by open sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by open sets.

    Returns:
        list[set[T]]: The circuits of a given matroid.
    """
    E, _ = matroid
    return from_dependent_matroid((E, dependent_sets.from_open_matroid(matroid)))


def from_hyperplanes_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct circuits from a matroid defined by hyperplanes.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by hyperplanes.

    Returns:
        list[set[T]]: The circuits of a given matroid.
    """
    E, _ = matroid
    return from_dependent_matroid((E, dependent_sets.from_hyperplanes_matroid(matroid)))


def from_spanning_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct circuits from a matroid defined by spanning sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by spanning sets.

    Returns:
        list[set[T]]: The circuits of a given matroid.
    """
    E, _ = matroid
    return from_dependent_matroid((E, dependent_sets.from_spanning_matroid(matroid)))