import pytest

from matroids.core.set_operator import powset

from matroids.construct.closure_function import (
    from_independent_matroid,
    from_dependent_matroid,
    from_bases_matroid,
    from_circuits_matroid,
    from_rank_matroid,
    from_nulity_matroid,
    from_flats_matroid,
    from_open_matroid,
    from_hyperplanes_matroid,
    from_spanning_matroid,
)


@pytest.mark.parametrize('independent_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , lambda X: {1,2,3}                              ),
    (( {1,2,3}, [set(),{1}] )                                  , lambda X: {1,2,3} if 1 in X else {2,3}         ),
    (( {1,2,3}, [set(),{1},{2}] )                              , lambda X: {3} if X <= {3} else {1,2,3}         ),
    (( {1,2,3}, [set(),{1},{2},{3}] )                          , lambda X: {1,2,3} if X else X                  ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , lambda X: X | {3}                              ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3}] )              , lambda X: X if X <= {1} else X | {2,3}         ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3}] )        , lambda X: X if len(X) <= 1 else {1,2,3}        ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), lambda X: X                                    ),
])
def test_from_independent_matroid(independent_matroid, expected):
    E, _ = independent_matroid
    cl1 = from_independent_matroid(independent_matroid)
    cl2 = expected
    assert all(cl1(X) == cl2(X) for X in powset(E))


@pytest.mark.parametrize('dependent_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), lambda X: {1,2,3}                              ),
    (( {1,2,3}, [{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )    , lambda X: {1,2,3} if 1 in X else {2,3}         ),
    (( {1,2,3}, [{3},{1,2},{1,3},{2,3},{1,2,3}] )        , lambda X: {3} if X <= {3} else {1,2,3}         ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )            , lambda X: {1,2,3} if X else X                  ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )              , lambda X: X | {3}                              ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                        , lambda X: X if X <= {1} else X | {2,3}         ),
    (( {1,2,3}, [{1,2,3}] )                              , lambda X: X if len(X) <= 1 else {1,2,3}        ),
    (( {1,2,3}, [] )                                     , lambda X: X                                    ),
])
def test_from_dependent_matroid(dependent_matroid, expected):
    E, _ = dependent_matroid
    cl1 = from_dependent_matroid(dependent_matroid)
    cl2 = expected
    assert all(cl1(X) == cl2(X) for X in powset(E))


@pytest.mark.parametrize('bases_matroid, expected', [
    (( {1,2,3}, [set()] )            , lambda X: {1,2,3}                              ),
    (( {1,2,3}, [{1}] )              , lambda X: {1,2,3} if 1 in X else {2,3}         ),
    (( {1,2,3}, [{1},{2}] )          , lambda X: {3} if X <= {3} else {1,2,3}         ),
    (( {1,2,3}, [{1},{2},{3}] )      , lambda X: {1,2,3} if X else X                  ),
    (( {1,2,3}, [{1,2}] )            , lambda X: X | {3}                              ),
    (( {1,2,3}, [{1,2},{1,3}] )      , lambda X: X if X <= {1} else X | {2,3}         ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), lambda X: X if len(X) <= 1 else {1,2,3}        ),
    (( {1,2,3}, [{1,2,3}] )          , lambda X: X                                    ),
])
def test_from_bases_matroid(bases_matroid, expected):
    E, _ = bases_matroid
    cl1 = from_bases_matroid(bases_matroid)
    cl2 = expected
    assert all(cl1(X) == cl2(X) for X in powset(E))


