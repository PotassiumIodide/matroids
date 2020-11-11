import pytest

from src.matroids.checker import (
    satisfies_independent_axiom,
    satisfies_dependent_axiom,
    satisfies_bases_axiom,
    satisfies_circuits_axiom,
    satisfies_rank_function_axiom,
    satisfies_closure_axiom,
)


@pytest.mark.parametrize('maybe_matroid, expected', [
    (( {1, 2, 3}, [set(), {1}, {2}, {3}, {1, 2}, {1, 3}]                    ),  True),
    (( {1, 2, 3}, [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}]            ),  True),
    (( {1, 2, 3}, [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}] ),  True),
    (( {1, 2, 3}, [{1}, {2}, {3}]                                           ), False),
    (( {1, 2, 3}, [set(), {1}, {2}, {3}, {1, 3}]                            ), False),
    (( {1, 2, 3}, [set(), {1}, {1, 2}]                                      ), False),
    (( {1, 2}   , [set(), {1}, {2}, {3}, {1, 2}, {1, 3}]                    ), False), 
    (( {4, 5, 6}, [set(), {1}, {2}, {3}, {1, 2}, {1, 3}]                    ), False),
])
def test_satisfies_independent_axiom(maybe_matroid, expected):
    assert satisfies_independent_axiom(maybe_matroid) == expected


@pytest.mark.parametrize('maybe_matroid, expected', [
    (( {1, 2, 3}, [{2, 3}, {1, 2, 3}] )                       ,  True),
    (( {1, 2, 3}, [{1, 2, 3}] )                               ,  True),
    (( {1, 2, 3}, [] )                                        ,  True),
    (( {1, 2, 3}, [set(), {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}] ), False),
    (( {1, 2, 3}, [{1, 2}, {2, 3}, {1, 2, 3}] )               , False),
    (( {1, 2, 3}, [{2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}] )     , False),
    (( {1, 2}   , [{2, 3}, {1, 2, 3}] )                       , False), 
    (( {4, 5, 6}, [{2, 3}, {1, 2, 3}] )                       , False),
])
def test_satisfies_dependent_axiom(maybe_matroid, expected):
    assert satisfies_dependent_axiom(maybe_matroid) == expected


@pytest.mark.parametrize('maybe_matroid, expected', [
    (( {1, 2, 3}, [set()]          ),  True),
    (( {1, 2, 3}, [{1}, {2}, {3}]  ),  True),
    (( {1, 2, 3}, [{1, 2}, {1, 3}] ),  True),
    (( {1, 2, 3}, [{1, 2, 3}]      ),  True),
    (( {1, 2, 3}, [{1}, {2, 3}]    ), False),
    (( {1, 2, 3}, [{1, 4}, {2, 3}] ), False),
    (( {4, 5, 6}, [{1, 2}, {1, 3}] ), False),
    (( {1, 2, 3}, []               ), False)
])
def test_satisfies_bases_axiom(maybe_matroid, expected):
    assert satisfies_bases_axiom(maybe_matroid) == expected


@pytest.mark.parametrize('maybe_matroid, expected', [
    (( {1, 2, 3}, [{3}]            ),  True),
    (( {1, 2, 3}, [{1}, {2}, {3}]  ),  True),
    (( {1, 2, 3}, [{1, 2}, {3}]    ),  True),
    (( {1, 2, 3}, [{1, 2, 3}]      ),  True),
    (( {1, 2, 3}, []               ),  True),
    (( {1, 2, 3}, [{1, 3}, {2, 3}] ), False),
    (( {1, 2, 3}, [{1}, {1, 2}]    ), False),
    (( {4, 5, 6}, [{1, 2}, {3}]    ), False),
])
def test_satisfies_circuits_axiom(maybe_matroid, expected):
    assert satisfies_circuits_axiom(maybe_matroid) == expected


# function for checking the rank funciton axiom.
def f(x: set) -> int:
    if not x:
        return 0
    elif x == {1, 2} or x == {1, 2, 3}:
        return 2
    else:
        return 1


@pytest.mark.parametrize('maybe_matroid, expected', [
    (( {1, 2, 3}, len                                                     ),  True),
    (( {1, 2, 3}, lambda x: 2 if x == {1, 2, 3} else len(x)               ),  True),
    (( {1, 2, 3}, lambda x: 1 if x else 0                                 ),  True),
    (( {1, 2, 3}, lambda x: len(x)-1 if x in [{1,2,3}, {2,3}] else len(x) ),  True),
    (( set()    , lambda x: 0                                             ),  True),
    (( {1, 2, 3}, lambda x: len(x) if x else 1                  ), False),
    (( {1, 2, 3}, lambda x: 0 if x == {1, 2, 3} or not x else 1 ), False),
    (( {1, 2, 3}, lambda x: 2 * len(x)                          ), False),
    (( {1, 2, 3}, f                                             ), False),
    (( set()    , lambda x: 1                                   ), False),
])
def test_satisfies_rank_function_axiom(maybe_matroid, expected):
    assert satisfies_rank_function_axiom(maybe_matroid) == expected


# functions for checking the closure axiom.
def cl(x: set[int]) -> set[int]:
    if x in [set(), {1}]:
        return x
    elif x in [{2}, {3}, {2, 3}]:
        return {2, 3}
    else:
        return {1, 2, 3}


def ncl1(x: set[int]) -> set[int]:
    if x == {1,2,3} or not x:
        return set()
    elif x in [{1}, {2}, {3}]:
        return {1, 2, 3}
    else:
        return x


def ncl2(x: set[int]) -> set[int]:
    if x in [{3}, {1,2}, {1,2,3}]:
        return {1,2,3}
    elif x in [{1}, {1,3}]:
        return {1,3}
    elif x in [{2}, {2,3}]:
        return {2,3}
    else:
        return set()


@pytest.mark.parametrize('maybe_matroid, expected', [
    (( {1, 2, 3}, lambda x: x                               ),  True),
    (( {1, 2, 3}, lambda x: x if len(x) <= 1 else {1, 2, 3} ),  True),
    (( {1, 2, 3}, lambda x: {1, 2, 3} if x else x           ),  True),
    (( {1, 2, 3}, cl                                        ),  True),
    (( set()    , lambda x: x                               ),  True),
    (( {1, 2, 3}, lambda x: x if x else {1, 2, 3}           ), False),
    (( {1, 2, 3}, lambda x: {1}                             ), False),
    (( {1, 2, 3}, lambda x: {1, 2, 3} - x                   ), False),
    (( {1, 2, 3}, ncl1                                      ), False),
    (( {1, 2, 3}, ncl2                                      ), False),
])
def test_satisfies_closure_function_axiom(maybe_matroid, expected):
    assert satisfies_closure_axiom(maybe_matroid) == expected