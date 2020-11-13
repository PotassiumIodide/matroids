from functools import reduce
from operator  import and_
from typing    import Callable, TypeVar

from utils.set_operator import powset

T = TypeVar('T')


def indeps_from_deps_matroid(matroid: tuple[set[T], list[set]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by dependent sets

    Args:
        matroid (tuple[set[T], list[set]]): A matroid defined by dependent sets

    Returns:
        list[set[T]]: The independent sets of a given matroid.
    """
    E, Ds = matroid
    return [I for I in powset(E) if I not in Ds]


def indeps_from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by bases.

    Args:
        matroid (tuple[set[T], list[set[T]]]): Matroid defined by bases.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, Bs = matroid
    return [I for I in powset(E) if any(map(lambda B: I <= B, Bs))]


def indeps_from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        tuple[set[T], list[set[T]]]: The independent sets of a given matroid.
    """
    E, Cs = matroid
    # Is = {I ⊆ E : C ⊈ I, ∀C ∈ Cs}
    return [I for I in powset(E) if all(map(lambda C: not (C <= I), Cs))]


def indeps_from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The independent sets of a given matroid.
    """
    E, r = matroid
    # Is = {I ⊆ E : r(I) = |I|}
    return [I for I in powset(E) if r(I) == len(I)]


def indeps_from_closure_matroid(matroid: tuple[set[T], Callable[[set[T]], set[T]]]) -> list[set[T]]:
    """Construct independent sets from a matroid defined by a closure function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]): A matroid defined by a closure function.

    Returns:
        list[set[T]]: The independent sets of a given matroid.
    """
    E, cl = matroid
    # Is = { I ⊆ E : i ∈ cl(I\{i}), ∀i ∈ I }
    return [I for I in powset(E) if all(map(lambda i: i not in cl(I - {i}), I))]


def deps_from_indeps_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct dependent sets from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        list[set[T]]: The dependent sets of a given matroid.
    """
    E, Is = matroid
    # Ds = {D ⊆ E : D ∉ Is}
    return [D for D in powset(E) if D not in Is]


def deps_from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct dependent sets from a matroid defined by bases.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by bases.

    Returns:
        list[set[T]]: The dependent sets of a given matroid.
    """
    E, _ = matroid
    return deps_from_indeps_matroid((E, indeps_from_bases_matroid(matroid)))


def deps_from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct dependent sets from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, Cs = matroid
    return [D for D in powset(E) if any(map(lambda C: C <= D, Cs))]


def deps_from_rank_matroid(matroid: tuple[set[T], Callable[[set[T]], int]]) -> list[set[T]]:
    """Construnct dependent sets from a matroid defined by a rank function.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], int]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, _ = matroid
    return deps_from_indeps_matroid((E, indeps_from_rank_matroid(matroid)))


def deps_from_closure_matroid(matroid: tuple[set[T],Callable[[set[T]], set[T]]]) -> list[set[T]]:
    """COnstruct dependent sets from a matroid defined by a closure function.

    Args:
        matroid (tuple[set[T],Callable[[set[T]], set[T]]]): A matroid defined by a rank function.

    Returns:
        list[set[T]]: The dependent sets of a matroid.
    """
    E, _ = matroid
    return deps_from_circuits_matroid((E, circuits_from_closure_matroid(matroid)))


def bases_from_indeps_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by independent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, Is = matroid
    # Bs = { B ∈ Is : B ⊈ I, ∀I ∈ Is\{B} }
    return [B for B in Is if all(map(lambda I: not B < I, Is))]


def bases_from_deps_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): Matroid defined by dependent sets.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, _ = matroid
    return bases_from_indeps_matroid((E, indeps_from_deps_matroid(matroid)))


def bases_from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct bases from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        list[set[T]]: The bases of a given matroid.
    """
    E, _ = matroid
    return bases_from_indeps_matroid((E, indeps_from_circuits_matroid(matroid)))


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
    return bases_from_indeps_matroid((E, indeps_from_closure_matroid(matroid)))


def circuits_from_indeps_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
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


def circuits_from_deps_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
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
    return circuits_from_deps_matroid((E, deps_from_bases_matroid(matroid)))


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
        list[set[T]]: [description]
    """
    E, cl = matroid
    # Ds' = { D ⊆ E : D ≠ ∅ and d ∈ cl(D\{d}), ∀d ∈ D }
    # Cs: The minimal set of Ds' (Note that all the members in Ds are dependent but Ds' does NOT include all of the dependent sets.)
    Ds_ = [D_ for D_ in powset(E) if D_ and all(map(lambda d_: d_ in cl(D_ - {d_}), D_))]
    return [C for C in Ds_ if all(map(lambda D_: not D_ < C, Ds_))]


def rank_function_from_indeps_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by independent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        Callable[set[T], int]: The rank function of a given matroid.
    """
    E, Is = matroid
    # r(X) = max{|I|: I ∈ Is, I ⊆ X}, ∀X ⊆ E.
    return lambda X: max(map(len, (I for I in Is if I <= X)))


def rank_function_from_deps_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by dependent sets.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, _ = matroid
    return rank_function_from_indeps_matroid((E, indeps_from_deps_matroid(matroid)))


def rank_function_from_bases_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by bases.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by bases.

    Returns:
        Callable[[set[T]], int]: A rank function of a given matroid.
    """
    E, _ = matroid
    return rank_function_from_indeps_matroid((E, indeps_from_bases_matroid(matroid)))


def rank_function_from_circuits_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by circuits.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, _ = matroid
    return rank_function_from_indeps_matroid((E, indeps_from_circuits_matroid(matroid)))


def rank_function_from_closure_matroid(matroid: tuple[set[T], Callable[[set[T]], set[T]]]) -> Callable[[set[T]], int]:
    """Construct a rank function from a matroid defined by circuits.

    Args:
        matroid (tuple[set[T], Callable[[set[T]], set[T]]]): A matroid defined by a closure function.

    Returns:
        Callable[[set[T]], int]: The rank function of a given matroid.
    """
    E, _ = matroid
    return rank_function_from_circuits_matroid((E, circuits_from_closure_matroid(matroid)))


def closure_function_from_indeps_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by independent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by independent sets.

    Returns:
        Callable[[set[T]], set[T]]: The gained closure function of a given matroid.
    """
    E, _ = matroid
    return closure_function_from_rank_matroid((E, rank_function_from_indeps_matroid(matroid)))


def closure_function_from_deps_matroid(matroid: tuple[set[T], list[set[T]]]) -> Callable[[set[T]], set[T]]:
    """Construct a closure function from a matroid defined by dependent sets.

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by dependent sets.

    Returns:
        Callable[[set[T]], set[T]]: A closure function of a given matroid.
    """
    E, _ = matroid
    return closure_function_from_indeps_matroid((E, indeps_from_deps_matroid(matroid)))


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


def open_sets_from_flats_matroid(matroid: tuple[set[T], list[set[T]]]) -> list[set[T]]:
    """Construct open sets from a matroid defined by flats

    Args:
        matroid (tuple[set[T], list[set[T]]]): A matroid defined by flats

    Returns:
        list[set[T]]: The open sets of a given matroid.
    """
    E, Fs = matroid
    # Os = { E - F : F ∈ Fs }
    return [E - F for F in Fs]