@pytest.mark.parametrize('circuits_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3}] )      , lambda X: {1,2,3}                              ),
    (( {1,2,3}, [{2},{3}] )          , lambda X: {1,2,3} if 1 in X else {2,3}         ),
    (( {1,2,3}, [{3},{1,2}] )        , lambda X: {3} if X <= {3} else {1,2,3}         ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), lambda X: {1,2,3} if X else X                  ),
    (( {1,2,3}, [{3}] )              , lambda X: X | {3}                              ),
    (( {1,2,3}, [{2,3}] )            , lambda X: X if X <= {1} else X | {2,3}         ),
    (( {1,2,3}, [{1,2,3}] )          , lambda X: X if len(X) <= 1 else {1,2,3}        ),
    (( {1,2,3}, [] )                 , lambda X: X                                    ),
])
def test_from_circuits_matroid(circuits_matroid, expected):
    E, _ = circuits_matroid
    cl1 = from_circuits_matroid(circuits_matroid)
    cl2 = expected
    assert all(cl1(X) == cl2(X) for X in powset(E))


@pytest.mark.parametrize('rank_matroid, expected', [
    (( {1,2,3}, lambda X: 0 )                                   , lambda X: {1,2,3}                              ),
    (( {1,2,3}, lambda X: 1 if 1 in X else 0 )                  , lambda X: {1,2,3} if 1 in X else {2,3}         ),
    (( {1,2,3}, lambda X: 0 if X <= {3} else 1 )                , lambda X: {3} if X <= {3} else {1,2,3}         ),
    (( {1,2,3}, lambda X: 1 if X else 0 )                       , lambda X: {1,2,3} if X else X                  ),
    (( {1,2,3}, lambda X: len(X) - 1 if 3 in X else len(X) )    , lambda X: X | {3}                              ),
    (( {1,2,3}, lambda X: len(X) - 1 if {2,3} <= X else len(X) ), lambda X: X if X <= {1} else X | {2,3}         ),
    (( {1,2,3}, lambda X: 2 if X == {1,2,3} else len(X) )       , lambda X: X if len(X) <= 1 else {1,2,3}        ),
    (( {1,2,3}, len )                                           , lambda X: X                                    ),
])
def test_from_rank_matroid(rank_matroid, expected):
    E, _ = rank_matroid
    cl1 = from_rank_matroid(rank_matroid)
    cl2 = expected
    assert all(cl1(X) == cl2(X) for X in powset(E))


@pytest.mark.parametrize('nulity_matroid, expected', [
    (( {1,2,3}, len )                                         , lambda X: {1,2,3}                              ),
    (( {1,2,3}, lambda X: len(X) - 1 if 1 in X else len(X) )  , lambda X: {1,2,3} if 1 in X else {2,3}         ),
    (( {1,2,3}, lambda X: len(X) if X <= {3} else len(X) - 1 ), lambda X: {3} if X <= {3} else {1,2,3}         ),
    (( {1,2,3}, lambda X: len(X) - 1 if X else len(X) )       , lambda X: {1,2,3} if X else X                  ),
    (( {1,2,3}, lambda X: 1 if 3 in X else 0 )                , lambda X: X | {3}                              ),
    (( {1,2,3}, lambda X: 1 if {2,3} <= X else 0 )            , lambda X: X if X <= {1} else X | {2,3}         ),
    (( {1,2,3}, lambda X: len(X) - 2 if X == {1,2,3} else 0 ) , lambda X: X if len(X) <= 1 else {1,2,3}        ),
    (( {1,2,3}, lambda X: 0 )                                 , lambda X: X                                    ),
])
def test_from_nulity_matroid(nulity_matroid, expected):
    E, _ = nulity_matroid
    cl1 = from_nulity_matroid(nulity_matroid)
    cl2 = expected
    for X in powset(E):
        print(cl1(X), cl2(X))
    assert all(cl1(X) == cl2(X) for X in powset(E))


