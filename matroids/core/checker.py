from itertools import combinations
from math import inf
from typing import Callable, TypeVar, Union

from .set_operator import powset

T = TypeVar('T')


def satisfies_independent_axiom( maybe_matroid                      : tuple[set[T], list[set[T]]]
                               , clearly_has_emptyset               : bool=False
                               , clearly_hereditary                 : bool=False
                               , clearly_has_augmentation_properties: bool=False) -> bool:
    """Judge whether the given pair of a ground set and a family of its subsets is a matroid.
    This is done due to the axiom of independent sets.

    Args:
        maybe_matroid (tuple[set[T], list[set[T]]]): A tuple (E, Is), where E is a ground set and Is is a family of subsets of E.
        clearly_has_emptyset                 (bool, optional) - If this is True, the check of (I1) will be skipped. Defaults to False.
        clearly_hereditary                   (bool, optional) - If this is True, the check of (I2) will be skipped. Defaults to False.
        clearly_has_augmentation_properties  (bool, optional) - If this is True, the check of (I3) will be skipped. Defaults to False.
    
    Returns:
        bool: True if the given family satisfies the axiom of independent sets, otherwise False.
    """
    E, Is = maybe_matroid
    # [Prerequisits] I ∈ Is => I ⊆ E
    if not all(map(lambda I: I <= E, Is)):
        return False
    
    # (I1) ∅ ∈ Is (non-empty)
    if not clearly_has_emptyset and set() not in Is:
        return False
    
    # (I2) I1 ⊆ I2 and I2 ∈ Is => I1 ∈ Is (hereditary)
    if not clearly_hereditary:
        for I2 in Is:
            if any(I1 not in Is for I1 in powset(I2)):
                return False

    # (I3) I1, I2 ∈ Is and |I1| < |I2| => ∃e ∈ I2\I1 s.t. I1 ∪ {e} ∈ Is (independence augmentation property)
    if clearly_has_augmentation_properties:
        return True

    for I1 in Is:
        for I2 in (I2 for I2 in Is if len(I2) > len(I1)):
            if not [e for e in I2 - I1 if (I1 | {e}) in Is]:
                return False
    return True


def satisfies_dependent_axiom( maybe_matroid                      : tuple[set[T], list[set[T]]]
                             , clearly_has_no_emptyset            : bool=False
                             , clearly_opposite_hereditary        : bool=False
                             , clearly_has_diminishment_properties: bool=False) -> bool:
    """Judge whether the given pair of a ground set and a family of its subsets is a matroid.
    This is done due to the axiom of dependent sets (derived from that of independent sets).

    Args:
        maybe_matroid (tuple[set[T], list[set[T]]]): A tuple (E, Ds), where E is a ground set and Ds is a family of subsets of E.
        clearly_has_emptyset                 (bool, optional) - If this is True, the check of (D1) will be skipped. Defaults to False.
        clearly_opposite_hereditary          (bool, optional) - If this is True, the check of (D2) will be skipped. Defaults to False.
        clearly_has_diminishment_properties  (bool, optional) - If this is True, the check of (D3) will be skipped. Defaults to False.
    
    Returns:
        bool: True if the given family satisfies the axiom of independent sets, otherwise False.
    """
    E, Ds = maybe_matroid
    # [Prerequisits] D ∈ Ds => D ⊆ E
    if not all(map(lambda D: D <= E, Ds)):
        return False
    
    # (D1) ∅ ∉ Ds (no empty)
    if not clearly_has_no_emptyset and set() in Ds:
        return False
    
    # (D2) D1 ⊆ D2 ⊆ E and D1 ∈ Ds => D2 ∈ Ds (opposite-hereditary)
    if not clearly_opposite_hereditary:
        for D1 in Ds:
            if any(D2 not in Ds for D2 in [D for D in powset(E) if D1 <= D]):
                return False

    # (D3) D1, D2 ∈ Ds and D1 ≠ D2 => (D1 ∩ D2 ∈ Ds) or ((D1 ∪ D2)\{e} ∈ Ds, ∀e ∈ E)
    if clearly_has_diminishment_properties:
        return True

    for D1, D2 in combinations(Ds, 2):
        if (D1 & D2 not in Ds) and any((D1 | D2) - {e} not in Ds for e in E):
            return False
    return True


