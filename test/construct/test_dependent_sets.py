import pytest

from matroids.construct.dependent_sets import (
    from_independent_matroid,
    from_bases_matroid,
    from_circuits_matroid,
    from_rank_matroid,
    from_nulity_matroid,
    from_closure_matroid,
    from_flats_matroid,
    from_open_matroid,
    from_hyperplanes_matroid,
    from_spanning_matroid,
)


@pytest.mark.parametrize('independent_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
    (( {1,2,3}, [set(),{1}] )                                  , [{2},{3},{1,2},{1,3},{2,3},{1,2,3}]     ),
    (( {1,2,3}, [set(),{1},{2}] )                              , [{3},{1,2},{1,3},{2,3},{1,2,3}]         ),
    (( {1,2,3}, [set(),{1},{2},{3}] )                          , [{1,2},{1,3},{2,3},{1,2,3}]             ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , [{3},{1,3},{2,3},{1,2,3}]               ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3}] )              , [{2,3},{1,2,3}]                         ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3}] )        , [{1,2,3}]                               ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), []                                      ),
])
def test_from_independent_matroid(independent_matroid, expected):
    Ds1 = from_independent_matroid(independent_matroid)
    Ds2 = expected
    assert all(map(lambda D1: D1 in Ds2, Ds1)) and all(map(lambda D2: D2 in Ds1, Ds2))


@pytest.mark.parametrize('bases_matroid, expected', [
    (( {1,2,3}, [set()] )            , [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
    (( {1,2,3}, [{1}] )              , [{2},{3},{1,2},{1,3},{2,3},{1,2,3}]     ),
    (( {1,2,3}, [{1},{2}] )          , [{3},{1,2},{1,3},{2,3},{1,2,3}]         ),
    (( {1,2,3}, [{1},{2},{3}] )      , [{1,2},{1,3},{2,3},{1,2,3}]             ),
    (( {1,2,3}, [{1,2}] )            , [{3},{1,3},{2,3},{1,2,3}]               ),
    (( {1,2,3}, [{1,2},{1,3}] )      , [{2,3},{1,2,3}]                         ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), [{1,2,3}]                               ),
    (( {1,2,3}, [{1,2,3}] )          , []                                      ),
])
def test_from_bases_matroid(bases_matroid, expected):
    Ds1 = from_bases_matroid(bases_matroid)
    Ds2 = expected
    assert all(map(lambda D1: D1 in Ds2, Ds1)) and all(map(lambda D2: D2 in Ds1, Ds2))


@pytest.mark.parametrize('circuits_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3}] )      , [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
    (( {1,2,3}, [{2},{3}] )          , [{2},{3},{1,2},{1,3},{2,3},{1,2,3}]     ),
    (( {1,2,3}, [{1,2},{3}] )        , [{3},{1,2},{1,3},{2,3},{1,2,3}]         ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), [{1,2},{1,3},{2,3},{1,2,3}]             ),
    (( {1,2,3}, [{3}] )              , [{3},{1,3},{2,3},{1,2,3}]               ),
    (( {1,2,3}, [{2,3}] )            , [{2,3},{1,2,3}]                         ),
    (( {1,2,3}, [{1,2,3}] )          , [{1,2,3}]                               ),
    (( {1,2,3}, [] )                 , []                                      ),
])
def test_from_circuits_matroid(circuits_matroid, expected):
    Ds1 = from_circuits_matroid(circuits_matroid)
    Ds2 = expected
    assert all(map(lambda D1: D1 in Ds2, Ds1)) and all(map(lambda D2: D2 in Ds1, Ds2))