@pytest.mark.parametrize('flats_matroid, expected', [
    (( {1,2,3}, [{1,2,3}] )                                    , lambda X: {1,2,3}                              ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                              , lambda X: {1,2,3} if 1 in X else {2,3}         ),
    (( {1,2,3}, [{3},{1,2,3}] )                                , lambda X: {3} if X <= {3} else {1,2,3}         ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , lambda X: {1,2,3} if X else X                  ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )                    , lambda X: X | {3}                              ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , lambda X: X if X <= {1} else X | {2,3}         ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2,3}] )                  , lambda X: X if len(X) <= 1 else {1,2,3}        ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), lambda X: X                                    ),
])
def test_from_flats_matroid(flats_matroid, expected):
    E, _ = flats_matroid
    cl1 = from_flats_matroid(flats_matroid)
    cl2 = expected
    assert all(cl1(X) == cl2(X) for X in powset(E))


@pytest.mark.parametrize('open_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , lambda X: {1,2,3}                              ),
    (( {1,2,3}, [set(),{1}] )                                  , lambda X: {1,2,3} if 1 in X else {2,3}         ),
    (( {1,2,3}, [set(),{1,2}] )                                , lambda X: {3} if X <= {3} else {1,2,3}         ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , lambda X: {1,2,3} if X else X                  ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , lambda X: X | {3}                              ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , lambda X: X if X <= {1} else X | {2,3}         ),
    (( {1,2,3}, [set(),{1,2},{1,3},{2,3},{1,2,3}] )            , lambda X: X if len(X) <= 1 else {1,2,3}        ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), lambda X: X                                    ),
])
def test_from_open_matroid(open_matroid, expected):
    E, _ = open_matroid
    cl1 = from_open_matroid(open_matroid)
    cl2 = expected
    assert all(cl1(X) == cl2(X) for X in powset(E))


@pytest.mark.parametrize('hyperplanes_matroid, expected', [
    (( {1,2,3}, [] )                 , lambda X: {1,2,3}                              ),
    (( {1,2,3}, [{2,3}] )            , lambda X: {1,2,3} if 1 in X else {2,3}         ),
    (( {1,2,3}, [{3}] )              , lambda X: {3} if X <= {3} else {1,2,3}         ),
    (( {1,2,3}, [set()] )            , lambda X: {1,2,3} if X else X                  ),
    (( {1,2,3}, [{1,3},{2,3}] )      , lambda X: X | {3}                              ),
    (( {1,2,3}, [{1},{2,3}] )        , lambda X: X if X <= {1} else X | {2,3}         ),
    (( {1,2,3}, [{1},{2},{3}] )      , lambda X: X if len(X) <= 1 else {1,2,3}        ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), lambda X: X                                    ),
])
def test_from_hyperplanes_matroid(hyperplanes_matroid, expected):
    E, _ = hyperplanes_matroid
    cl1 = from_hyperplanes_matroid(hyperplanes_matroid)
    cl2 = expected
    assert all(cl1(X) == cl2(X) for X in powset(E))


@pytest.mark.parametrize('spanning_matroid, expected', [
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ) , lambda X: {1,2,3}                              ),
    (( {1,2,3}, [{1},{1,2},{1,3},{1,2,3}] )                     , lambda X: {1,2,3} if 1 in X else {2,3}         ),
    (( {1,2,3}, [{1},{2},{1,2},{1,3},{2,3},{1,2,3}] )           , lambda X: {3} if X <= {3} else {1,2,3}         ),
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )       , lambda X: {1,2,3} if X else X                  ),
    (( {1,2,3}, [{1,2},{1,2,3}] )                               , lambda X: X | {3}                              ),
    (( {1,2,3}, [{1,2},{1,3},{1,2,3}] )                         , lambda X: X if X <= {1} else X | {2,3}         ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )                   , lambda X: X if len(X) <= 1 else {1,2,3}        ),
    (( {1,2,3}, [{1,2,3}] )                                     , lambda X: X                                    ),
])
def test_from_spanning_matroid(spanning_matroid, expected):
    E, _ = spanning_matroid
    cl1 = from_spanning_matroid(spanning_matroid)
    cl2 = expected
    assert all(cl1(X) == cl2(X) for X in powset(E))