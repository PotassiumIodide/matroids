import pytest

from matroids.construct.circuits import (
    from_independent_matroid,
    from_dependent_matroid,
    from_bases_matroid,
    from_rank_matroid,
    from_closure_matroid,
    from_flats_matroid,
    from_open_matroid,
    from_hyperplanes_matroid,
    from_spanning_matroid,
)


@pytest.mark.parametrize('independent_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , [{1},{2},{3}]       ),
    (( {1,2,3}, [set(),{1}] )                                  , [{2},{3}]           ),
    (( {1,2,3}, [set(),{1},{2}] )                              , [{1,2},{3}]         ),
    (( {1,2,3}, [set(),{1},{2},{3}] )                          , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , [{3}]               ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3}] )              , [{2,3}]             ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3}] )        , [{1,2,3}]           ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), []                  ),
])
def test_from_independent_matroid(independent_matroid, expected):
    Cs1 = from_independent_matroid(independent_matroid)
    Cs2 = expected
    assert all(map(lambda C1: C1 in Cs2, Cs1)) and all(map(lambda C2: C2 in Cs1, Cs2))


@pytest.mark.parametrize('dependent_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [{1},{2},{3}]       ),
    (( {1,2,3}, [{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )    , [{2},{3}]           ),
    (( {1,2,3}, [{3},{1,2},{1,3},{2,3},{1,2,3}] )        , [{1,2},{3}]         ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )            , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [{3},{1,3},{2,3}] )                      , [{3}]               ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                        , [{2,3}]             ),
    (( {1,2,3}, [{1,2,3}] )                              , [{1,2,3}]           ),
    (( {1,2,3}, [] )                                     , []                  ),
])
def test_from_dependent_matroid(dependent_matroid, expected):
    Cs1 = from_dependent_matroid(dependent_matroid)
    Cs2 = expected
    assert all(map(lambda C1: C1 in Cs2, Cs1)) and all(map(lambda C2: C2 in Cs1, Cs2))


@pytest.mark.parametrize('bases_matroid, expected', [
    (( {1,2,3}, [set()] )            , [{1},{2},{3}]       ),
    (( {1,2,3}, [{1}] )              , [{2},{3}]           ),
    (( {1,2,3}, [{1},{2}] )          , [{1,2},{3}]         ),
    (( {1,2,3}, [{1},{2},{3}] )      , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [{1,2}] )            , [{3}]               ),
    (( {1,2,3}, [{1,2},{1,3}] )      , [{2,3}]             ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), [{1,2,3}]           ),
    (( {1,2,3}, [{1,2,3}] )          , []                  ),
])
def test_from_bases_matroid(bases_matroid, expected):
    Cs1 = from_bases_matroid(bases_matroid)
    Cs2 = expected
    assert all(map(lambda C1: C1 in Cs2, Cs1)) and all(map(lambda C2: C2 in Cs1, Cs2))


@pytest.mark.parametrize('rank_matroid, expected', [
    (( {1,2,3}, lambda X: 0 )                                   , [{1},{2},{3}]       ),
    (( {1,2,3}, lambda X: 1 if 1 in X else 0 )                  , [{2},{3}]           ),
    (( {1,2,3}, lambda X: 0 if X <= {3} else 1 )                , [{1,2},{3}]         ),
    (( {1,2,3}, lambda X: 1 if X else 0 )                       , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, lambda X: len(X) - 1 if 3 in X else len(X) )    , [{3}]               ),
    (( {1,2,3}, lambda X: len(X) - 1 if {2,3} <= X else len(X) ), [{2,3}]             ),
    (( {1,2,3}, lambda X: 2 if X == {1,2,3} else len(X))        , [{1,2,3}]           ),
    (( {1,2,3}, len )                                           , []                  ),
])
def test_from_rank_matroid(rank_matroid, expected):
    Cs1 = from_rank_matroid(rank_matroid)
    Cs2 = expected
    assert all(map(lambda C1: C1 in Cs2, Cs1)) and all(map(lambda C2: C2 in Cs1, Cs2))


