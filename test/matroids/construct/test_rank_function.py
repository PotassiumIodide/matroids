import pytest

from utils.set_operator import powset

from src.matroids.construct.rank_function import (
    from_independent_matroid,
    from_dependent_matroid,
    from_bases_matroid,
    from_circuits_matroid,
    from_closure_matroid,
    from_flats_matroid,
    from_open_matroid,
    from_hyperplanes_matroid,
    from_spanning_matroid,
)


@pytest.mark.parametrize('independent_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , lambda X: 0                                    ),
    (( {1,2,3}, [set(),{1}] )                                  , lambda X: 1 if 1 in X else 0                   ),
    (( {1,2,3}, [set(),{1},{2}] )                              , lambda X: 0 if X <= {3} else 1                 ),
    (( {1,2,3}, [set(),{1},{2},{3}] )                          , lambda X: 1 if X else 0                        ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , lambda X: len(X) - 1 if 3 in X else len(X)     ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3}] )              , lambda X: len(X) - 1 if {2,3} <= X else len(X) ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3}] )        , lambda X: 2 if X == {1,2,3} else len(X)        ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), len                                            ),
])
def test_from_independent_matroid(independent_matroid, expected):
    E, _ = independent_matroid
    r1 = from_independent_matroid(independent_matroid)
    r2 = expected
    assert all(r1(X) == r2(X) for X in powset(E))


@pytest.mark.parametrize('dependent_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), lambda X: 0                                    ),
    (( {1,2,3}, [{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )    , lambda X: 1 if 1 in X else 0                   ),
    (( {1,2,3}, [{3},{1,2},{1,3},{2,3},{1,2,3}] )        , lambda X: 0 if X <= {3} else 1                 ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )            , lambda X: 1 if X else 0                        ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )              , lambda X: len(X) - 1 if 3 in X else len(X)     ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                        , lambda X: len(X) - 1 if {2,3} <= X else len(X) ),
    (( {1,2,3}, [{1,2,3}] )                              , lambda X: 2 if X == {1,2,3} else len(X)        ),
    (( {1,2,3}, [] )                                     , len                                            ),
])
def test_from_dependent_matroid(dependent_matroid, expected):
    E, _ = dependent_matroid
    r1 = from_dependent_matroid(dependent_matroid)
    r2 = expected
    assert all(r1(X) == r2(X) for X in powset(E))


@pytest.mark.parametrize('bases_matroid, expected', [
    (( {1,2,3}, [set()] )            , lambda X: 0                                    ),
    (( {1,2,3}, [{1}] )              , lambda X: 1 if 1 in X else 0                   ),
    (( {1,2,3}, [{1},{2}] )          , lambda X: 0 if X <= {3} else 1                 ),
    (( {1,2,3}, [{1},{2},{3}] )      , lambda X: 1 if X else 0                        ),
    (( {1,2,3}, [{1,2}] )            , lambda X: len(X) - 1 if 3 in X else len(X)     ),
    (( {1,2,3}, [{1,2},{1,3}] )      , lambda X: len(X) - 1 if {2,3} <= X else len(X) ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), lambda X: 2 if X == {1,2,3} else len(X)        ),
    (( {1,2,3}, [{1,2,3}] )          , len                                            ),
])
def test_from_bases_matroid(bases_matroid, expected):
    E, _ = bases_matroid
    r1 = from_bases_matroid(bases_matroid)
    r2 = expected
    assert all(r1(X) == r2(X) for X in powset(E))


@pytest.mark.parametrize('circuits_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3}] )      , lambda X: 0                                    ),
    (( {1,2,3}, [{2},{3}] )          , lambda X: 1 if 1 in X else 0                   ),
    (( {1,2,3}, [{3},{1,2}] )        , lambda X: 0 if X <= {3} else 1                 ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), lambda X: 1 if X else 0                        ),
    (( {1,2,3}, [{3}] )              , lambda X: len(X) - 1 if 3 in X else len(X)     ),
    (( {1,2,3}, [{2,3}] )            , lambda X: len(X) - 1 if {2,3} <= X else len(X) ),
    (( {1,2,3}, [{1,2,3}] )          , lambda X: 2 if X == {1,2,3} else len(X)        ),
    (( {1,2,3}, [] )                 , len                                            ),
])
def test_from_circuits_matroid(circuits_matroid, expected):
    E, _ = circuits_matroid
    r1 = from_circuits_matroid(circuits_matroid)
    r2 = expected
    assert all(r1(X) == r2(X) for X in powset(E))