def satisfies_bases_axiom( maybe_matroid: tuple[set[T], list[set[T]]]
                         , clearly_non_empty: bool=False
                         , clearly_base_exchangable: bool=False) -> bool:
    """Judge whether the given pair of a ground set and a family of its subsets is a matroid.
    This is done due to the axiom of bases.

    Args:
        maybe_matroid (tuple[set[T], list[set[T]]]): A tuple (E, Bs), where E is a ground set and Bs is a family of subsets of E.
        clearly_non_empty        (bool, optional): If this is True, the check of (B1) will be skipped. Defaults to False.
        clearly_base_exchangable (bool, optional): If this is True, the check of (B2) will be skipped. Defaults to False.

    Returns:
        bool: True if the given family satisfies the axiom of bases, otherwise False.
    """
    E, Bs = maybe_matroid
    # (B1) Bs ≠ ∅ (non-empty)
    if not clearly_non_empty and not Bs:
        return False

    # [Prerequisits] B ∈ Bs => B ⊆ E
    if not all(map(lambda B: B <= E, Bs)):
        return False

    # [Trivial Bases] {∅} is a bases of a trivial matroid (E, ∅) for any E. <- For faster
    if set() in Bs and len(Bs) == 1:
        return True

    # [Easy Check] B1, B2 ∈ Bs => |B1| = |B2| (<=> |{|B|: B ∈ Bs}| - 1 = 0) <- For faster
    if len(set(map(len, Bs))) - 1:
        return False
    
    # (B2) B1, B2 ∈ Bs, b1 ∈ B1 - B2 => ∃b2 ∈ B2 - B1: (B1 - {b1}) ∪ {b2} ∈ Bs
    if not clearly_base_exchangable:
        for B1, B2 in combinations(Bs, 2):
            for b1 in B1 - B2:
                if not [b2 for b2 in B2 - B1 if ((B1 - {b1}) | {b2}) in Bs]:
                    return False
    return True


def satisfies_circuits_axiom( maybe_matroid               : tuple[set[T], list[set[T]]]
                            , clearly_has_no_emptyset     : bool=False
                            , clearly_minimal             : bool=False
                            , clearly_circuits_exchangable: bool=False) -> bool:
    """Judge whether the given pair of a ground set and a family of its subsets is a matroid.
    This is done due to the axiom of circuits.

    Args:
        maybe_matroid (tuple[set[T], list[set[T]]]): A tuple (E, Cs), where E is a ground set and Cs is a family of subsets of E.
        clearly_has_no_emptyset      (bool, optional): If this is True, the check of (C1) will be skipped. Defaults to False.
        clearly_minimal              (bool, optional): If this is True, the check of (C2) will be skipped. Defaults to False.
        clearly_circuits_exchangable (bool, optional): If this is True, the check of (C3) will be skipped. Defaults to False.

    Returns:
        bool: True if the given family satisfies the axiom of circuits, otherwise False.
    """
    E, Cs = maybe_matroid
    # [Prerequisits] C ∈ Cs => C 
    if not all(map(lambda C: C <= E, Cs)):
        return False

    # (C1) ∅ ∉ Cs
    if not clearly_has_no_emptyset and set() in Cs:
        return False

    # (C2) C1, C2 ∈ Cs and C1 ⊆ C2 => C1 = C2.
    if not clearly_minimal:
        for C1, C2 in combinations(Cs, 2):
            if C1 <= C2 and C1 != C2:
                return False
    
    # (C3) C1, C2 ∉ Cs with C1 ≠ C2 and e ∈ C1 ∩ C2 => ∃C3 ∈ Cs s.t. C3 ⊆ (C1 ∪ C2) - e.
    if not clearly_circuits_exchangable:
        for C1, C2 in combinations(Cs, 2):
            for e in C1 & C2:
                if not any([C3 <= (C1 | C2) - {e} for C3 in Cs]):
                    return False
    return True