@pytest.mark.parametrize('closure_matroid, expected', [
    (( {1,2,3}, lambda X: {1,2,3} )                      , [{1},{2},{3}]                                 ),
    (( {1,2,3}, lambda X: {1,2,3} if 1 in X else {2,3} ) , [{2},{3}]                                     ),
    (( {1,2,3}, lambda X: {3} if X <= {3} else {1,2,3} ) , [{3},{1,2}]                                   ),
    (( {1,2,3}, lambda X: {1,2,3} if X else X )          , [{1,2},{1,3},{2,3}]                           ),
    (( {1,2,3}, lambda X: X | {3} )                      , [{3}]                                         ),
    (( {1,2,3}, lambda X: X if X <= {1} else X | {2,3} ) , [{2,3}]                                       ),
    (( {1,2,3}, lambda X: X if len(X) <= 1 else {1,2,3} ), [{1,2,3}]                                     ),
    (( {1,2,3}, lambda X: X )                            , []                                            ),
])
def test_from_closure_matroid(closure_matroid, expected):
    Cs1 = from_closure_matroid(closure_matroid)
    Cs2 = expected
    assert all(map(lambda C1: C1 in Cs2, Cs1)) and all(map(lambda C2: C2 in Cs1, Cs2))


@pytest.mark.parametrize('flats_matroid, expected', [
    (( {1,2,3}, [{1,2,3}] )                                    , [{1},{2},{3}]       ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                              , [{2},{3}]           ),
    (( {1,2,3}, [{3},{1,2,3}] )                                , [{3},{1,2}]         ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )                    , [{3}]               ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , [{2,3}]             ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2,3}] )                  , [{1,2,3}]           ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), []                  ),
])
def test_from_flats_matroid(flats_matroid, expected):
    Cs1 = from_flats_matroid(flats_matroid)
    Cs2 = expected
    assert all(map(lambda C1: C1 in Cs2, Cs1)) and all(map(lambda C2: C2 in Cs1, Cs2))


@pytest.mark.parametrize('open_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , [{1},{2},{3}]       ),
    (( {1,2,3}, [set(),{1}] )                                  , [{2},{3}]           ),
    (( {1,2,3}, [set(),{1,2}] )                                , [{3},{1,2}]         ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , [{3}]               ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , [{2,3}]             ),
    (( {1,2,3}, [set(),{1,2},{1,3},{2,3},{1,2,3}] )            , [{1,2,3}]           ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), []                  ),
])
def test_from_open_matroid(open_matroid, expected):
    Cs1 = from_open_matroid(open_matroid)
    Cs2 = expected
    assert all(map(lambda C1: C1 in Cs2, Cs1)) and all(map(lambda C2: C2 in Cs1, Cs2))


@pytest.mark.parametrize('hyperplanes_matroid, expected', [
    (( {1,2,3}, [] )                 , [{1},{2},{3}]       ),
    (( {1,2,3}, [{2,3}] )            , [{2},{3}]           ),
    (( {1,2,3}, [{3}] )              , [{3},{1,2}]         ),
    (( {1,2,3}, [set()] )            , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [{1,3},{2,3}] )      , [{3}]               ),
    (( {1,2,3}, [{1},{2,3}] )        , [{2,3}]             ),
    (( {1,2,3}, [{1},{2},{3}] )      , [{1,2,3}]           ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), []                  ),
])
def test_from_hyperplanes_matroid(hyperplanes_matroid, expected):
    Cs1 = from_hyperplanes_matroid(hyperplanes_matroid)
    Cs2 = expected
    assert all(map(lambda C1: C1 in Cs2, Cs1)) and all(map(lambda C2: C2 in Cs1, Cs2))


@pytest.mark.parametrize('spanning_matroid, expected', [
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [{1},{2},{3}]       ),
    (( {1,2,3}, [{1},{1,2},{1,3},{1,2,3}] )                    , [{2},{3}]           ),
    (( {1,2,3}, [{1},{2},{1,2},{1,3},{2,3},{1,2,3}] )          , [{3},{1,2}]         ),
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )      , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [{1,2},{1,2,3}] )                              , [{3}]               ),
    (( {1,2,3}, [{1,2},{1,3},{1,2,3}] )                        , [{2,3}]             ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )                  , [{1,2,3}]           ),
    (( {1,2,3}, [{1,2,3}] )                                    , []                  ),
])
def test_from_spanning_matroid(spanning_matroid, expected):
    Cs1 = from_spanning_matroid(spanning_matroid)
    Cs2 = expected
    assert all(map(lambda C1: C1 in Cs2, Cs1)) and all(map(lambda C2: C2 in Cs1, Cs2))

