from functools import reduce
from itertools import chain, combinations
from operator import or_
from typing import Any, Iterable, TypeVar

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
    return bool(someset) and all(map(lambda X: (X == set()) or not (X < someset), set_collection))


def find_minimal_sets(set_collection: list[set[T]]) -> list[set[T]]:
    """Find all of the minimal set in a given collection of sets

    Args:
        set_collection (list[set[T]]): A collection of sets

    Returns:
        list[set[T]]: All of the minimal sets in the given collection of sets.
    """
    return [s for s in set_collection if is_minimal(s, set_collection)]


def is_maximal(someset: set[T], set_collection: list[set[T]]) -> bool:
    """Check whether the given set is no subset of all members in a given collection of sets.

    Args:
        someset (set): A set expected to be maximal.
        set_collection (list[set]): A collection of sets for this judgement.

    Returns:
        bool: True if the given set is maximal, otherwise False
    """
    return all(map(lambda X: not (someset < X), set_collection))


def find_maximal_sets(set_collection: list[set[T]]) -> list[set[T]]:
    """Find all of the maximal set in a given collection of sets

    Args:
        set_collection (list[set[T]]): A collection of sets

    Returns:
        list[set[T]]: All of the minimal sets in the given collection of sets.
    """
    return [s for s in set_collection if is_maximal(s, set_collection)]


infinite = 99999999
# α(M)を求めるための関数
def _search_node(setE={}, setU=[{}], setS={}, num=0, d=0, length=0):
    ans = [infinite]
    if d >= length:
        return infinite
    for i in range(d, length):
        if (setU[i] - setS) != set():  # setSにない要素がある=>必ずsetEの要素
            if setE == setS | setU[i]:  # i番目の要素を追加することでEを満たしたらその場でノードの最小値として返す
                return num+1
            ans.append(_search_node(setE, setU, setS | setU[i], num+1, i+1, length))
    return min(ans)


def revlex_sort_key(s: set[T]) -> tuple[T]:
    """This is the key for sorted function to sort a list of set in reverse lexicographic order.

    Args:
        s (set[T]): A set.

    Returns:
        tuple[list[T]]: Sorted list in reverse lexicographic order.
    """
    return tuple(reversed(s))