def satisfies_rank_function_axiom( maybe_matroid                        : tuple[set[T], Callable[[set[T]], int]]
                                 , clearly_bounded_above_by_cardinality : bool=False
                                 , clearly_monotonic                    : bool=False
                                 , clearly_submodular                   : bool=False) -> bool:
    """Judge whether the given pair of a ground set and a function from set to non-negative integers is a matroid.
    This is done due to the axiom of a rank function.

    Args:
        maybe_matroid (tuple[set[T], Callable[[set[T]], int]): A tuple (E, r), where E is a ground set and r is a function.
        clearly_bounded_above_by_cardinality (bool, optional): If this is True, the check of (R1) will be skipped. Defaults to False.
        clearly_monotonic                    (bool, optional): If this is True, the check of (R2) will be skipped. Defaults to False.
        clearly_submodular                   (bool, optional): If this is True, the check of (R3) will be skipped. Defaults to False.

    Returns:
        bool: True if the given family satisfies the axiom of a rank function, otherwise False.
    """
    E, r = maybe_matroid
    # (R1) ∀X ⊆ E, 0 ≦ r(X) ≦ |X|
    if not clearly_bounded_above_by_cardinality:
        for X in powset(E):
            if not (0 <= r(X) <= len(X)):
                return False
    
    # (R2) X ⊆ Y ⊆ E => r(X) ≦ r(Y) (monotonic)
    if not clearly_monotonic:
        for Y in powset(E):
            for X in powset(Y):
                if r(X) > r(Y):
                    return False

    # (R3) ∀X, Y ⊆ E, r(X) + r(Y) ≧ r(X ∪ Y) + r(X ∩ Y) (Submodularity)
    if not clearly_submodular:
        for X, Y in combinations(powset(E), 2):
            if r(X) + r(Y) < r(X | Y) + r (X & Y):
                return False

    return True


def satisfies_nulity_function_axiom( maybe_matroid                      : tuple[set[T], Callable[[set[T]], int]]
                                   , clearly_bounded_above_by_cardinality : bool=False
                                   , clearly_inequal_with_distribution    : bool=False
                                   , clearly_supermodular                 : bool=False) -> bool:
    """Judge whether the given pair of a ground set and a function from set to non-negative integers is a matroid.
    This is done due to the axiom of a nulity function.

    Args:
        maybe_matroid (tuple[set[T], Callable[[set[T]], int]): A tuple (E, n), where E is a ground set and n is a function.
        clearly_bounded_above_by_cardinality (bool, optional): If this is True, the check of (N1) will be skipped. Defaults to False.
        clearly_inequal_with_distribution    (bool, optional): If this is True, the check of (N2) will be skipped. Defaults to False.
        clearly_supermodular                 (bool, optional): If this is True, the check of (N3) will be skipped. Defaults to False.

    Returns:
        bool: True if the given family satisfies the axiom of a nulity function, otherwise False.
    """
    E, n = maybe_matroid
    # (N1) ∀X ⊆ E, 0 ≦ n(X) ≦ |X|
    if not clearly_bounded_above_by_cardinality:
        for X in powset(E):
            if not (0 <= n(X) <= len(X)):
                return False
    
    # (N2) X ⊆ Y ⊆ E => n(Y) - n(X) ≦ |Y - X|
    if not clearly_inequal_with_distribution:
        for Y in powset(E):
            for X in powset(Y):
                if n(Y) - n(X) > len(Y - X):
                    return False

    # (R3) ∀X, Y ⊆ E, n(X) + n(Y) ≦ n(X ∪ Y) + n(X ∩ Y) (Supermodularity)
    if not clearly_supermodular:
        for X, Y in combinations(powset(E), 2):
            if n(X) + n(Y) > n(X | Y) + n(X & Y):
                return False

    return True


