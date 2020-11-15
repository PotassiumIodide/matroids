from functools import reduce
from itertools import combinations_with_replacement
from operator  import and_
from typing    import Callable, TypeVar

from utils.set_operator import powset

T = TypeVar('T')


def independent_sets_from_dependent_matroid(matroid: tuple[set[T], list[set]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by dependent sets

    Args:
        matroid (tuple[set[T], list[set]]): A matroid defined by dependent sets

    Returns:
        list[set[T]]: The independent sets of a given matroid.
    """
    E, Ds = matroid
    return [I for I in powset(E) if I not in Ds]


def independent_sets_from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by bases.

    Args:
        matroid (tuple[set[T], list[set[T]]]): Matroid defined by bases.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, Bs = matroid
    return [I for I in powset(E) if any(map(lambda B: I <= B, Bs))]


def independent_sets_from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        tuple[set[T], list[set[T]]]: The independent sets of a given matroid.
    """
    E, Cs = matroid
    # Is = {I ⊆ E : C ⊈ I, ∀C ∈ Cs}
    return [I for I in powset(E) if all(map(lambda C: not (C <= I), Cs))]


def independent_sets_from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The independent sets of a given matroid.
    """
    E, r = matroid
    # Is = {I ⊆ E : r(I) = |I|}
    return [I for I in powset(E) if r(I) == len(I)]


def independent_sets_from_closure_matroid(matroid: tuple[set[T], Callable[[set[T]], set[T]]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by a closure function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]): A matroid defined by a closure function.

    Returns:
        list[set[T]]: The independent sets of a given matroid.
    """
    E, cl = matroid
    # Is = { I ⊆ E : i ∉ cl(I\{i}), ∀i ∈ I }
    return [I for I in powset(E) if all(map(lambda i: i not in cl(I - {i}), I))]


def independent_sets_from_flats_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        list[set[T]]: The independent sets of a given matroid.
    """
    E, _ = matroid
    return independent_sets_from_closure_matroid((E, closure_function_from_flats_matroid(matroid)))


def independent_sets_from_open_sets_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by open sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by open sets.

    Returns:
        list[set[T]]: The independent sets of a given matroid.
    """
    E, _ = matroid
    return independent_sets_from_flats_matroid((E, flats_from_open_sets_matroid(matroid)))


def independent_sets_from_hyperplanes_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct independent sets from a matroid deifned by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        list[set[T]]: The independent sets of a given matroid.
    """
    E, _ = matroid
    return independent_sets_from_flats_matroid((E, flats_from_hyperplanes_matroid(matroid)))


def independent_sets_from_spanning_sets_matroid(matroid: tuple[set[T],list[set[T]]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by spanning sets.

    Args:
        matroid (tuple[set[T],list[set[T]]]): A matroid defined by spanning sets.

    Returns:
        list[set[T]]: The independent sets of a given matroid.
    """
    E, _ = matroid
    return independent_sets_from_bases_matroid((E, bases_from_spanning_sets_matroid(matroid)))


def dependent_sets_from_independent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct dependent sets from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        list[set[T]]: The dependent sets of a given matroid.
    """
    E, Is = matroid
    # Ds = {D ⊆ E : D ∉ Is}
    return [D for D in powset(E) if D not in Is]


def dependent_sets_from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct dependent sets from a matroid defined by bases.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by bases.

    Returns:
        list[set[T]]: The dependent sets of a given matroid.
    """
    E, _ = matroid
    return dependent_sets_from_independent_matroid((E, independent_sets_from_bases_matroid(matroid)))


def dependent_sets_from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct dependent sets from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, Cs = matroid
    return [D for D in powset(E) if any(map(lambda C: C <= D, Cs))]


def dependent_sets_from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> list[set[T]]:
    """Construnct dependent sets from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, _ = matroid
    return dependent_sets_from_independent_matroid((E, independent_sets_from_rank_matroid(matroid)))


def dependent_sets_from_closure_matroid(matroid: tuple[set[T],Callable[[set[T]], set[T]]]) -> list[set[T]]:
    """COnstruct dependent sets from a matroid defined by a closure function.

    Args:
        matroid (tuple[set[T],Callable[[set[T]], set[T]]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, _ = matroid
    return dependent_sets_from_circuits_matroid((E, circuits_from_closure_matroid(matroid)))


def dependent_sets_from_flats_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct dependent sets from a matroid defined by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, _ = matroid
    return dependent_sets_from_independent_matroid((E, independent_sets_from_flats_matroid(matroid)))


def dependent_sets_from_open_sets_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct dependent sets from a matroid defined by open sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by open sets.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, _ = matroid
    return dependent_sets_from_independent_matroid((E, independent_sets_from_open_sets_matroid(matroid)))


def dependent_sets_from_hyperplanes_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct dependent sets from a matroid defined by hyperplanes.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by hyperplanes.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, _ = matroid
    return dependent_sets_from_independent_matroid((E, independent_sets_from_hyperplanes_matroid(matroid)))


def dependent_sets_from_spanning_sets_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct dependent sets from a matroid defined by spanning sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by spanning sets.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, _ = matroid
    return dependent_sets_from_independent_matroid((E, independent_sets_from_spanning_sets_matroid(matroid)))


def bases_from_independent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by independent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, Is = matroid
    # Bs = { B ∈ Is : B ⊈ I, ∀I ∈ Is\{B} }
    return [B for B in Is if all(map(lambda I: not B < I, Is))]


def bases_from_dependent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): Matroid defined by dependent sets.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, _ = matroid
    return bases_from_independent_matroid((E, independent_sets_from_dependent_matroid(matroid)))


def bases_from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, _ = matroid
    return bases_from_independent_matroid((E, independent_sets_from_circuits_matroid(matroid)))


def bases_from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> list[set[T]]:
    """Construct bases from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]]], int]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, r = matroid
    # Bs = { B ⊆ E : |B| = r(B) = r(E) }
    return [B for B in powset(E) if (len(B) == r(B)) and (len(B) == r(E)) ]


def bases_from_closure_matroid(matroid: tuple[set[T], Callable[[set[T]], set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by a closure function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, _ = matroid
    return bases_from_independent_matroid((E, independent_sets_from_closure_matroid(matroid)))


def bases_from_flats_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, _ = matroid
    return bases_from_independent_matroid((E, independent_sets_from_flats_matroid(matroid)))


def bases_from_open_sets_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by open sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by open sets.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, _ = matroid
    return bases_from_independent_matroid((E, independent_sets_from_open_sets_matroid(matroid)))


def bases_from_hyperplanes_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by hyperplanes.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by hyperplanes.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, _ = matroid
    return bases_from_independent_matroid((E, independent_sets_from_hyperplanes_matroid(matroid)))


def bases_from_spanning_sets_matroid(matroid: tuple[set[T],list[set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by spanning sets.

    Args:
        matroid (tuple[set[T],list[set[T]]]): A matroid defined by spanning sets.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, Ss = matroid
    # Bs: The minimal set of Ss.
    return [B for B in Ss if all(map(lambda S: not S < B, Ss))]


def circuits_from_independent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
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


def circuits_from_dependent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct circuits from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by dependent sets.

    Returns:
        tuple[set[T], list[set[T]]]: The circuits of a given matroid.
    """
    E, Ds = matroid
    # Cs = { C ∈ Ds : D ⊈ C, ∀D ∈ Ds\{C} }
    return [ C for C in Ds if all(map(lambda D: not D < C, Ds)) ]


def circuits_from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct circuits from a matroid defined by bases

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by bases.

    Returns:
        list[set[T]]: The circuits of a given matroid.
    """
    E, _ = matroid
    return circuits_from_dependent_matroid((E, dependent_sets_from_bases_matroid(matroid)))


def circuits_from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> list[set[T]]:
    """Construct circuits from a matroid defined by a rank function

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The circuits of a given matroid.
    """
    E, r = matroid
    # Cs = { C ⊆ E : C ≠ ∅ and r(C\{c}) = |C| - 1 = r(C), ∀c ∈ C }
    return [C for C in powset(E) if (C != set()) and all(map(lambda c: (r(C - {c}) == len(C) - 1) and (len(C) - 1 == r(C)), C))]


def circuits_from_closure_matroid(matroid: tuple[set[T], Callable[[set[T]], set[T]]]) -> list[set[T]]:
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


def circuits_from_flats_matroid(matroid: tuple[set[T],list[set[T]]]) -> list[set[T]]:
    """Construct circuits from a matroid defined by flats.

    Args:
        matroid (tuple[set[T],list[set[T]]]): A matroid defined by flats.

    Returns:
        list[set[T]]: The circuits of a given matroid.
    """
    E, _ = matroid
    return circuits_from_dependent_matroid((E, dependent_sets_from_flats_matroid(matroid)))


def circuits_from_open_sets_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct circuits from a matroid defined by open sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by open sets.

    Returns:
        list[set[T]]: The circuits of a given matroid.
    """
    E, _ = matroid
    return circuits_from_dependent_matroid((E, dependent_sets_from_open_sets_matroid(matroid)))


def circuits_from_hyperplanes_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct circuits from a matroid defined by hyperplanes.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by hyperplanes.

    Returns:
        list[set[T]]: The circuits of a given matroid.
    """
    E, _ = matroid
    return circuits_from_dependent_matroid((E, dependent_sets_from_hyperplanes_matroid(matroid)))


def circuits_from_spanning_sets_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct circuits from a matroid defined by spanning sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by spanning sets.

    Returns:
        list[set[T]]: The circuits of a given matroid.
    """
    E, _ = matroid
    return circuits_from_dependent_matroid((E, dependent_sets_from_spanning_sets_matroid(matroid)))


def rank_function_from_independent_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by independent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        Callable[set[T], int]: The rank function of a given matroid.
    """
    E, Is = matroid
    # r(X) = max{|I|: I ∈ Is, I ⊆ X}, ∀X ⊆ E.
    return lambda X: max(map(len, (I for I in Is if I <= X)))


def rank_function_from_dependent_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by dependent sets.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, _ = matroid
    return rank_function_from_independent_matroid((E, independent_sets_from_dependent_matroid(matroid)))


def rank_function_from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by bases.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by bases.

    Returns:
        Callable[[set[T]], int]: A rank function of a given matroid.
    """
    E, _ = matroid
    return rank_function_from_independent_matroid((E, independent_sets_from_bases_matroid(matroid)))


def rank_function_from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, _ = matroid
    return rank_function_from_independent_matroid((E, independent_sets_from_circuits_matroid(matroid)))


def rank_function_from_closure_matroid(matroid: tuple[set[T], Callable[[set[T]], set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]]): A matroid defined by a closure function.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, _ = matroid
    return rank_function_from_circuits_matroid((E, circuits_from_closure_matroid(matroid)))


def rank_function_from_flats_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, _ = matroid
    return rank_function_from_independent_matroid((E, independent_sets_from_flats_matroid(matroid)))


def rank_function_from_open_sets_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by open sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by open sets.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, _ = matroid
    return rank_function_from_independent_matroid((E, independent_sets_from_open_sets_matroid(matroid)))


def rank_function_from_hyperplanes_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by hyperplanes.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by hyperplanes.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, _ = matroid
    return rank_function_from_independent_matroid((E, independent_sets_from_hyperplanes_matroid(matroid)))


def rank_function_from_spanning_sets_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by spanning sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by spanning sets.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, _ = matroid
    return rank_function_from_independent_matroid((E, independent_sets_from_spanning_sets_matroid(matroid)))


def closure_function_from_independent_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by independent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        Callable[[set[T]], set[T]]: The gained closure function of a given matroid.
    """
    E, _ = matroid
    return closure_function_from_rank_matroid((E, rank_function_from_independent_matroid(matroid)))


def closure_function_from_dependent_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by dependent sets.

    Returns:
        Callable[[set[T]], set[T]]: A closure function of a given matroid.
    """
    E, _ = matroid
    return closure_function_from_independent_matroid((E, independent_sets_from_dependent_matroid(matroid)))


def closure_function_from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by bases.

    Args:
        matroid (tuple[set[T], list[set[T]]]): Matroid defined by bases.

    Returns:
        Callable[[set[T]], set[T]]: The closure function of a given matroid.
    """
    E, _ = matroid
    return closure_function_from_rank_matroid((E, rank_function_from_bases_matroid(matroid)))


def closure_function_from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        Callable[[set[T]], set[T]]: The closure function of a given matroid.
    """
    E, Cs = matroid
    # cl(X) = X ∪ { e ∈ E : ∃C ∈ Cs s.t. e ∈ C ⊆ X ∪ {e} }
    return lambda X: X | { e for e in E if any(map(lambda C: e in C and C <= X | {e}, Cs))}


def closure_function_from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function.

    Returns:
        Callable[[set[T]], set[T]]: The closure function of a given matroid.
    """
    E, r = matroid
    # cl(X) = {e ∈ E | r(X) = r(X ∪ {e})}, ∀X ⊆ E
    return lambda X: {e for e in E if r(X) == r(X | {e})}


def closure_function_from_flats_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        Callable[[set[T]], set[T]]: The closure function of a given matroid.
    """
    E, Fs = matroid
    # cl(X) = ∩ { F ∈ Fs : X ⊆ F }
    return lambda X: reduce(and_, (F for F in Fs if X <= F), E)


def closure_function_from_open_sets_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by open sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by open sets.

    Returns:
        Callable[[set[T]], set[T]]: The closure function of a given matroid.
    """
    E, _ = matroid
    return closure_function_from_rank_matroid((E, rank_function_from_open_sets_matroid(matroid)))


def closure_function_from_hyperplanes_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by hyperplanes.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by hyperplanes.

    Returns:
        Callable[[set[T]], set[T]]: The closure function of a given matroid.
    """
    E, _ = matroid
    return closure_function_from_rank_matroid((E, rank_function_from_hyperplanes_matroid(matroid)))


def closure_function_from_spanning_sets_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by spanning sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by spanning sets.

    Returns:
        Callable[[set[T]], set[T]]: The closure function of a given matroid.
    """
    E, _ = matroid
    return closure_function_from_rank_matroid((E, rank_function_from_spanning_sets_matroid(matroid)))


def flats_from_independent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct flats from a matroid defined by independent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        list[set[T]]: The flats of a given matroid.
    """
    E, _ = matroid
    return flats_from_closure_matroid((E, closure_function_from_independent_matroid(matroid)))


def flats_from_dependent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct flats from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by dependent sets.

    Returns:
        list[set[T]]: The flats of a given matroid.
    """
    E, _ = matroid
    return flats_from_closure_matroid((E, closure_function_from_dependent_matroid(matroid)))



def flats_from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct flats from a matroid defined by bases.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by bases.

    Returns:
        list[set[T]]: The flats of a given matroid.
    """
    E, _ = matroid
    return flats_from_closure_matroid((E, closure_function_from_bases_matroid(matroid)))


def flats_from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct flats from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        list[set[T]]: The flats of a given matroid.
    """
    E, _ = matroid
    return flats_from_closure_matroid((E, closure_function_from_circuits_matroid(matroid)))


def flats_from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> list[set[T]]:
    """Construct flats from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The flats of a given matroid.
    """
    E, r = matroid
    # Fs = { F ⊆ E : r(F ∪ {e}) = r(F) + 1, ∀e ∈ E\F }
    return [ F for F in powset(E) if all(map(lambda e: r(F | {e}) == r(F) + 1, E - F))]


def flats_from_closure_matroid(matroid: tuple[set[T], Callable[[set[T]], set[T]]]) -> list[set[T]]:
    """Construct flats from a matroid defined by a closure function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]]): A matroid defined by a closure function.

    Returns:
        list[set[T]]: The flats of a given matroid.
    """
    E, cl = matroid
    # Fs = { F ⊆ E | cl(F) = F }
    return [F for F in powset(E) if cl(F) == F]


def flats_from_open_sets_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct flats from a matroid defined by open sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by open sets.

    Returns:
        list[set[T]]: The flats of a given matroid.
    """
    E, Os = matroid
    # Fs = { E - O : O ∈ Os }
    return [ E - O for O in Os ]


