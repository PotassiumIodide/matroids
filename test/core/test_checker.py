import pytest

from matroids.core.checker import (
    satisfies_independent_axiom,
    satisfies_dependent_axiom,
    satisfies_bases_axiom,
    satisfies_circuits_axiom,
    satisfies_rank_function_axiom,
    satisfies_nulity_function_axiom,
    satisfies_closure_axiom,
    satisfies_open_sets_axiom,
    satisfies_hyperplanes_axiom,
    satisfies_spanning_sets_axiom,
)


@pytest.mark.parametrize('maybe_matroid, expected', [
    (( {1,2,3}, [set()] )                                      ,  True),
    (( {1,2,3}, [set(),{1}] )                                  ,  True),
    (( {1,2,3}, [set(),{1},{2}] )                              ,  True),
    (( {1,2,3}, [set(),{1},{2},{3}] )                          ,  True),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        ,  True),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3}] )              ,  True),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3}] )        ,  True),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),  True),
    (( {1,2,3}, [{1},{2},{3}] )                                , False),
    (( {1,2,3}, [set(),{1},{2},{3},{1,3}] )                    , False),
    (( {1,2,3}, [set(),{1},{1,2}] )                            , False),
    (( {1,2}  , [set(),{1},{2},{3},{1,2},{1,3}] )              , False), 
    (( {4,5,6}, [set(),{1},{2},{3},{1,2},{1,3}] )              , False),
])
def test_satisfies_independent_axiom(maybe_matroid, expected):
    assert satisfies_independent_axiom(maybe_matroid) == expected


@pytest.mark.parametrize('maybe_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),  True),
    (( {1,2,3}, [{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )    ,  True),
    (( {1,2,3}, [{3},{1,2},{1,3},{2,3},{1,2,3}] )        ,  True),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )            ,  True),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )              ,  True),
    (( {1,2,3}, [{2,3},{1,2,3}] )                        ,  True),
    (( {1,2,3}, [{1,2,3}] )                              ,  True),
    (( {1,2,3}, [] )                                     ,  True),
    (( {1,2,3}, [set(),{1,2},{1,3},{2,3},{1,2,3}] )      , False),
    (( {1,2,3}, [{1,2},{2,3},{1,2,3}] )                  , False),
    (( {1,2,3}, [{2},{3},{1,3},{2,3},{1,2,3}] )          , False),
    (( {1,2}  , [{2,3},{1,2,3}] )                        , False), 
    (( {4,5,6}, [{2,3},{1,2,3}] )                        , False),
])
def test_satisfies_dependent_axiom(maybe_matroid, expected):
    assert satisfies_dependent_axiom(maybe_matroid) == expected


@pytest.mark.parametrize('maybe_matroid, expected', [
    (( {1,2,3}, [set()] )            ,  True),
    (( {1,2,3}, [{1}] )              ,  True),
    (( {1,2,3}, [{1},{2}] )          ,  True),
    (( {1,2,3}, [{1},{2},{3}] )      ,  True),
    (( {1,2,3}, [{1,2}] )            ,  True),
    (( {1,2,3}, [{1,2},{1,3}] )      ,  True),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ),  True),
    (( {1,2,3}, [{1,2,3}] )          ,  True),
    (( {1,2,3}, [{1},{2,3}] )        , False),
    (( {1,2,3}, [{1,4},{2,3}] )      , False),
    (( {4,5,6}, [{1,2},{1,3}] )      , False),
    (( {1,2,3}, [] )                 , False)
])
def test_satisfies_bases_axiom(maybe_matroid, expected):
    assert satisfies_bases_axiom(maybe_matroid) == expected


@pytest.mark.parametrize('maybe_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3}] )      ,  True),
    (( {1,2,3}, [{2},{3}] )          ,  True),
    (( {1,2,3}, [{3},{1,2}] )        ,  True),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ),  True),
    (( {1,2,3}, [{3}] )              ,  True),
    (( {1,2,3}, [{2,3}] )            ,  True),
    (( {1,2,3}, [{1,2,3}] )          ,  True),
    (( {1,2,3}, [] )                 ,  True),
    (( {1,2,3}, [{1,3},{2,3}] )      , False),
    (( {1,2,3}, [{1},{1,2}] )        , False),
    (( {4,5,6}, [{1,2},{3}] )        , False),
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
    (( {1,2,3}, lambda X: 0 )                                   ,  True),
    (( {1,2,3}, lambda X: 1 if 1 in X else 0 )                  ,  True),
    (( {1,2,3}, lambda X: 0 if X <= {3} else 1 )                ,  True),
    (( {1,2,3}, lambda X: 1 if X else 0 )                       ,  True),
    (( {1,2,3}, lambda X: len(X) - 1 if 3 in X else len(X) )    ,  True),
    (( {1,2,3}, lambda X: len(X) - 1 if {2,3} <= X else len(X) ),  True),
    (( {1,2,3}, lambda X: 2 if X == {1,2,3} else len(X) )       ,  True),
    (( {1,2,3}, len )                                           ,  True),
    (( {1,2,3}, lambda x: len(x) if x else 1 )                  , False),
    (( {1,2,3}, lambda x: 0 if x == {1, 2, 3} or not x else 1 ) , False),
    (( {1,2,3}, lambda x: 2 * len(x) )                          , False),
    (( {1,2,3}, f )                                             , False),
    (( set()  , lambda x: 1 )                                   , False),
])
def test_satisfies_rank_function_axiom(maybe_matroid, expected):
    assert satisfies_rank_function_axiom(maybe_matroid) == expected