def satisfies_closure_axiom( maybe_matroid                        : tuple[set[T], Callable[[set[T]], set[T]]]
                           , clearly_increasing                   : bool=False
                           , clearly_monotonic                    : bool=False
                           , clearly_MacLane_Steinitz_exchangable : bool=False) -> bool:
    """Judge whether the given pair of a ground set and a function from set to set is a matroid.
    This is done due to the axiom of a closure operator.

    Args:
        maybe_matroid (tuple[set[T], Callable[[set[T]], set[T]]]): A tuple (E, cl), where E is a ground set and cl is a function.
        clearly_increasing                   (bool, optional): If this is True, the check of (Cl1) will be skipped. Defaults to False.
        clearly_monotonic                    (bool, optional): If this is True, the check of (Cl2) will be skipped. Defaults to False.
        clearly_MacLane_Steinitz_exchangable (bool, optional): If this is True, the check of (Cl3) will be skipped. Defaults to False.

    Returns:
        bool: True if the given family satisfies the axiom of a closure operator, otherwise False.
    """
    E, cl = maybe_matroid
    
    # (Cl1) ∀X ⊆ E, X ⊆ cl(X) (increasing)
    if not clearly_increasing:
        for X in powset(E):
            if not (X <= cl(X)):
                return False
    
    # (Cl2) ∀X, Y ⊆ E, X ⊆ cl(Y) => cl(X) ⊆ cl(Y) (monotonic)
    if not clearly_monotonic:
        for Y in powset(E):
            for X in powset(cl(Y)):
                if not (cl(X) <= cl(Y)):
                    return False

    # (Cl3) ∀X ⊆ E, ∀e1 ∈ E, e2 ∈ (X ∪ {e1}) - cl(X) => e1 ∈ cl(X ∪ {e2}) - cl(X)  (Mac Lane-Steinitz exchange property)
    if not clearly_MacLane_Steinitz_exchangable:
        for X in powset(E):
            for e1 in E:
                for e2 in (e2 for e2 in E if e2 in (X | {e1}) - cl(X)):
                    if e1 not in cl(X | {e2}) - cl(X):
                        return False
    
    return True


def satisfies_flats_axiom( maybe_matroid                        : tuple[set[T], list[set[T]]]
                         , clearly_has_ground_set               : bool=False
                         , clearly_closed_by_intersection       : bool=False
                         , clearly_complement_partitionable     : bool=False) -> bool:
    """Judge whether the given pair of a ground set and a collection of subsets is a matroid.
    This is done due to the axiom of flats.

    Args:
        maybe_matroid (tuple[set[T], list[set[T]]]): A tuple (E, Fs), where E is a ground set and Fs is a family of subsets of E.
        clearly_has_ground_set (bool, optional)          : If this is True, the check of (F1) will be skipped. Defaults to False.
        clearly_closed_by_intersection (bool, optional)  : If this is True, the check of (F2) will be skipped. Defaults to False.
        clearly_complement_partitionable (bool, optional): If this is True, the check of (F3) will be skipped. Defaults to False.

    Returns:
        bool: True if the given family satisfies the axiom of flats, False otherwise.
    """
    E, Fs = maybe_matroid

    # (F1) E ∈ Fs
    if not clearly_has_ground_set and E not in Fs:
        return False
    
    # (F2) F1, F2 ∈ Fs => F1 ∩ F2 ∈ Fs
    if not clearly_closed_by_intersection and any(map(lambda F1, F2: F1 & F2 not in Fs ,combinations(Fs, 2))):
        return False
    
    # TODO: Implement the check of (F3)
    # (F3) F ∈ Fs and {F1,F2, ..., Fk} is the set of minimal members of Fs s.t. F ⊊ ∪[i∈{1..k}] Fi,
    #      F1 - F, F2 - F, ... , Fk - F partitions E - F.
    if not clearly_complement_partitionable:
        for F in Fs:
            pass
    
    return True