def flats_from_hyperplanes_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """COnstruct flats from a matroid defined by hyperplanes.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by hyperplanes.

    Returns:
        list[set[T]]: The flats of a given matroid.
    """
    E, Hs = matroid
    # Fs is a group generated by Hs under the intersection.
    Hs.append(E)
    all_intersection = lambda Xs: [X for X in powset(E) if X in [A & B for A, B in combinations_with_replacement(Xs, 2)]]
    
    tmp = all_intersection(Hs)
    # Repeat unless the set is closed under the intersection.
    # This loop must be stopped because E is finite, and E includes any intersection.
    while True:
        next_tmp = all_intersection(tmp)
        if len(tmp) == len(next_tmp):
            return tmp
        tmp = next_tmp


def flats_from_spanning_sets_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct flats from a matroid defined by spanning sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by spanning sets.

    Returns:
        list[set[T]]: The flats of a given matroid.
    """
    E, _ = matroid
    return flats_from_closure_matroid((E, closure_function_from_spanning_sets_matroid(matroid)))


def open_sets_from_independent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by independent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, _ = matroid
    return open_sets_from_flats_matroid((E, flats_from_independent_matroid(matroid)))


def open_sets_from_dependent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by dependent sets.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, _ = matroid
    return open_sets_from_flats_matroid((E, flats_from_dependent_matroid(matroid)))


def open_sets_from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by bases.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by bases.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, _ = matroid
    return open_sets_from_flats_matroid((E, flats_from_bases_matroid(matroid)))


def open_sets_from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, _ = matroid
    return open_sets_from_flats_matroid((E, flats_from_circuits_matroid(matroid)))


def open_sets_from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, _ = matroid
    return open_sets_from_flats_matroid((E, flats_from_rank_matroid(matroid)))


def open_sets_from_closure_matroid(matroid: tuple[set[T], Callable[[set[T]], set[T]]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by a closure function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]]): A matroid defined by a closure function.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, _ = matroid
    return open_sets_from_flats_matroid((E, flats_from_closure_matroid(matroid)))


def open_sets_from_flats_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, Fs = matroid
    # Os = { E - F : F ∈ Fs }
    return [E - F for F in Fs]


def open_sets_from_hyperplanes_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by hyperplanes.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by hyperplanes.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, _ = matroid
    return open_sets_from_flats_matroid((E, flats_from_hyperplanes_matroid(matroid)))


def open_sets_from_spanning_sets_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by spanning sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by spanning sets.

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, _ = matroid
    return open_sets_from_flats_matroid((E, flats_from_spanning_sets_matroid(matroid)))


def hyperplanes_from_independent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct hyperplanes from a matroid defined by independent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        list[set[T]]: The hyperplanes of a given matroid.
    """
    E, _ = matroid
    return hyperplanes_from_bases_matroid((E, bases_from_independent_matroid(matroid)))