@pytest.mark.parametrize('closure_matroid, expected', [
    (( {1,2,3}, lambda X: {1,2,3} )                      , lambda X: 0                                    ),
    (( {1,2,3}, lambda X: {1,2,3} if 1 in X else {2,3} ) , lambda X: 1 if 1 in X else 0                   ),
    (( {1,2,3}, lambda X: {3} if X <= {3} else {1,2,3} ) , lambda X: 0 if X <= {3} else 1                 ),
    (( {1,2,3}, lambda X: {1,2,3} if X else X )          , lambda X: 1 if X else 0                        ),
    (( {1,2,3}, lambda X: X | {3} )                      , lambda X: len(X) - 1 if 3 in X else len(X)     ),
    (( {1,2,3}, lambda X: X if X <= {1} else X | {2,3} ) , lambda X: len(X) - 1 if {2,3} <= X else len(X) ),
    (( {1,2,3}, lambda X: X if len(X) <= 1 else {1,2,3} ), lambda X: 2 if X == {1,2,3} else len(X)        ),
    (( {1,2,3}, lambda X: X )                            , len                                            ),
])
def test_from_closure_matroid(closure_matroid, expected):
    E, _ = closure_matroid
    r1 = from_closure_matroid(closure_matroid)
    r2 = expected
    assert all(r1(X) == r2(X) for X in powset(E))


@pytest.mark.parametrize('flats_matroid, expected', [
    (( {1,2,3}, [{1,2,3}] )                                    , lambda X: 0                                    ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                              , lambda X: 1 if 1 in X else 0                   ),
    (( {1,2,3}, [{3},{1,2,3}] )                                , lambda X: 0 if X <= {3} else 1                 ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , lambda X: 1 if X else 0                        ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )                    , lambda X: len(X) - 1 if 3 in X else len(X)     ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , lambda X: len(X) - 1 if {2,3} <= X else len(X) ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2,3}] )                  , lambda X: 2 if X == {1,2,3} else len(X)        ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), len                                            ),
])
def test_from_flats_matroid(flats_matroid, expected):
    E, _ = flats_matroid
    r1 = from_flats_matroid(flats_matroid)
    r2 = expected
    assert all(r1(X) == r2(X) for X in powset(E))


@pytest.mark.parametrize('open_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , lambda X: 0                                    ),
    (( {1,2,3}, [set(),{1}] )                                  , lambda X: 1 if 1 in X else 0                   ),
    (( {1,2,3}, [set(),{1,2}] )                                , lambda X: 0 if X <= {3} else 1                 ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , lambda X: 1 if X else 0                        ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , lambda X: len(X) - 1 if 3 in X else len(X)     ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , lambda X: len(X) - 1 if {2,3} <= X else len(X) ),
    (( {1,2,3}, [set(),{1,2},{1,3},{2,3},{1,2,3}] )            , lambda X: 2 if X == {1,2,3} else len(X)        ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), len                                            ),
])
def test_from_flats_matroid(open_matroid, expected):
    E, _ = open_matroid
    r1 = from_open_matroid(open_matroid)
    r2 = expected
    assert all(r1(X) == r2(X) for X in powset(E))


@pytest.mark.parametrize('hyperplanes_matroid, expected', [
    (( {1,2,3}, [{1,2,3}] )                                    , lambda X: 0                                    ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                              , lambda X: 1 if 1 in X else 0                   ),
    (( {1,2,3}, [{3},{1,2,3}] )                                , lambda X: 0 if X <= {3} else 1                 ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , lambda X: 1 if X else 0                        ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )                    , lambda X: len(X) - 1 if 3 in X else len(X)     ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , lambda X: len(X) - 1 if {2,3} <= X else len(X) ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2,3}] )                  , lambda X: 2 if X == {1,2,3} else len(X)        ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), len                                            ),
])
def test_from_hyperplanes_matroid(hyperplanes_matroid, expected):
    E, _ = hyperplanes_matroid
    r1 = from_hyperplanes_matroid(hyperplanes_matroid)
    r2 = expected
    assert all(r1(X) == r2(X) for X in powset(E))


@pytest.mark.parametrize('spanning_matroid, expected', [
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), lambda X: 0                                    ),
    (( {1,2,3}, [{1},{1,2},{1,3},{1,2,3}] )                    , lambda X: 1 if 1 in X else 0                   ),
    (( {1,2,3}, [{1},{2},{1,2},{1,3},{2,3},{1,2,3}] )          , lambda X: 0 if X <= {3} else 1                 ),
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )      , lambda X: 1 if X else 0                        ),
    (( {1,2,3}, [{1,2},{1,2,3}] )                              , lambda X: len(X) - 1 if 3 in X else len(X)     ),
    (( {1,2,3}, [{1,2},{1,3},{1,2,3}] )                        , lambda X: len(X) - 1 if {2,3} <= X else len(X) ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )                  , lambda X: 2 if X == {1,2,3} else len(X)        ),
    (( {1,2,3}, [{1,2,3}] )                                    , len                                            ),
])
def test_from_spanning_matroid(spanning_matroid, expected):
    E, _ = spanning_matroid
    r1 = from_spanning_matroid(spanning_matroid)
    r2 = expected
    assert all(r1(X) == r2(X) for X in powset(E))