def satisfies_open_sets_axiom( maybe_matroid          : tuple[set[T], list[set[T]]]
                             , clearly_has_emptyset   : bool=False
                             , clearly_closed_by_union: bool=False
                             , clearly_exists_another : bool=False) -> bool:
    """Judge whether the given pair of a ground set and a collection of subsets is a matroid.
    This is done due to the axiom of open sets.

    Args:
        maybe_matroid (tuple[set[T], list[set[T]]]): A tuple (E, Os), where E is a ground set and Os is a family of subsets of E.
        clearly_has_emptyset (bool, optional)   : If this is True, the check of (O1) will be skipped. Defaults to False.
        clearly_closed_by_union (bool, optional): If this is True, the check of (O2) will be skipped. Defaults to False.
        clearly_exists_another (bool, optional) : If this is True, the check of (O3) will be skipped. Defaults to False.

    Returns:
        bool: True if the given family satisfies the axiom of open sets, False otherwise.
    """
    E, Os = maybe_matroid

    # [Prerequisits] O ∈ Os => O ⊆ E
    if not all(map(lambda O: O <= E, Os)):
        return False

    # (O1) ∅ ∈ Os
    if (not clearly_has_emptyset) and (set() not in Os):
        print("Hey")
        return False
    
    # (O2) O1, O2 ∈ Os => O1 ∪ O2 ∈ Os
    if not clearly_closed_by_union:
        for (O1, O2) in combinations(Os, 2):
            if O1 | O2 not in Os:
                return False
    
    # (O3) ∀O1, O2 ∈ Os, ∀o ∈ O1 ∩ O2, ∃O3 ∈ Os s.t. (O1 ∪ O2)\(O1 ∩ O2) ⊆ O3 ⊊ (O1 ∪ O2)\{o}
    if not clearly_exists_another:
        for O1, O2 in combinations(Os, 2):
            for o in O1 & O2:
                if not any(map(lambda O3: ((O1 | O2) - (O1 & O2)) <= O3 < (O1 | O2 - {o}), Os)):
                    return False
    return True


def satisfies_hyperplanes_axiom( maybe_matroid: tuple[set[T], list[set[T]]]
                               , clearly_has_no_ground_set: bool=False
                               , clearly_clutter          : bool=False
                               , clearly_exists_another   : bool=False) -> bool:
    """Judge whether the given pair of a ground set and a collection of subsets is a matroid.
    This is done due to the axiom of hyperplanes.

    Args:
        maybe_matroid (tuple[set[T], list[set[T]]]): A tuple (E, Hs), where E is a ground set and Hs is a family of subsets of E.
        clearly_has_no_ground_set (bool, optional): If this is True, the check of (H1) will be skipped. Defaults to False.
        clearly_clutter (bool, optional)          : If this is True, the check of (H2) will be skipped. Defaults to False.
        clearly_exists_another (bool, optional)   : If this is True, the check of (H3) will be skipped. Defaults to False.
    
    Returns:
        bool: True if the given family satisfies the axiom of hyperplanes, False otherwise.
    """
    E, Hs = maybe_matroid
    # [Prerequisits] H ∈ Hs => H ⊆ E
    if any(map(lambda H: not H <= E, Hs)):
        return False
    
    # (H1) E ∉ Hs
    if (not clearly_has_no_ground_set) and (E in Hs):
        return False
    
    # (H2) H1, H2 ∈ Hs and H1 ⊆ H2 => H1 = H2
    if not clearly_clutter:
        for H1, H2 in combinations(Hs, 2):
            if ((H1 <= H2) or (H2 <= H1)) and H1 != H2:
                return False
    
    # (H3) H1, H2 ∈ Hs with H1 ≠ H2 and e ∈ E - (H1 ∪ H2) => ∃H3 ∈ Hs s.t. (H1 ∩ H2) ∪ {e} ⊆ H3.
    if not clearly_exists_another:
        for H1, H2 in combinations(Hs, 2):
            for e in (E - (H1 | H2)):
                if not any(map(lambda H3: ((H1 & H2) | {e}) <= H3, Hs)):
                    return False
    return True