@pytest.mark.parametrize('rank_matroid, expected', [
    (( {1,2,3}, lambda X: 0 )                                   , [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
    (( {1,2,3}, lambda X: 1 if 1 in X else 0 )                  , [{2},{3},{1,2},{1,3},{2,3},{1,2,3}]     ),
    (( {1,2,3}, lambda X: 0 if X <= {3} else 1 )                , [{3},{1,2},{1,3},{2,3},{1,2,3}]         ),
    (( {1,2,3}, lambda X: 1 if X else 0 )                       , [{1,2},{1,3},{2,3},{1,2,3}]             ),
    (( {1,2,3}, lambda X: len(X) - 1 if 3 in X else len(X) )    , [{3},{1,3},{2,3},{1,2,3}]               ),
    (( {1,2,3}, lambda X: len(X) - 1 if {2,3} <= X else len(X) ), [{2,3},{1,2,3}]                         ),
    (( {1,2,3}, lambda X: 2 if X == {1,2,3} else len(X) )       , [{1,2,3}]                               ),
    (( {1,2,3}, len )                                           , []                                      ),
])
def test_from_rank_matroid(rank_matroid, expected):
    Ds1 = from_rank_matroid(rank_matroid)
    Ds2 = expected
    assert all(map(lambda D1: D1 in Ds2, Ds1)) and all(map(lambda D2: D2 in Ds1, Ds2))


@pytest.mark.parametrize('nulity_matroid, expected', [
    (( {1,2,3}, len )                                         , [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
    (( {1,2,3}, lambda X: len(X) - 1 if 1 in X else len(X) )  , [{2},{3},{1,2},{1,3},{2,3},{1,2,3}]     ),
    (( {1,2,3}, lambda X: len(X) if X <= {3} else len(X) - 1 ), [{3},{1,2},{1,3},{2,3},{1,2,3}]         ),
    (( {1,2,3}, lambda X: len(X) - 1 if X else len(X) )       , [{1,2},{1,3},{2,3},{1,2,3}]             ),
    (( {1,2,3}, lambda X: 1 if 3 in X else 0 )                , [{3},{1,3},{2,3},{1,2,3}]               ),
    (( {1,2,3}, lambda X: 1 if {2,3} <= X else 0 )            , [{2,3},{1,2,3}]                         ),
    (( {1,2,3}, lambda X: len(X) - 2 if X == {1,2,3} else 0 ) , [{1,2,3}]                               ),
    (( {1,2,3}, lambda X: 0 )                                 , []                                      ),
])
def test_from_nulity_matroid(nulity_matroid, expected):
    Ds1 = from_nulity_matroid(nulity_matroid)
    Ds2 = expected
    assert all(map(lambda D1: D1 in Ds2, Ds1)) and all(map(lambda D2: D2 in Ds1, Ds2))


@pytest.mark.parametrize('closure_matroid, expected', [
    (( {1,2,3}, lambda X: {1,2,3} )                      , [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}]       ),
    (( {1,2,3}, lambda X: {1,2,3} if 1 in X else {2,3} ) , [{2},{3},{1,2},{1,3},{2,3},{1,2,3}]           ),
    (( {1,2,3}, lambda X: {3} if X <= {3} else {1,2,3} ) , [{3},{1,2},{1,3},{2,3},{1,2,3}]               ),
    (( {1,2,3}, lambda X: {1,2,3} if X else X )          , [{1,2},{1,3},{2,3},{1,2,3}]                   ),
    (( {1,2,3}, lambda X: X | {3} )                      , [{3},{1,3},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, lambda X: X if X <= {1} else X | {2,3} ) , [{2,3},{1,2,3}]                               ),
    (( {1,2,3}, lambda X: X if len(X) <= 1 else {1,2,3} ), [{1,2,3}]                                     ),
    (( {1,2,3}, lambda X: X )                            , []                                            ),
])
def test_from_closure_matroid(closure_matroid, expected):
    Ds1 = from_closure_matroid(closure_matroid)
    Ds2 = expected
    assert all(map(lambda D1: D1 in Ds2, Ds1)) and all(map(lambda D2: D2 in Ds1, Ds2))


@pytest.mark.parametrize('flats_matroid, expected', [
    (( {1,2,3}, [{1,2,3}] )                                    , [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}]       ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                              , [{2},{3},{1,2},{1,3},{2,3},{1,2,3}]           ),
    (( {1,2,3}, [{3},{1,2,3}] )                                , [{3},{1,2},{1,3},{2,3},{1,2,3}]               ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , [{1,2},{1,3},{2,3},{1,2,3}]                   ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )                    , [{3},{1,3},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , [{2,3},{1,2,3}]                               ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2,3}] )                  , [{1,2,3}]                                     ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), []                                            ),
])
def test_from_flats_matroid(flats_matroid, expected):
    Ds1 = from_flats_matroid(flats_matroid)
    Ds2 = expected
    assert all(map(lambda D1: D1 in Ds2, Ds1)) and all(map(lambda D2: D2 in Ds1, Ds2))


