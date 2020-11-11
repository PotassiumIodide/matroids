from itertools import chain, combinations
from typing import TypeVar

T = TypeVar('T')

def powset(E: set[T]) -> list[set[T]]:
    """Return the power set, a set of all subsets, of a given set E

    Arguments:
        E: {set} - a ground set

    Returns:
        {list[set]} - the power set of a given set E.
    """
    return [*map(set, chain.from_iterable(combinations(E, r) for r in range(len(E)+1)))]


def is_minimal(someset: set[T], set_collection: list[set[T]]) -> bool:
    """Check whether the given set is no super set of all members in a given collection of sets.

    Args:
        someset (set): A set expected to be minimal.
        set_collection (list[set]): A collection of sets for this judgement.

    Returns:
        bool: True if the given set is minimal, otherwise False
    """
    for s in set_collection:
        if s == someset or not s:
            continue
        elif s <= someset:
            return False
    return True


def find_minimal_sets(set_collection: list[set[T]]) -> list[set[T]]:
    """Find all of the minimal set in a given collection of sets

    Args:
        set_collection (list[set[T]]): A collection of sets

    Returns:
        list[set[T]]: All of the minimal sets in the given collection of sets.
    """
    return [s for s in set_collection if is_minimal(s, set_collection) and s]


def is_maximal(someset: set[T], set_collection: list[set[T]]) -> bool:
    """Check whether the given set is no subset of all members in a given collection of sets.

    Args:
        someset (set): A set expected to be maximal.
        set_collection (list[set]): A collection of sets for this judgement.

    Returns:
        bool: True if the given set is maximal, otherwise False
    """
    for s in set_collection:
        if s == someset or not s:
            continue
        elif someset <= s:
            return False
    return True


def find_maximal_sets(set_collection: list[set[T]]) -> list[set[T]]:
    """Find all of the maximal set in a given collection of sets

    Args:
        set_collection (list[set[T]]): A collection of sets

    Returns:
        list[set[T]]: All of the minimal sets in the given collection of sets.
    """
    return [s for s in set_collection if is_maximal(s, set_collection)]