@pytest.mark.parametrize('maybe_matroid, expected', [
    (( {1,2,3}, len )                                                      ,  True),
    (( {1,2,3}, lambda X: len(X) - 1 if 1 in X else len(X) )               ,  True),
    (( {1,2,3}, lambda X: len(X) if X <= {3} else len(X) - 1 )             ,  True),
    (( {1,2,3}, lambda X: len(X) - 1 if X else len(X) )                    ,  True),
    (( {1,2,3}, lambda X: 1 if 3 in X else 0 )                             ,  True),
    (( {1,2,3}, lambda X: 1 if {2,3} <= X else 0 )                         ,  True),
    (( {1,2,3}, lambda X: len(X) - 2 if X == {1,2,3} else 0 )              ,  True),
    (( {1,2,3}, lambda X: 0 )                                              ,  True),
    (( {1,2,3}, lambda X: 0 if X else len(X) - 1 )                         , False),
    (( {1,2,3}, lambda X: len(X) if X == {1,2,3} or not X else len(X) - 1 ), False),
    (( {1,2,3}, lambda X: 2 * len(X))                                      , False),
    (( {1,2,3}, lambda X: len(X) - f(X) )                                  , False),
    (( set()  , lambda X: len(X) - 1 )                                     , False),
])
def test_satisfies_nulity_function_axiom(maybe_matroid, expected):
    assert satisfies_nulity_function_axiom(maybe_matroid) == expected


# functions for checking the closure axiom.
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
    (( {1,2,3}, lambda X: {1,2,3} )                      ,  True),
    (( {1,2,3}, lambda X: {1,2,3} if 1 in X else {2,3} ) ,  True),
    (( {1,2,3}, lambda X: {3} if X <= {3} else {1,2,3} ) ,  True),
    (( {1,2,3}, lambda X: {1,2,3} if X else X )          ,  True),
    (( {1,2,3}, lambda X: X | {3} )                      ,  True),
    (( {1,2,3}, lambda X: X if X <= {1} else X | {2,3} ) ,  True),
    (( {1,2,3}, lambda X: X if len(X) <= 1 else {1,2,3} ),  True),
    (( {1,2,3}, lambda X: X )                            ,  True),
    (( {1,2,3}, lambda x: x if x else {1, 2, 3} )        , False),
    (( {1,2,3}, lambda x: {1} )                          , False),
    (( {1,2,3}, lambda x: {1, 2, 3} - x )                , False),
    (( {1,2,3}, ncl1 )                                   , False),
    (( {1,2,3}, ncl2 )                                   , False),
])
def test_satisfies_closure_function_axiom(maybe_matroid, expected):
    assert satisfies_closure_axiom(maybe_matroid) == expected


@pytest.mark.parametrize('maybe_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , True ),
    (( {1,2,3}, [set(),{1}] )                                  , True ),
    (( {1,2,3}, [set(),{1,2}] )                                , True ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , True ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , True ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , True ),
    (( {1,2,3}, [set(),{1,2},{1,3},{2,3},{1,2,3}] )            , True ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), True ),
    (( {1,2,3}, [set(),{1,3},{2,3}] )                          , False),
    (( {1,2,3}, [set(),{1},{1,2},{1,2,3}] )                    , False),
    (( {4,5,6}, [set(),{1},{2},{1,2}] )                        , False),
])
def test_satisfies_open_sets_axiom(maybe_matroid, expected):
    assert satisfies_open_sets_axiom(maybe_matroid) == expected


@pytest.mark.parametrize('maybe_matroid, expected', [
    (( {1,2,3}, [] )                         , True ),
    (( {1,2,3}, [{2,3}] )                    , True ),
    (( {1,2,3}, [{3}] )                      , True ),
    (( {1,2,3}, [set()] )                    , True ),
    (( {1,2,3}, [{1,3},{2,3}] )              , True ),
    (( {1,2,3}, [{1},{2,3}] )                , True ),
    (( {1,2,3}, [{1},{2},{3}] )              , True ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] )        , True ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] ), False),
    (( {1,2,3}, [{3},{1,3},{2,3}] )          , False),
    (( {1,2,3}, [{1},{2}] )                  , False),
    (( {4,5,6}, [{1,2},{1,3},{2,3}] )        , False),
])
def test_satisfies_hyperplanes_axiom(maybe_matroid, expected):
    assert satisfies_hyperplanes_axiom(maybe_matroid) == expected


@pytest.mark.parametrize('maybe_matroid, expected', [
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), True ),
    (( {1,2,3}, [{1},{1,2},{1,3},{1,2,3}] )                    , True ),
    (( {1,2,3}, [{1},{2},{1,2},{1,3},{2,3},{1,2,3}] )          , True ),
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )      , True ),
    (( {1,2,3}, [{1,2},{1,2,3}] )                              , True ),
    (( {1,2,3}, [{1,2},{1,3},{1,2,3}] )                        , True ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )                  , True ),
    (( {1,2,3}, [{1,2,3}] )                                    , True ),
    (( {1,2,3}, [] )                                           , False),
    (( {1,2,3}, [set(),{1},{1,2},{1,3}] )                      , False),
    (( {1,2,3}, [{1},{2},{3},{1,2},{2,3},{1,2,3}] )            , False),
    (( {4,5,6}, [{1,2},{1,2,3}] )                              , False),
])
def test_satisfies_spanning_sets_axiom(maybe_matroid, expected):
    assert satisfies_spanning_sets_axiom(maybe_matroid) == expected