def hyperplanes_from_dependent_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct hyperplanes from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by dependent sets.

    Returns:
        list[set[T]]: The hyperplanes of a given matroid.
    """
    E, _ = matroid
    return hyperplanes_from_bases_matroid((E, bases_from_dependent_matroid(matroid)))


def hyperplanes_from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
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


def hyperplanes_from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct hyperplanes from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        list[set[T]]: The hyperplanes of a given matroid.
    """
    E, _ = matroid
    return hyperplanes_from_bases_matroid((E, bases_from_circuits_matroid(matroid)))


def hyperplanes_from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]],int]]) -> list[set[T]]:
    """Construct hyperplanes from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The hyperplanes of a given matroid.
    """
    E, _ = matroid
    return hyperplanes_from_bases_matroid((E, bases_from_rank_matroid(matroid)))


def hyperplanes_from_closure_matroid(matroid: tuple[set[T], Callable[[set[T]],set[T]]]) -> list[set[T]]:
    """Construct hyperplanes from a matroid defined by a closure function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]]): A matroid defined by a closure function.

    Returns:
        list[set[T]]: The hyperplanes of a given matroid.
    """
    E, _ = matroid
    return hyperplanes_from_bases_matroid((E, bases_from_closure_matroid(matroid)))


def hyperplanes_from_flats_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct hyperplanes from a matroid defined by flats.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats.

    Returns:
        list[set[T]]: The hyperplanes of a given matroid.
    """
    E, Fs = matroid
    # Hs = { H ∈ Fs\{E} : H ⊈ F, ∀F ∈ Fs\{E} }
    return [H for H in Fs if ((H != E) and all(map(lambda F: (not H < F) or (F == E), Fs)))]


def hyperplanes_from_spanning_sets_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
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


def spanning_sets_from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> list[set[T]]:
    """Construct spanning sets from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function

    Returns:
        list[set[T]]: The spanning set of a given matroid.
    """
    E, r = matroid
    # Ss = { S ⊆ E : r(S) = r(E) }
    return [S for S in powset(E) if r(S) == r(E)]