@pytest.mark.parametrize('open_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}]       ),
    (( {1,2,3}, [set(),{1}] )                                  , [{2},{3},{1,2},{1,3},{2,3},{1,2,3}]           ),
    (( {1,2,3}, [set(),{1,2}] )                                , [{3},{1,2},{1,3},{2,3},{1,2,3}]               ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , [{1,2},{1,3},{2,3},{1,2,3}]                   ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , [{3},{1,3},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , [{2,3},{1,2,3}]                               ),
    (( {1,2,3}, [set(),{1,2},{1,3},{2,3},{1,2,3}] )            , [{1,2,3}]                                     ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), []                                            ),
])
def test_from_open_matroid(open_matroid, expected):
    Ds1 = from_open_matroid(open_matroid)
    Ds2 = expected
    assert all(map(lambda D1: D1 in Ds2, Ds1)) and all(map(lambda D2: D2 in Ds1, Ds2))


@pytest.mark.parametrize('hyperplanes_matroid, expected', [
    (( {1,2,3}, [] )                 , [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}]       ),
    (( {1,2,3}, [{2,3}] )            , [{2},{3},{1,2},{1,3},{2,3},{1,2,3}]           ),
    (( {1,2,3}, [{3}] )              , [{3},{1,2},{1,3},{2,3},{1,2,3}]               ),
    (( {1,2,3}, [set()] )            , [{1,2},{1,3},{2,3},{1,2,3}]                   ),
    (( {1,2,3}, [{1,3},{2,3}] )      , [{3},{1,3},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{1},{2,3}] )        , [{2,3},{1,2,3}]                               ),
    (( {1,2,3}, [{1},{2},{3}] )      , [{1,2,3}]                                     ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), []                                            ),
])
def test_from_hyperplanes_matroid(hyperplanes_matroid, expected):
    Ds1 = from_hyperplanes_matroid(hyperplanes_matroid)
    Ds2 = expected
    assert all(map(lambda D1: D1 in Ds2, Ds1)) and all(map(lambda D2: D2 in Ds1, Ds2))


@pytest.mark.parametrize('spanning_matroid, expected', [
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}]       ),
    (( {1,2,3}, [{1},{1,2},{1,3},{1,2,3}] )                    , [{2},{3},{1,2},{1,3},{2,3},{1,2,3}]           ),
    (( {1,2,3}, [{1},{2},{1,2},{1,3},{2,3},{1,2,3}] )          , [{3},{1,2},{1,3},{2,3},{1,2,3}]               ),
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )      , [{1,2},{1,3},{2,3},{1,2,3}]                   ),
    (( {1,2,3}, [{1,2},{1,2,3}] )                              , [{3},{1,3},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{1,2},{1,3},{1,2,3}] )                        , [{2,3},{1,2,3}]                               ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )                  , [{1,2,3}]                                     ),
    (( {1,2,3}, [{1,2,3}] )                                    , []                                            ),
])
def test_from_spanning_matroid(spanning_matroid, expected):
    Ds1 = from_spanning_matroid(spanning_matroid)
    Ds2 = expected
    assert all(map(lambda D1: D1 in Ds2, Ds1)) and all(map(lambda D2: D2 in Ds1, Ds2))