def satisfies_spanning_sets_axiom( maybe_matroid: tuple[set[T], list[set[T]]]
                                 , clearly_has_ground_set     : bool=False
                                 , clearly_opposite_hereditary: bool=False
                                 , clearly_exists_decrement   : bool=False) -> bool:
    """Judge whether the given pair of a ground set and a collection of subsets is a matroid.
    This is done due to the axiom of spanning sets.

    Args:
        maybe_matroid (tuple[set[T], list[set[T]]]): A tuple (E, Ss), where E is a ground set and Ss is a family of subsets of E.
        clearly_has_ground_set (bool, optional)     : If this is True, the check of (S1) will be skipped. Defaults to False.
        clearly_opposite_hereditary (bool, optional): If this is True, the check of (S2) will be skipped. Defaults to False.
        clearly_exists_decrement (bool, optional)   : If this is True, the check of (S3) will be skipped. Defaults to False.

    Returns:
        bool: True if the given family satisfies the axiom of hyperplanes, False otherwise.
    """
    E, Ss = maybe_matroid
    # [Prerequisits] S ∈ Ss => S ⊆ Ss
    if any(map(lambda S: not S <= E, Ss)):
        return False
    
    # (S1) E ∈ Ss
    if (not clearly_has_ground_set) and (E not in Ss):
        return False
    
    # (S2) S1 ∈ Ss and S1 ⊆ S2 => S2 ∈ Ss
    if not clearly_opposite_hereditary:
        for S1 in Ss:
            if any(map(lambda S2: (S1 <= S2) and (S2 not in Ss), powset(E))):
                return False
    
    # (S3) S1, S2 ∈ Ss and |S1| < |S2| => ∃s∈S2-S1 s.t. S2\{s} ∈ Ss.
    if not clearly_exists_decrement:
        for S1, S2 in combinations(Ss, 2):
            if len(S1) == len(S2):
                continue
            smaller, larger = (S1, S2) if len(S1) < len(S2) else (S2, S1)
            if not any(map(lambda s: S2 - {s} in Ss, larger - smaller)):
                return False
    
    return True

def satisfies_girth_function_axiom( maybe_matroid: tuple[set[T], Callable[[set[T]], Union[int, float]]]
                                  , clearly_decrementable: bool=False
                                  , clearly_monotonic_decrease: bool=False
                                  , clearly_symmetric_finite: bool=False) -> bool:
    """Judge whether the given pair of a ground set and a collection of subsets is a matroid.
    This is done due to the axiom of a girth function.

    Args:
        maybe_matroid (tuple[set[T], Callable[[set[T]], Union[int, float]]]): A matroid defined by a girth function.
        clearly_decrementable (bool, optional): If this is True, the check of (G1) will be skipped. Defaults to False.
        clearly_monotonic_decrease (bool, optional): If this is True, the check of (G2) will be skipped. Defaults to False.
        clearly_symmetric_finite (bool, optional): If this is True, the check of (G3) will be skipped. Defaults to False.

    Returns:
        bool: True if the given family satisfies the axiom of a girth function, False otherwise.
    """
    E, g = maybe_matroid

    # (G1) X ⊆ E and g(X) < ∞ => ∃Y ⊊ X s.t. g(X) = g(Y) = |Y|.
    if not clearly_decrementable:
        for X in powset(E):
            if g(X) < inf:
                if not any((g(X) == g(Y)) and (g(Y) == len(Y)) for Y in powset(X)):
                    return False
    
    # (G2) X ⊆ Y ⊆ E => g(X) ≧ g(Y).
    if not clearly_monotonic_decrease:
        for Y in powset(E):
            for X in powset(Y):
                if g(X) < g(Y):
                    return False
    
    # (G3) X, Y ⊆ E with X ≠ Y, g(X) = |X|, g(Y) = |Y|, and e ∈ X ∩ Y => g((X∪Y)\{e}) < ∞
    if not clearly_symmetric_finite:
        for X, Y in combinations(powset(E),2):
            if (g(X) != len(X)) or (g(Y) != len(Y)) or X.isdisjoint(Y):
                continue
            for e in X & Y:
                if g((X | Y) - {e}) == inf:
                    return False
    return True