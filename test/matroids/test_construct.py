import pytest

from src.utils.set_operator import powset

from src.matroids.construct import (
    independent_sets_from_dependent_matroid,
    independent_sets_from_bases_matroid,
    independent_sets_from_circuits_matroid,
    independent_sets_from_rank_matroid,
    independent_sets_from_closure_matroid,
    independent_sets_from_flats_matroid,
    independent_sets_from_open_sets_matroid,
    independent_sets_from_hyperplanes_matroid,
    independent_sets_from_spanning_sets_matroid,
    dependent_sets_from_independent_matroid,
    dependent_sets_from_bases_matroid,
    dependent_sets_from_circuits_matroid,
    dependent_sets_from_rank_matroid,
    dependent_sets_from_closure_matroid,
    dependent_sets_from_flats_matroid,
    dependent_sets_from_open_sets_matroid,
    dependent_sets_from_hyperplanes_matroid,
    dependent_sets_from_spanning_sets_matroid,
    bases_from_independent_matroid,
    bases_from_dependent_matroid,
    bases_from_circuits_matroid,
    bases_from_rank_matroid,
    bases_from_closure_matroid,
    bases_from_flats_matroid,
    bases_from_open_sets_matroid,
    bases_from_hyperplanes_matroid,
    bases_from_spanning_sets_matroid,
    circuits_from_independent_matroid,
    circuits_from_dependent_matroid,
    circuits_from_bases_matroid,
    circuits_from_rank_matroid,
    circuits_from_closure_matroid,
    circuits_from_flats_matroid,
    circuits_from_open_sets_matroid,
    circuits_from_hyperplanes_matroid,
    circuits_from_spanning_sets_matroid,
    rank_function_from_independent_matroid,
    rank_function_from_dependent_matroid,
    rank_function_from_bases_matroid,
    rank_function_from_circuits_matroid,
    rank_function_from_closure_matroid,
    rank_function_from_flats_matroid,
    rank_function_from_open_sets_matroid,
    rank_function_from_hyperplanes_matroid,
    rank_function_from_spanning_sets_matroid,
    closure_function_from_independent_matroid,
    closure_function_from_dependent_matroid,
    closure_function_from_bases_matroid,
    closure_function_from_circuits_matroid,
    closure_function_from_rank_matroid,
    closure_function_from_flats_matroid,
    closure_function_from_open_sets_matroid,
    closure_function_from_hyperplanes_matroid,
    closure_function_from_spanning_sets_matroid,
    flats_from_independent_matroid,
    flats_from_dependent_matroid,
    flats_from_bases_matroid,
    flats_from_circuits_matroid,
    flats_from_rank_matroid,
    flats_from_closure_matroid,
    flats_from_open_sets_matroid,
    flats_from_hyperplanes_matroid,
    flats_from_spanning_sets_matroid,
    open_sets_from_independent_matroid,
    open_sets_from_dependent_matroid,
    open_sets_from_bases_matroid,
    open_sets_from_circuits_matroid,
    open_sets_from_rank_matroid,
    open_sets_from_closure_matroid,
    open_sets_from_flats_matroid,
    open_sets_from_hyperplanes_matroid,
    open_sets_from_spanning_sets_matroid,
    hyperplanes_from_independent_matroid,
    hyperplanes_from_dependent_matroid,
    hyperplanes_from_bases_matroid,
    hyperplanes_from_circuits_matroid,
    hyperplanes_from_rank_matroid,
    hyperplanes_from_closure_matroid,
    hyperplanes_from_flats_matroid,
    hyperplanes_from_open_sets_matroid,
    hyperplanes_from_spanning_sets_matroid,
    spanning_sets_from_independent_matroid,
    spanning_sets_from_bases_matroid,
    spanning_sets_from_rank_matroid,
)


# TODO: Make a test case when a given pair is not a matroid.
@pytest.mark.parametrize('dependent_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [set()]                                       ),
    (( {1,2,3}, [{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )    , [set(), {1}]                                  ),
    (( {1,2,3}, [{3},{1,2},{1,3},{2,3},{1,2,3}] )        , [set(), {1},{2}]                              ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )            , [set(), {1},{2},{3}]                          ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )              , [set(), {1},{2},{1,2}]                        ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                        , [set(),{1},{2},{3},{1,2},{1,3}]               ),
    (( {1,2,3}, [{1,2,3}] )                              , [set(),{1},{2},{3},{1,2},{1,3},{2,3}]         ),
    (( {1,2,3}, [] )                                     , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_independent_sets_from_dependent_matroid(dependent_matroid, expected):
    Is1 = independent_sets_from_dependent_matroid(dependent_matroid)
    Is2 = expected
    assert all(map(lambda I1: I1 in Is2, Is1)) and all(map(lambda I2: I2 in Is1, Is2))


@pytest.mark.parametrize('bases_matroid, expected', [
    (( {1,2,3}, [set()] )            , [set()]                                       ),
    (( {1,2,3}, [{1}] )              , [set(), {1}]                                  ),
    (( {1,2,3}, [{1},{2}] )          , [set(), {1},{2}]                              ),
    (( {1,2,3}, [{1},{2},{3}] )      , [set(), {1},{2},{3}]                          ),
    (( {1,2,3}, [{1,2}] )            , [set(), {1},{2},{1,2}]                        ),
    (( {1,2,3}, [{1,2},{1,3}] )      , [set(),{1},{2},{3},{1,2},{1,3}]               ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), [set(),{1},{2},{3},{1,2},{1,3},{2,3}]         ),
    (( {1,2,3}, [{1,2,3}] )          , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_independent_sets_from_bases_matroid(bases_matroid, expected):
    Is1 = independent_sets_from_bases_matroid(bases_matroid)
    Is2 = expected
    assert all(map(lambda I1: I1 in Is2, Is1)) and all(map(lambda I2: I2 in Is1, Is2))


@pytest.mark.parametrize('circuits_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3}] )      , [set()]                                       ),
    (( {1,2,3}, [{2},{3}] )          , [set(), {1}]                                  ),
    (( {1,2,3}, [{1,2},{3}] )        , [set(), {1},{2}]                              ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), [set(), {1},{2},{3}]                          ),
    (( {1,2,3}, [{3}] )              , [set(), {1},{2},{1,2}]                        ),
    (( {1,2,3}, [{2,3}] )            , [set(),{1},{2},{3},{1,2},{1,3}]               ),
    (( {1,2,3}, [{1,2,3}] )          , [set(),{1},{2},{3},{1,2},{1,3},{2,3}]         ),
    (( {1,2,3}, [] )                 , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_independent_sets_from_circuits_matroid(circuits_matroid, expected):
    Is1 = independent_sets_from_circuits_matroid(circuits_matroid)
    Is2 = expected
    assert all(map(lambda I1: I1 in Is2, Is1)) and all(map(lambda I2: I2 in Is1, Is2))


@pytest.mark.parametrize('rank_matroid, expected', [
    (( {1,2,3}, lambda X: 0 )                                   , [set()]                                       ),
    (( {1,2,3}, lambda X: 1 if 1 in X else 0 )                  , [set(), {1}]                                  ),
    (( {1,2,3}, lambda X: 0 if X <= {0,3} else 1 )              , [set(), {1},{2}]                              ),
    (( {1,2,3}, lambda X: 1 if X else 0 )                       , [set(), {1},{2},{3}]                          ),
    (( {1,2,3}, lambda X: len(X) - 1 if 3 in X else len(X) )    , [set(), {1},{2},{1,2}]                        ),
    (( {1,2,3}, lambda X: len(X) - 1 if {2,3} <= X else len(X) ), [set(),{1},{2},{3},{1,2},{1,3}]               ),
    (( {1,2,3}, lambda X: 2 if X == {1,2,3} else len(X) )       , [set(),{1},{2},{3},{1,2},{1,3},{2,3}]         ),
    (( {1,2,3}, len )                                           , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_independent_sets_from_rank_matroid(rank_matroid, expected):
    Is1 = independent_sets_from_rank_matroid(rank_matroid)
    Is2 = expected
    assert all(map(lambda I1: I1 in Is2, Is1)) and all(map(lambda I2: I2 in Is1, Is2))


@pytest.mark.parametrize('closure_matroid, expected', [
    (( {1,2,3}, lambda X: {1,2,3} )                      , [set()]                                       ),
    (( {1,2,3}, lambda X: {1,2,3} if 1 in X else {2,3} ) , [set(), {1}]                                  ),
    (( {1,2,3}, lambda X: {3} if X <= {3} else {1,2,3} ) , [set(), {1},{2}]                              ),
    (( {1,2,3}, lambda X: {1,2,3} if X else X )          , [set(), {1},{2},{3}]                          ),
    (( {1,2,3}, lambda X: X | {3} )                      , [set(), {1},{2},{1,2}]                        ),
    (( {1,2,3}, lambda X: X if X <= {1} else X | {2,3} ) , [set(),{1},{2},{3},{1,2},{1,3}]               ),
    (( {1,2,3}, lambda X: X if len(X) <= 1 else {1,2,3} ), [set(),{1},{2},{3},{1,2},{1,3},{2,3}]         ),
    (( {1,2,3}, lambda X: X )                            , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_independent_sets_from_closure_matroid(closure_matroid, expected):
    Is1 = independent_sets_from_closure_matroid(closure_matroid)
    Is2 = expected
    assert all(map(lambda I1: I1 in Is2, Is1)) and all(map(lambda I2: I2 in Is1, Is2))


@pytest.mark.parametrize('flats_matroid, expected', [
    (( {1,2,3}, [{1,2,3}] )                                    , [set()]                                       ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                              , [set(), {1}]                                  ),
    (( {1,2,3}, [{3},{1,2,3}] )                                , [set(), {1},{2}]                              ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , [set(), {1},{2},{3}]                          ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )                    , [set(), {1},{2},{1,2}]                        ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , [set(),{1},{2},{3},{1,2},{1,3}]               ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2,3}] )                  , [set(),{1},{2},{3},{1,2},{1,3},{2,3}]         ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_independent_sets_from_flats_matroid(flats_matroid, expected):
    Is1 = independent_sets_from_flats_matroid(flats_matroid)
    Is2 = expected
    assert all(map(lambda I1: I1 in Is2, Is1)) and all(map(lambda I2: I2 in Is1, Is2))


@pytest.mark.parametrize('open_sets_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , [set()]                                       ),
    (( {1,2,3}, [set(),{1}] )                                  , [set(), {1}]                                  ),
    (( {1,2,3}, [set(),{1,2}] )                                , [set(), {1},{2}]                              ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , [set(), {1},{2},{3}]                          ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , [set(), {1},{2},{1,2}]                        ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , [set(),{1},{2},{3},{1,2},{1,3}]               ),
    (( {1,2,3}, [set(),{1,2},{1,3},{2,3},{1,2,3}] )            , [set(),{1},{2},{3},{1,2},{1,3},{2,3}]         ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_independent_sets_from_open_sets_matroid(open_sets_matroid, expected):
    Is1 = independent_sets_from_open_sets_matroid(open_sets_matroid)
    Is2 = expected
    assert all(map(lambda I1: I1 in Is2, Is1)) and all(map(lambda I2: I2 in Is1, Is2))


@pytest.mark.parametrize('hyperplanes_matroid, expected', [
    (( {1,2,3}, [] )                 , [set()]                                       ),
    (( {1,2,3}, [{2,3}] )            , [set(), {1}]                                  ),
    (( {1,2,3}, [{3}] )              , [set(), {1},{2}]                              ),
    (( {1,2,3}, [set()] )            , [set(), {1},{2},{3}]                          ),
    (( {1,2,3}, [{1,3},{2,3}] )      , [set(), {1},{2},{1,2}]                        ),
    (( {1,2,3}, [{1},{2,3}] )        , [set(),{1},{2},{3},{1,2},{1,3}]               ),
    (( {1,2,3}, [{1},{2},{3}] )      , [set(),{1},{2},{3},{1,2},{1,3},{2,3}]         ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_independent_sets_from_hyperplanes_matroid(hyperplanes_matroid, expected):
    Is1 = independent_sets_from_hyperplanes_matroid(hyperplanes_matroid)
    Is2 = expected
    assert all(map(lambda I1: I1 in Is2, Is1)) and all(map(lambda I2: I2 in Is1, Is2))


@pytest.mark.parametrize('spanning_sets_matroid, expected', [
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [set()]                                       ),
    (( {1,2,3}, [{1},{1,2},{1,3},{1,2,3}] )                    , [set(), {1}]                                  ),
    (( {1,2,3}, [{1},{2},{1,2},{1,3},{2,3},{1,2,3}] )          , [set(), {1},{2}]                              ),
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )      , [set(), {1},{2},{3}]                          ),
    (( {1,2,3}, [{1,2},{1,2,3}] )                              , [set(), {1},{2},{1,2}]                        ),
    (( {1,2,3}, [{1,2},{1,3},{1,2,3}] )                        , [set(),{1},{2},{3},{1,2},{1,3}]               ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )                  , [set(),{1},{2},{3},{1,2},{1,3},{2,3}]         ),
    (( {1,2,3}, [{1,2,3}] )                                    , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_independent_sets_from_spanning_sets_matroid(spanning_sets_matroid, expected):
    Is1 = independent_sets_from_spanning_sets_matroid(spanning_sets_matroid)
    Is2 = expected
    assert all(map(lambda I1: I1 in Is2, Is1)) and all(map(lambda I2: I2 in Is1, Is2))


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
def test_dependent_sets_from_independent_matroid(independent_matroid, expected):
    Ds1 = dependent_sets_from_independent_matroid(independent_matroid)
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
def test_dependent_sets_from_bases_matroid(bases_matroid, expected):
    Ds1 = dependent_sets_from_bases_matroid(bases_matroid)
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
def test_dependent_sets_from_circuits_matroid(circuits_matroid, expected):
    Ds1 = dependent_sets_from_circuits_matroid(circuits_matroid)
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
def test_dependent_sets_from_rank_matroid(rank_matroid, expected):
    Ds1 = dependent_sets_from_rank_matroid(rank_matroid)
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
def test_dependent_sets_from_closure_matroid(closure_matroid, expected):
    Ds1 = dependent_sets_from_closure_matroid(closure_matroid)
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
def test_dependent_sets_from_flats_matroid(flats_matroid, expected):
    Ds1 = dependent_sets_from_flats_matroid(flats_matroid)
    Ds2 = expected
    assert all(map(lambda D1: D1 in Ds2, Ds1)) and all(map(lambda D2: D2 in Ds1, Ds2))


@pytest.mark.parametrize('open_sets_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}]       ),
    (( {1,2,3}, [set(),{1}] )                                  , [{2},{3},{1,2},{1,3},{2,3},{1,2,3}]           ),
    (( {1,2,3}, [set(),{1,2}] )                                , [{3},{1,2},{1,3},{2,3},{1,2,3}]               ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , [{1,2},{1,3},{2,3},{1,2,3}]                   ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , [{3},{1,3},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , [{2,3},{1,2,3}]                               ),
    (( {1,2,3}, [set(),{1,2},{1,3},{2,3},{1,2,3}] )            , [{1,2,3}]                                     ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), []                                            ),
])
def test_dependent_sets_from_open_sets_matroid(open_sets_matroid, expected):
    Ds1 = dependent_sets_from_open_sets_matroid(open_sets_matroid)
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
def test_dependent_sets_from_hyperplanes_matroid(hyperplanes_matroid, expected):
    Ds1 = dependent_sets_from_hyperplanes_matroid(hyperplanes_matroid)
    Ds2 = expected
    assert all(map(lambda D1: D1 in Ds2, Ds1)) and all(map(lambda D2: D2 in Ds1, Ds2))


@pytest.mark.parametrize('spanning_sets_matroid, expected', [
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}]       ),
    (( {1,2,3}, [{1},{1,2},{1,3},{1,2,3}] )                    , [{2},{3},{1,2},{1,3},{2,3},{1,2,3}]           ),
    (( {1,2,3}, [{1},{2},{1,2},{1,3},{2,3},{1,2,3}] )          , [{3},{1,2},{1,3},{2,3},{1,2,3}]               ),
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )      , [{1,2},{1,3},{2,3},{1,2,3}]                   ),
    (( {1,2,3}, [{1,2},{1,2,3}] )                              , [{3},{1,3},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{1,2},{1,3},{1,2,3}] )                        , [{2,3},{1,2,3}]                               ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )                  , [{1,2,3}]                                     ),
    (( {1,2,3}, [{1,2,3}] )                                    , []                                            ),
])
def test_dependent_sets_from_spanning_sets_matroid(spanning_sets_matroid, expected):
    Ds1 = dependent_sets_from_spanning_sets_matroid(spanning_sets_matroid)
    Ds2 = expected
    assert all(map(lambda D1: D1 in Ds2, Ds1)) and all(map(lambda D2: D2 in Ds1, Ds2))


@pytest.mark.parametrize('independent_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , [set()]             ),
    (( {1,2,3}, [set(),{1}] )                                  , [{1}]               ),
    (( {1,2,3}, [set(),{1},{2}] )                              , [{1},{2}]           ),
    (( {1,2,3}, [set(),{1},{2},{3}] )                          , [{1},{2},{3}]       ),
    (( {1,2,3}, [set(),{1},{1,2}] )                            , [{1,2}]             ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3}] )              , [{1,2},{1,3}]       ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3}] )        , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [{1,2,3}]           ),
])
def test_bases_from_independent_matroid(independent_matroid, expected):
    Bs1 = bases_from_independent_matroid(independent_matroid)
    Bs2 = expected
    assert all(map(lambda B1: B1 in Bs2, Bs1)) and all(map(lambda B2: B2 in Bs1, Bs2))


@pytest.mark.parametrize('dependent_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [set()]             ),
    (( {1,2,3}, [{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )    , [{1}]               ),
    (( {1,2,3}, [{3},{1,2},{1,3},{2,3},{1,2,3}] )        , [{1},{2}]           ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )            , [{1},{2},{3}]       ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )              , [{1,2}]             ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                        , [{1,2},{1,3}]       ),
    (( {1,2,3}, [{1,2,3}] )                              , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [] )                                     , [{1,2,3}]           ),
])
def test_bases_from_dependent_matroid(dependent_matroid, expected):
    Bs1 = bases_from_dependent_matroid(dependent_matroid)
    Bs2 = expected
    assert all(map(lambda B1: B1 in Bs2, Bs1)) and all(map(lambda B2: B2 in Bs1, Bs2))


@pytest.mark.parametrize('circuits_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3}] )      , [set()]             ),
    (( {1,2,3}, [{2},{3}] )          , [{1}]               ),
    (( {1,2,3}, [{1,2},{3}] )        , [{1},{2}]           ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), [{1},{2},{3}]       ),
    (( {1,2,3}, [{3}] )              , [{1,2}]             ),
    (( {1,2,3}, [{2,3}] )            , [{1,2},{1,3}]       ),
    (( {1,2,3}, [{1,2,3}] )          , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [] )                 , [{1,2,3}]           ),
])
def test_bases_from_circuits_matroid(circuits_matroid, expected):
    Bs1 = bases_from_circuits_matroid(circuits_matroid)
    Bs2 = expected
    assert all(map(lambda B1: B1 in Bs2, Bs1)) and all(map(lambda B2: B2 in Bs1, Bs2))


@pytest.mark.parametrize('rank_matroid, expected', [
    (( {1,2,3}, lambda X: 0 )                                   , [set()]             ),
    (( {1,2,3}, lambda X: 1 if 1 in X else 0 )                  , [{1}]               ),
    (( {1,2,3}, lambda X: 0 if X <= {0,3} else 1 )              , [{1},{2}]           ),
    (( {1,2,3}, lambda X: 1 if X else 0 )                       , [{1},{2},{3}]       ),
    (( {1,2,3}, lambda X: len(X) - 1 if 3 in X else len(X) )    , [{1,2}]             ),
    (( {1,2,3}, lambda X: len(X) - 1 if {2,3} <= X else len(X) ), [{1,2},{1,3}]       ),
    (( {1,2,3}, lambda X: 2 if X == {1,2,3} else len(X) )       , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, len )                                           , [{1,2,3}]           ),
])
def test_bases_from_rank_matroid(rank_matroid, expected):
    Bs1 = bases_from_rank_matroid(rank_matroid)
    Bs2 = expected
    assert all(map(lambda B1: B1 in Bs2, Bs1)) and all(map(lambda B2: B2 in Bs1, Bs2))


@pytest.mark.parametrize('closure_matroid, expected', [
    (( {1,2,3}, lambda X: {1,2,3} )                      , [set()]             ),
    (( {1,2,3}, lambda X: {1,2,3} if 1 in X else {2,3} ) , [{1}]               ),
    (( {1,2,3}, lambda X: {3} if X <= {3} else {1,2,3} ) , [{1},{2}]           ),
    (( {1,2,3}, lambda X: {1,2,3} if X else X )          , [{1},{2},{3}]       ),
    (( {1,2,3}, lambda X: X | {3} )                      , [{1,2}]             ),
    (( {1,2,3}, lambda X: X if X <= {1} else X | {2,3} ) , [{1,2},{1,3}]       ),
    (( {1,2,3}, lambda X: X if len(X) <= 1 else {1,2,3} ), [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, lambda X: X )                            , [{1,2,3}]           ),
])
def test_bases_from_closure_matroid(closure_matroid, expected):
    Bs1 = bases_from_closure_matroid(closure_matroid)
    Bs2 = expected
    assert all(map(lambda B1: B1 in Bs2, Bs1)) and all(map(lambda B2: B2 in Bs1, Bs2))


@pytest.mark.parametrize('flats_matroid, expected', [
    (( {1,2,3}, [{1,2,3}] )                                    , [set()]             ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                              , [{1}]               ),
    (( {1,2,3}, [{3},{1,2,3}] )                                , [{1},{2}]           ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , [{1},{2},{3}]       ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )                    , [{1,2}]             ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , [{1,2},{1,3}]       ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2,3}] )                  , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [{1,2,3}]           ),
])
def test_bases_from_flats_matroid(flats_matroid, expected):
    Bs1 = bases_from_flats_matroid(flats_matroid)
    Bs2 = expected
    assert all(map(lambda B1: B1 in Bs2, Bs1)) and all(map(lambda B2: B2 in Bs1, Bs2))


@pytest.mark.parametrize('open_sets_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , [set()]             ),
    (( {1,2,3}, [set(),{1}] )                                  , [{1}]               ),
    (( {1,2,3}, [set(),{1,2}] )                                , [{1},{2}]           ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , [{1},{2},{3}]       ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , [{1,2}]             ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , [{1,2},{1,3}]       ),
    (( {1,2,3}, [set(),{1,2},{1,3},{2,3},{1,2,3}] )            , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [{1,2,3}]           ),
])
def test_bases_from_open_sets_matroid(open_sets_matroid, expected):
    Bs1 = bases_from_open_sets_matroid(open_sets_matroid)
    Bs2 = expected
    assert all(map(lambda B1: B1 in Bs2, Bs1)) and all(map(lambda B2: B2 in Bs1, Bs2))


@pytest.mark.parametrize('hyperplanes_matroid, expected', [
    (( {1,2,3}, [] )                 , [set()]             ),
    (( {1,2,3}, [{2,3}] )            , [{1}]               ),
    (( {1,2,3}, [{3}] )              , [{1},{2}]           ),
    (( {1,2,3}, [set()] )            , [{1},{2},{3}]       ),
    (( {1,2,3}, [{1,3},{2,3}] )      , [{1,2}]             ),
    (( {1,2,3}, [{1},{2,3}] )        , [{1,2},{1,3}]       ),
    (( {1,2,3}, [{1},{2},{3}] )      , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), [{1,2,3}]           ),
])
def test_bases_from_hyperplanes_matroid(hyperplanes_matroid, expected):
    Bs1 = bases_from_hyperplanes_matroid(hyperplanes_matroid)
    Bs2 = expected
    assert all(map(lambda B1: B1 in Bs2, Bs1)) and all(map(lambda B2: B2 in Bs1, Bs2))


@pytest.mark.parametrize('spanning_sets_matroid, expected', [
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [set()]             ),
    (( {1,2,3}, [{1},{1,2},{1,3},{1,2,3}] )                    , [{1}]               ),
    (( {1,2,3}, [{1},{2},{1,2},{1,3},{2,3},{1,2,3}] )          , [{1},{2}]           ),
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )      , [{1},{2},{3}]       ),
    (( {1,2,3}, [{1,2},{1,2,3}] )                              , [{1,2}]             ),
    (( {1,2,3}, [{1,2},{1,3},{1,2,3}] )                        , [{1,2},{1,3}]       ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )                  , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [{1,2,3}] )                                    , [{1,2,3}]           ),
])
def test_bases_from_spanning_sets_matroid(spanning_sets_matroid, expected):
    Bs1 = bases_from_spanning_sets_matroid(spanning_sets_matroid)
    Bs2 = expected
    assert all(map(lambda B1: B1 in Bs2, Bs1)) and all(map(lambda B2: B2 in Bs1, Bs2))


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
def test_circuits_from_independent_matroid(independent_matroid, expected):
    Cs1 = circuits_from_independent_matroid(independent_matroid)
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
def test_circuits_from_dependent_matroid(dependent_matroid, expected):
    Cs1 = circuits_from_dependent_matroid(dependent_matroid)
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
def test_circuits_from_bases_matroid(bases_matroid, expected):
    Cs1 = circuits_from_bases_matroid(bases_matroid)
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
def test_circuits_from_rank_matroid(rank_matroid, expected):
    Cs1 = circuits_from_rank_matroid(rank_matroid)
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
def test_circuits_from_closure_matroid(closure_matroid, expected):
    Cs1 = circuits_from_closure_matroid(closure_matroid)
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
def test_circuits_from_flats_matroid(flats_matroid, expected):
    Cs1 = circuits_from_flats_matroid(flats_matroid)
    Cs2 = expected
    assert all(map(lambda C1: C1 in Cs2, Cs1)) and all(map(lambda C2: C2 in Cs1, Cs2))


@pytest.mark.parametrize('open_sets_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , [{1},{2},{3}]       ),
    (( {1,2,3}, [set(),{1}] )                                  , [{2},{3}]           ),
    (( {1,2,3}, [set(),{1,2}] )                                , [{3},{1,2}]         ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , [{3}]               ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , [{2,3}]             ),
    (( {1,2,3}, [set(),{1,2},{1,3},{2,3},{1,2,3}] )            , [{1,2,3}]           ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), []                  ),
])
def test_circuits_from_open_sets_matroid(open_sets_matroid, expected):
    Cs1 = circuits_from_open_sets_matroid(open_sets_matroid)
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
def test_circuits_from_hyperplanes_matroid(hyperplanes_matroid, expected):
    Cs1 = circuits_from_hyperplanes_matroid(hyperplanes_matroid)
    Cs2 = expected
    assert all(map(lambda C1: C1 in Cs2, Cs1)) and all(map(lambda C2: C2 in Cs1, Cs2))


@pytest.mark.parametrize('spanning_sets_matroid, expected', [
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [{1},{2},{3}]       ),
    (( {1,2,3}, [{1},{1,2},{1,3},{1,2,3}] )                    , [{2},{3}]           ),
    (( {1,2,3}, [{1},{2},{1,2},{1,3},{2,3},{1,2,3}] )          , [{3},{1,2}]         ),
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )      , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [{1,2},{1,2,3}] )                              , [{3}]               ),
    (( {1,2,3}, [{1,2},{1,3},{1,2,3}] )                        , [{2,3}]             ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )                  , [{1,2,3}]           ),
    (( {1,2,3}, [{1,2,3}] )                                    , []                  ),
])
def test_circuits_from_spanning_sets_matroid(spanning_sets_matroid, expected):
    Cs1 = circuits_from_spanning_sets_matroid(spanning_sets_matroid)
    Cs2 = expected
    assert all(map(lambda C1: C1 in Cs2, Cs1)) and all(map(lambda C2: C2 in Cs1, Cs2))


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
def test_rank_function_from_independent_matroid(independent_matroid, expected):
    E, _ = independent_matroid
    r1 = rank_function_from_independent_matroid(independent_matroid)
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
def test_rank_function_from_dependent_matroid(dependent_matroid, expected):
    E, _ = dependent_matroid
    r1 = rank_function_from_dependent_matroid(dependent_matroid)
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
def test_rank_function_from_bases_matroid(bases_matroid, expected):
    E, _ = bases_matroid
    r1 = rank_function_from_bases_matroid(bases_matroid)
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
def test_rank_function_from_circuits_matroid(circuits_matroid, expected):
    E, _ = circuits_matroid
    r1 = rank_function_from_circuits_matroid(circuits_matroid)
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
def test_rank_function_from_closure_matroid(closure_matroid, expected):
    E, _ = closure_matroid
    r1 = rank_function_from_closure_matroid(closure_matroid)
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
def test_rank_function_from_flats_matroid(flats_matroid, expected):
    E, _ = flats_matroid
    r1 = rank_function_from_flats_matroid(flats_matroid)
    r2 = expected
    assert all(r1(X) == r2(X) for X in powset(E))


@pytest.mark.parametrize('open_sets_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , lambda X: 0                                    ),
    (( {1,2,3}, [set(),{1}] )                                  , lambda X: 1 if 1 in X else 0                   ),
    (( {1,2,3}, [set(),{1,2}] )                                , lambda X: 0 if X <= {3} else 1                 ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , lambda X: 1 if X else 0                        ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , lambda X: len(X) - 1 if 3 in X else len(X)     ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , lambda X: len(X) - 1 if {2,3} <= X else len(X) ),
    (( {1,2,3}, [set(),{1,2},{1,3},{2,3},{1,2,3}] )            , lambda X: 2 if X == {1,2,3} else len(X)        ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), len                                            ),
])
def test_rank_function_from_flats_matroid(open_sets_matroid, expected):
    E, _ = open_sets_matroid
    r1 = rank_function_from_open_sets_matroid(open_sets_matroid)
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
def test_rank_function_from_hyperplanes_matroid(hyperplanes_matroid, expected):
    E, _ = hyperplanes_matroid
    r1 = rank_function_from_hyperplanes_matroid(hyperplanes_matroid)
    r2 = expected
    assert all(r1(X) == r2(X) for X in powset(E))


@pytest.mark.parametrize('spanning_sets_matroid, expected', [
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), lambda X: 0                                    ),
    (( {1,2,3}, [{1},{1,2},{1,3},{1,2,3}] )                    , lambda X: 1 if 1 in X else 0                   ),
    (( {1,2,3}, [{1},{2},{1,2},{1,3},{2,3},{1,2,3}] )          , lambda X: 0 if X <= {3} else 1                 ),
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )      , lambda X: 1 if X else 0                        ),
    (( {1,2,3}, [{1,2},{1,2,3}] )                              , lambda X: len(X) - 1 if 3 in X else len(X)     ),
    (( {1,2,3}, [{1,2},{1,3},{1,2,3}] )                        , lambda X: len(X) - 1 if {2,3} <= X else len(X) ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )                  , lambda X: 2 if X == {1,2,3} else len(X)        ),
    (( {1,2,3}, [{1,2,3}] )                                    , len                                            ),
])
def test_rank_function_from_spanning_sets_matroid(spanning_sets_matroid, expected):
    E, _ = spanning_sets_matroid
    r1 = rank_function_from_spanning_sets_matroid(spanning_sets_matroid)
    r2 = expected
    assert all(r1(X) == r2(X) for X in powset(E))


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
def test_closure_function_from_independent_matroid(independent_matroid, expected):
    E, _ = independent_matroid
    cl1 = closure_function_from_independent_matroid(independent_matroid)
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
def test_closure_function_from_dependent_matroid(dependent_matroid, expected):
    E, _ = dependent_matroid
    cl1 = closure_function_from_dependent_matroid(dependent_matroid)
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
def test_closure_function_from_bases_matroid(bases_matroid, expected):
    E, _ = bases_matroid
    cl1 = closure_function_from_bases_matroid(bases_matroid)
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
def test_closure_function_from_circuits_matroid(circuits_matroid, expected):
    E, _ = circuits_matroid
    cl1 = closure_function_from_circuits_matroid(circuits_matroid)
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
def test_closure_function_from_rank_matroid(rank_matroid, expected):
    E, _ = rank_matroid
    cl1 = closure_function_from_rank_matroid(rank_matroid)
    cl2 = expected
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
def test_closure_function_from_flats_matroid(flats_matroid, expected):
    E, _ = flats_matroid
    cl1 = closure_function_from_flats_matroid(flats_matroid)
    cl2 = expected
    assert all(cl1(X) == cl2(X) for X in powset(E))


@pytest.mark.parametrize('open_sets_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , lambda X: {1,2,3}                              ),
    (( {1,2,3}, [set(),{1}] )                                  , lambda X: {1,2,3} if 1 in X else {2,3}         ),
    (( {1,2,3}, [set(),{1,2}] )                                , lambda X: {3} if X <= {3} else {1,2,3}         ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , lambda X: {1,2,3} if X else X                  ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , lambda X: X | {3}                              ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , lambda X: X if X <= {1} else X | {2,3}         ),
    (( {1,2,3}, [set(),{1,2},{1,3},{2,3},{1,2,3}] )            , lambda X: X if len(X) <= 1 else {1,2,3}        ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), lambda X: X                                    ),
])
def test_closure_function_from_open_sets_matroid(open_sets_matroid, expected):
    E, _ = open_sets_matroid
    cl1 = closure_function_from_open_sets_matroid(open_sets_matroid)
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
def test_closure_function_from_hyperplanes_matroid(hyperplanes_matroid, expected):
    E, _ = hyperplanes_matroid
    cl1 = closure_function_from_hyperplanes_matroid(hyperplanes_matroid)
    cl2 = expected
    assert all(cl1(X) == cl2(X) for X in powset(E))


@pytest.mark.parametrize('spanning_sets_matroid, expected', [
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ) , lambda X: {1,2,3}                              ),
    (( {1,2,3}, [{1},{1,2},{1,3},{1,2,3}] )                     , lambda X: {1,2,3} if 1 in X else {2,3}         ),
    (( {1,2,3}, [{1},{2},{1,2},{1,3},{2,3},{1,2,3}] )           , lambda X: {3} if X <= {3} else {1,2,3}         ),
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )       , lambda X: {1,2,3} if X else X                  ),
    (( {1,2,3}, [{1,2},{1,2,3}] )                               , lambda X: X | {3}                              ),
    (( {1,2,3}, [{1,2},{1,3},{1,2,3}] )                         , lambda X: X if X <= {1} else X | {2,3}         ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )                   , lambda X: X if len(X) <= 1 else {1,2,3}        ),
    (( {1,2,3}, [{1,2,3}] )                                     , lambda X: X                                    ),
])
def test_closure_function_from_spanning_sets_matroid(spanning_sets_matroid, expected):
    E, _ = spanning_sets_matroid
    cl1 = closure_function_from_spanning_sets_matroid(spanning_sets_matroid)
    cl2 = expected
    assert all(cl1(X) == cl2(X) for X in powset(E))


@pytest.mark.parametrize('independent_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , [{1,2,3}]                                     ),
    (( {1,2,3}, [set(),{1}] )                                  , [{2,3},{1,2,3}]                               ),
    (( {1,2,3}, [set(),{1},{2}] )                              , [{3},{1,2,3}]                                 ),
    (( {1,2,3}, [set(),{1},{2},{3}] )                          , [set(),{1,2,3}]                               ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , [{3},{1,3},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3}] )              , [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3}] )        , [set(),{1},{2},{3},{1,2,3}]                   ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_flats_from_independent_matroid(independent_matroid, expected):
    Fs1 = flats_from_independent_matroid(independent_matroid)
    Fs2 = expected
    assert all(map(lambda F1: F1 in Fs2, Fs1)) and all(map(lambda F2: F2 in Fs1, Fs2))


@pytest.mark.parametrize('dependent_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [{1,2,3}]                                     ),
    (( {1,2,3}, [{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )    , [{2,3},{1,2,3}]                               ),
    (( {1,2,3}, [{3},{1,2},{1,3},{2,3},{1,2,3}] )        , [{3},{1,2,3}]                                 ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )            , [set(),{1,2,3}]                               ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )              , [{3},{1,3},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                        , [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{1,2,3}] )                              , [set(),{1},{2},{3},{1,2,3}]                   ),
    (( {1,2,3}, [] )                                     , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_flats_from_dependent_matroid(dependent_matroid, expected):
    Fs1 = flats_from_dependent_matroid(dependent_matroid)
    Fs2 = expected
    assert all(map(lambda F1: F1 in Fs2, Fs1)) and all(map(lambda F2: F2 in Fs1, Fs2))


@pytest.mark.parametrize('bases_matroid, expected', [
    (( {1,2,3}, [set()] )            , [{1,2,3}]                                     ),
    (( {1,2,3}, [{1}] )              , [{2,3},{1,2,3}]                               ),
    (( {1,2,3}, [{1},{2}] )          , [{3},{1,2,3}]                                 ),
    (( {1,2,3}, [{1},{2},{3}] )      , [set(),{1,2,3}]                               ),
    (( {1,2,3}, [{1,2}] )            , [{3},{1,3},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{1,2},{1,3}] )      , [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), [set(),{1},{2},{3},{1,2,3}]                   ),
    (( {1,2,3}, [{1,2,3}] )          , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_flats_from_bases_matroid(bases_matroid, expected):
    Fs1 = flats_from_bases_matroid(bases_matroid)
    Fs2 = expected
    assert all(map(lambda F1: F1 in Fs2, Fs1)) and all(map(lambda F2: F2 in Fs1, Fs2))


@pytest.mark.parametrize('circuits_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3}] )      , [{1,2,3}]                                     ),
    (( {1,2,3}, [{2},{3}] )          , [{2,3},{1,2,3}]                               ),
    (( {1,2,3}, [{3},{1,2}] )        , [{3},{1,2,3}]                                 ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), [set(),{1,2,3}]                               ),
    (( {1,2,3}, [{3}] )              , [{3},{1,3},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{2,3}] )            , [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{1,2,3}] )          , [set(),{1},{2},{3},{1,2,3}]                   ),
    (( {1,2,3}, [] )                 , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_flats_from_circuits_matroid(circuits_matroid, expected):
    Fs1 = flats_from_circuits_matroid(circuits_matroid)
    Fs2 = expected
    assert all(map(lambda F1: F1 in Fs2, Fs1)) and all(map(lambda F2: F2 in Fs1, Fs2))


@pytest.mark.parametrize('rank_matroid, expected', [
    (( {1,2,3}, lambda X: 0 )                                   , [{1,2,3}]                                     ),
    (( {1,2,3}, lambda X: 1 if 1 in X else 0 )                  , [{2,3},{1,2,3}]                               ),
    (( {1,2,3}, lambda X: 0 if X <= {3} else 1 )                , [{3},{1,2,3}]                                 ),
    (( {1,2,3}, lambda X: 1 if X else 0 )                       , [set(),{1,2,3}]                               ),
    (( {1,2,3}, lambda X: len(X) - 1 if 3 in X else len(X) )    , [{3},{1,3},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, lambda X: len(X) - 1 if {2,3} <= X else len(X) ), [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, lambda X: 2 if X == {1,2,3} else len(X) )       , [set(),{1},{2},{3},{1,2,3}]                   ),
    (( {1,2,3}, len )                                           , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_flats_from_rank_matroid(rank_matroid, expected):
    Fs1 = flats_from_rank_matroid(rank_matroid)
    Fs2 = expected
    assert all(map(lambda F1: F1 in Fs2, Fs1)) and all(map(lambda F2: F2 in Fs1, Fs2))


@pytest.mark.parametrize('closure_matroid, expected', [
    (( {1,2,3}, lambda X: {1,2,3} )                      , [{1,2,3}]                                     ),
    (( {1,2,3}, lambda X: {1,2,3} if 1 in X else {2,3} ) , [{2,3},{1,2,3}]                               ),
    (( {1,2,3}, lambda X: {3} if X <= {3} else {1,2,3} ) , [{3},{1,2,3}]                                 ),
    (( {1,2,3}, lambda X: {1,2,3} if X else X )          , [set(),{1,2,3}]                               ),
    (( {1,2,3}, lambda X: X | {3} )                      , [{3},{1,3},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, lambda X: X if X <= {1} else X | {2,3} ) , [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, lambda X: X if len(X) <= 1 else {1,2,3} ), [set(),{1},{2},{3},{1,2,3}]                   ),
    (( {1,2,3}, lambda X: X )                            , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_flats_from_closure_matroid(closure_matroid, expected):
    Fs1 = flats_from_closure_matroid(closure_matroid)
    Fs2 = expected
    assert all(map(lambda F1: F1 in Fs2, Fs1)) and all(map(lambda F2: F2 in Fs1, Fs2))


@pytest.mark.parametrize('open_sets_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , [{1,2,3}]                                     ),
    (( {1,2,3}, [set(),{1}] )                                  , [{2,3},{1,2,3}]                               ),
    (( {1,2,3}, [set(),{1,2}] )                                , [{3},{1,2,3}]                                 ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , [set(),{1,2,3}]                               ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , [{3},{1,3},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [set(),{1,2},{1,3},{2,3},{1,2,3}] )            , [set(),{1},{2},{3},{1,2,3}]                   ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_flats_from_open_sets_matroid(open_sets_matroid, expected):
    Fs1 = flats_from_open_sets_matroid(open_sets_matroid)
    Fs2 = expected
    assert all(map(lambda F1: F1 in Fs2, Fs1)) and all(map(lambda F2: F2 in Fs1, Fs2))


@pytest.mark.parametrize('hyperplanes_matroid, expected', [
    (( {1,2,3}, [] )                 , [{1,2,3}]                                     ),
    (( {1,2,3}, [{2,3}] )            , [{2,3},{1,2,3}]                               ),
    (( {1,2,3}, [{3}] )              , [{3},{1,2,3}]                                 ),
    (( {1,2,3}, [set()] )            , [set(),{1,2,3}]                               ),
    (( {1,2,3}, [{1,3},{2,3}] )      , [{3},{1,3},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{1},{2,3}] )        , [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{1},{2},{3}] )      , [set(),{1},{2},{3},{1,2,3}]                   ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_flats_from_hyperplanes_matroid(hyperplanes_matroid, expected):
    Fs1 = flats_from_hyperplanes_matroid(hyperplanes_matroid)
    Fs2 = expected
    assert all(map(lambda F1: F1 in Fs2, Fs1)) and all(map(lambda F2: F2 in Fs1, Fs2))


@pytest.mark.parametrize('spanning_sets_matroid, expected', [
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [{1,2,3}]                                     ),
    (( {1,2,3}, [{1},{1,2},{1,3},{1,2,3}] )                    , [{2,3},{1,2,3}]                               ),
    (( {1,2,3}, [{1},{2},{1,2},{1,3},{2,3},{1,2,3}] )          , [{3},{1,2,3}]                                 ),
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )      , [set(),{1,2,3}]                               ),
    (( {1,2,3}, [{1,2},{1,2,3}] )                              , [{3},{1,3},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{1,2},{1,3},{1,2,3}] )                        , [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )                  , [set(),{1},{2},{3},{1,2,3}]                   ),
    (( {1,2,3}, [{1,2,3}] )                                    , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_flats_from_spanning_sets_matroid(spanning_sets_matroid, expected):
    Fs1 = flats_from_spanning_sets_matroid(spanning_sets_matroid)
    Fs2 = expected
    assert all(map(lambda F1: F1 in Fs2, Fs1)) and all(map(lambda F2: F2 in Fs1, Fs2))


@pytest.mark.parametrize('independent_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , [set()]                                       ),
    (( {1,2,3}, [set(),{1}] )                                  , [set(),{1}]                                   ),
    (( {1,2,3}, [set(),{1},{2}] )                              , [set(),{1,2}]                                 ),
    (( {1,2,3}, [set(),{1},{2},{3}] )                          , [set(),{1,2,3}]                               ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , [set(),{1},{2},{1,2}]                         ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3}] )              , [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3}] )        , [set(),{1,2},{1,3},{2,3},{1,2,3}]             ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_open_sets_from_independent_matroid(independent_matroid, expected):
    Os1 = open_sets_from_independent_matroid(independent_matroid)
    Os2 = expected
    assert all(map(lambda O1: O1 in Os2, Os1)) and all(map(lambda O2: O2 in Os1, Os2))


@pytest.mark.parametrize('dependent_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [set()]                                       ),
    (( {1,2,3}, [{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )    , [set(),{1}]                                   ),
    (( {1,2,3}, [{3},{1,2},{1,3},{2,3},{1,2,3}] )        , [set(),{1,2}]                                 ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )            , [set(),{1,2,3}]                               ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )              , [set(),{1},{2},{1,2}]                         ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                        , [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{1,2,3}] )                              , [set(),{1,2},{1,3},{2,3},{1,2,3}]             ),
    (( {1,2,3}, [] )                                     , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_open_sets_from_dependent_matroid(dependent_matroid, expected):
    Os1 = open_sets_from_dependent_matroid(dependent_matroid)
    Os2 = expected
    assert all(map(lambda O1: O1 in Os2, Os1)) and all(map(lambda O2: O2 in Os1, Os2))


@pytest.mark.parametrize('bases_matroid, expected', [
    (( {1,2,3}, [set()] )            , [set()]                                       ),
    (( {1,2,3}, [{1}] )              , [set(),{1}]                                   ),
    (( {1,2,3}, [{1},{2}] )          , [set(),{1,2}]                                 ),
    (( {1,2,3}, [{1},{2},{3}] )      , [set(),{1,2,3}]                               ),
    (( {1,2,3}, [{1,2}] )            , [set(),{1},{2},{1,2}]                         ),
    (( {1,2,3}, [{1,2},{1,3}] )      , [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), [set(),{1,2},{1,3},{2,3},{1,2,3}]             ),
    (( {1,2,3}, [{1,2,3}] )          , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_open_sets_from_bases_matroid(bases_matroid, expected):
    Os1 = open_sets_from_bases_matroid(bases_matroid)
    Os2 = expected
    assert all(map(lambda O1: O1 in Os2, Os1)) and all(map(lambda O2: O2 in Os1, Os2))


@pytest.mark.parametrize('circuits_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3}] )      , [set()]                                       ),
    (( {1,2,3}, [{2},{3}] )          , [set(),{1}]                                   ),
    (( {1,2,3}, [{3},{1,2}] )        , [set(),{1,2}]                                 ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), [set(),{1,2,3}]                               ),
    (( {1,2,3}, [{3}] )              , [set(),{1},{2},{1,2}]                         ),
    (( {1,2,3}, [{2,3}] )            , [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{1,2,3}] )          , [set(),{1,2},{1,3},{2,3},{1,2,3}]             ),
    (( {1,2,3}, [] )                 , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_open_sets_from_circuits_matroid(circuits_matroid, expected):
    Os1 = open_sets_from_circuits_matroid(circuits_matroid)
    Os2 = expected
    assert all(map(lambda O1: O1 in Os2, Os1)) and all(map(lambda O2: O2 in Os1, Os2))


@pytest.mark.parametrize('rank_matroid, expected', [
    (( {1,2,3}, lambda X: 0 )                                   , [set()]                                       ),
    (( {1,2,3}, lambda X: 1 if 1 in X else 0 )                  , [set(),{1}]                                   ),
    (( {1,2,3}, lambda X: 0 if X <= {3} else 1 )                , [set(),{1,2}]                                 ),
    (( {1,2,3}, lambda X: 1 if X else 0 )                       , [set(),{1,2,3}]                               ),
    (( {1,2,3}, lambda X: len(X) - 1 if 3 in X else len(X) )    , [set(),{1},{2},{1,2}]                         ),
    (( {1,2,3}, lambda X: len(X) - 1 if {2,3} <= X else len(X) ), [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, lambda X: 2 if X == {1,2,3} else len(X) )       , [set(),{1,2},{1,3},{2,3},{1,2,3}]             ),
    (( {1,2,3}, len )                                           , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_open_sets_from_rank_matroid(rank_matroid, expected):
    Os1 = open_sets_from_rank_matroid(rank_matroid)
    Os2 = expected
    assert all(map(lambda O1: O1 in Os2, Os1)) and all(map(lambda O2: O2 in Os1, Os2))


@pytest.mark.parametrize('closure_matroid, expected', [
    (( {1,2,3}, lambda X: {1,2,3} )                      , [set()]                                       ),
    (( {1,2,3}, lambda X: {1,2,3} if 1 in X else {2,3} ) , [set(),{1}]                                   ),
    (( {1,2,3}, lambda X: {3} if X <= {3} else {1,2,3} ) , [set(),{1,2}]                                 ),
    (( {1,2,3}, lambda X: {1,2,3} if X else X )          , [set(),{1,2,3}]                               ),
    (( {1,2,3}, lambda X: X | {3} )                      , [set(),{1},{2},{1,2}]                         ),
    (( {1,2,3}, lambda X: X if X <= {1} else X | {2,3} ) , [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, lambda X: X if len(X )<= 1 else {1,2,3} ), [set(),{1,2},{1,3},{2,3},{1,2,3}]             ),
    (( {1,2,3}, lambda X: X )                            , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_open_sets_from_closure_matroid(closure_matroid, expected):
    Os1 = open_sets_from_closure_matroid(closure_matroid)
    Os2 = expected
    assert all(map(lambda O1: O1 in Os2, Os1)) and all(map(lambda O2: O2 in Os1, Os2))


@pytest.mark.parametrize('flats_matroid, expected', [
    (( {1,2,3}, [{1,2,3}] )                                    , [set()]                                       ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                              , [set(),{1}]                                   ),
    (( {1,2,3}, [{3},{1,2,3}] )                                , [set(),{1,2}]                                 ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , [set(),{1,2,3}]                               ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )                    , [set(),{1},{2},{1,2}]                         ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2,3}] )                  , [set(),{1,2},{1,3},{2,3},{1,2,3}]             ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_open_sets_from_flats_matroid(flats_matroid, expected):
    Os1 = open_sets_from_flats_matroid(flats_matroid)
    Os2 = expected
    assert all(map(lambda O1: O1 in Os2, Os1)) and all(map(lambda O2: O2 in Os1, Os2))


@pytest.mark.parametrize('hyperplanes_matroid, expected', [
    (( {1,2,3}, [] )                 , [set()]                                       ),
    (( {1,2,3}, [{2,3}] )            , [set(),{1}]                                   ),
    (( {1,2,3}, [{3}] )              , [set(),{1,2}]                                 ),
    (( {1,2,3}, [set()] )            , [set(),{1,2,3}]                               ),
    (( {1,2,3}, [{1,3},{2,3}] )      , [set(),{1},{2},{1,2}]                         ),
    (( {1,2,3}, [{1},{2,3}] )        , [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{1},{2},{3}] )      , [set(),{1,2},{1,3},{2,3},{1,2,3}]             ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_open_sets_from_hyperplanes_matroid(hyperplanes_matroid, expected):
    Os1 = open_sets_from_hyperplanes_matroid(hyperplanes_matroid)
    Os2 = expected
    assert all(map(lambda O1: O1 in Os2, Os1)) and all(map(lambda O2: O2 in Os1, Os2))


@pytest.mark.parametrize('spanning_sets_matroid, expected', [
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [set()]                                       ),
    (( {1,2,3}, [{1},{1,2},{1,3},{1,2,3}] )                    , [set(),{1}]                                   ),
    (( {1,2,3}, [{1},{2},{1,2},{1,3},{2,3},{1,2,3}] )          , [set(),{1,2}]                                 ),
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )      , [set(),{1,2,3}]                               ),
    (( {1,2,3}, [{1,2},{1,2,3}] )                              , [set(),{1},{2},{1,2}]                         ),
    (( {1,2,3}, [{1,2},{1,3},{1,2,3}] )                        , [set(),{1},{2,3},{1,2,3}]                     ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )                  , [set(),{1,2},{1,3},{2,3},{1,2,3}]             ),
    (( {1,2,3}, [{1,2,3}] )                                    , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_open_sets_from_spanning_sets_matroid(spanning_sets_matroid, expected):
    Os1 = open_sets_from_spanning_sets_matroid(spanning_sets_matroid)
    Os2 = expected
    assert all(map(lambda O1: O1 in Os2, Os1)) and all(map(lambda O2: O2 in Os1, Os2))


@pytest.mark.parametrize('independent_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , []                  ),
    (( {1,2,3}, [set(),{1}] )                                  , [{2,3}]             ),
    (( {1,2,3}, [set(),{1},{2}] )                              , [{3}]               ),
    (( {1,2,3}, [set(),{1},{2},{3}] )                          , [set()]             ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , [{1,3},{2,3}]       ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3}] )              , [{1},{2,3}]         ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3}] )        , [{1},{2},{3}]       ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [{1,2},{1,3},{2,3}] ),
])
def test_hyperplanes_from_independent_matroid(independent_matroid, expected):
    Hs1 = hyperplanes_from_independent_matroid(independent_matroid)
    Hs2 = expected
    assert all(map(lambda H1: H1 in Hs2, Hs1)) and all(map(lambda H2: H2 in Hs1, Hs2))


@pytest.mark.parametrize('dependent_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), []                  ),
    (( {1,2,3}, [{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )    , [{2,3}]             ),
    (( {1,2,3}, [{3},{1,2},{1,3},{2,3},{1,2,3}] )        , [{3}]               ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )            , [set()]             ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )              , [{1,3},{2,3}]       ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                        , [{1},{2,3}]         ),
    (( {1,2,3}, [{1,2,3}] )                              , [{1},{2},{3}]       ),
    (( {1,2,3}, [] )                                     , [{1,2},{1,3},{2,3}] ),
])
def test_hyperplanes_from_dependent_matroid(dependent_matroid, expected):
    Hs1 = hyperplanes_from_dependent_matroid(dependent_matroid)
    Hs2 = expected
    assert all(map(lambda H1: H1 in Hs2, Hs1)) and all(map(lambda H2: H2 in Hs1, Hs2))


@pytest.mark.parametrize('bases_matroid, expected', [
    (( {1,2,3}, [set()] )            , []                  ),
    (( {1,2,3}, [{1}] )              , [{2,3}]             ),
    (( {1,2,3}, [{1},{2}] )          , [{3}]               ),
    (( {1,2,3}, [{1},{2},{3}] )      , [set()]             ),
    (( {1,2,3}, [{1,2}] )            , [{1,3},{2,3}]       ),
    (( {1,2,3}, [{1,2},{1,3}] )      , [{1},{2,3}]         ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), [{1},{2},{3}]       ),
    (( {1,2,3}, [{1,2,3}] )          , [{1,2},{1,3},{2,3}] ),
])
def test_hyperplanes_from_bases_matroid(bases_matroid, expected):
    Hs1 = hyperplanes_from_bases_matroid(bases_matroid)
    Hs2 = expected
    assert all(map(lambda H1: H1 in Hs2, Hs1)) and all(map(lambda H2: H2 in Hs1, Hs2))


@pytest.mark.parametrize('circuits_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3}] )      , []                  ),
    (( {1,2,3}, [{2},{3}] )          , [{2,3}]             ),
    (( {1,2,3}, [{3},{1,2}] )        , [{3}]               ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), [set()]             ),
    (( {1,2,3}, [{3}] )              , [{1,3},{2,3}]       ),
    (( {1,2,3}, [{2,3}] )            , [{1},{2,3}]         ),
    (( {1,2,3}, [{1,2,3}] )          , [{1},{2},{3}]       ),
    (( {1,2,3}, [] )                 , [{1,2},{1,3},{2,3}] ),
])
def test_hyperplanes_from_circuits_matroid(circuits_matroid, expected):
    Hs1 = hyperplanes_from_circuits_matroid(circuits_matroid)
    Hs2 = expected
    assert all(map(lambda H1: H1 in Hs2, Hs1)) and all(map(lambda H2: H2 in Hs1, Hs2))


@pytest.mark.parametrize('rank_matroid, expected', [
    (( {1,2,3}, lambda X: 0 )                                   , []                  ),
    (( {1,2,3}, lambda X: 1 if 1 in X else 0 )                  , [{2,3}]             ),
    (( {1,2,3}, lambda X: 0 if X <= {3} else 1 )                , [{3}]               ),
    (( {1,2,3}, lambda X: 1 if X else 0 )                       , [set()]             ),
    (( {1,2,3}, lambda X: len(X) - 1 if 3 in X else len(X) )    , [{1,3},{2,3}]       ),
    (( {1,2,3}, lambda X: len(X) - 1 if {2,3} <= X else len(X) ), [{1},{2,3}]         ),
    (( {1,2,3}, lambda X: 2 if X == {1,2,3} else len(X) )       , [{1},{2},{3}]       ),
    (( {1,2,3}, len )                                           , [{1,2},{1,3},{2,3}] ),
])
def test_hyperplanes_from_rank_matroid(rank_matroid, expected):
    Hs1 = hyperplanes_from_rank_matroid(rank_matroid)
    Hs2 = expected
    assert all(map(lambda H1: H1 in Hs2, Hs1)) and all(map(lambda H2: H2 in Hs1, Hs2))


@pytest.mark.parametrize('closure_matroid, expected', [
    (( {1,2,3}, lambda X: {1,2,3} )                      , []                  ),
    (( {1,2,3}, lambda X: {1,2,3} if 1 in X else {2,3} ) , [{2,3}]             ),
    (( {1,2,3}, lambda X: {3} if X <= {3} else {1,2,3} ) , [{3}]               ),
    (( {1,2,3}, lambda X: {1,2,3} if X else X )          , [set()]             ),
    (( {1,2,3}, lambda X: X | {3} )                      , [{1,3},{2,3}]       ),
    (( {1,2,3}, lambda X: X if X <= {1} else X | {2,3} ) , [{1},{2,3}]         ),
    (( {1,2,3}, lambda X: X if len(X) <= 1 else {1,2,3} ), [{1},{2},{3}]       ),
    (( {1,2,3}, lambda X: X )                            , [{1,2},{1,3},{2,3}] ),
])
def test_hyperplanes_from_closure_matroid(closure_matroid, expected):
    Hs1 = hyperplanes_from_closure_matroid(closure_matroid)
    Hs2 = expected
    assert all(map(lambda H1: H1 in Hs2, Hs1)) and all(map(lambda H2: H2 in Hs1, Hs2))


@pytest.mark.parametrize('flats_matroid, expected', [
    (( {1,2,3}, [{1,2,3}]                                     ), []                  ),
    (( {1,2,3}, [{2,3},{1,2,3}]                               ), [{2,3}]             ),
    (( {1,2,3}, [{3},{1,2,3}]                                 ), [{3}]               ),
    (( {1,2,3}, [set(),{1,2,3}]                               ), [set()]             ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}]                     ), [{1,3},{2,3}]       ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}]                     ), [{1},{2,3}]         ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2,3}]                   ), [{1},{2},{3}]       ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [{1,2},{1,3},{2,3}] ),
])
def test_hyperplanes_from_flats_matroid(flats_matroid, expected):
    Hs1 = hyperplanes_from_flats_matroid(flats_matroid)
    Hs2 = expected
    assert all(map(lambda H1: H1 in Hs2, Hs1)) and all(map(lambda H2: H2 in Hs1, Hs2))


@pytest.mark.parametrize('open_sets_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , []                  ),
    (( {1,2,3}, [set(),{1}] )                                  , [{2,3}]             ),
    (( {1,2,3}, [set(),{1,2}] )                                , [{3}]               ),
    (( {1,2,3}, [set(),{1,2,3}] )                              , [set()]             ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , [{1,3},{2,3}]       ),
    (( {1,2,3}, [set(),{1},{2,3},{1,2,3}] )                    , [{1},{2,3}]         ),
    (( {1,2,3}, [set(),{1,2},{1,3},{2,3},{1,2,3}] )            , [{1},{2},{3}]       ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [{1,2},{1,3},{2,3}] ),
])
def test_hyperplanes_from_open_sets_matroid(open_sets_matroid, expected):
    Hs1 = hyperplanes_from_open_sets_matroid(open_sets_matroid)
    Hs2 = expected
    assert all(map(lambda H1: H1 in Hs2, Hs1)) and all(map(lambda H2: H2 in Hs1, Hs2))


@pytest.mark.parametrize('spanning_sets_matroid, expected', [
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), []                  ),
    (( {1,2,3}, [{1},{1,2},{1,3},{1,2,3}] )                    , [{2,3}]             ),
    (( {1,2,3}, [{1},{2},{1,2},{1,3},{2,3},{1,2,3}] )          , [{3}]               ),
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )      , [set()]             ),
    (( {1,2,3}, [{1,2},{1,2,3}] )                              , [{1,3},{2,3}]       ),
    (( {1,2,3}, [{1,2},{1,3},{1,2,3}] )                        , [{1},{2,3}]         ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )                  , [{1},{2},{3}]       ),
    (( {1,2,3}, [{1,2,3}] )                                    , [{1,2},{1,3},{2,3}] ),
])
def test_hyperplanes_from_spanning_sets_matroid(spanning_sets_matroid, expected):
    Hs1 = hyperplanes_from_spanning_sets_matroid(spanning_sets_matroid)
    Hs2 = expected
    assert all(map(lambda H1: H1 in Hs2, Hs1)) and all(map(lambda H2: H2 in Hs1, Hs2))


@pytest.mark.parametrize('independent_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
    (( {1,2,3}, [set(),{1}] )                                  , [{1},{1,2},{1,3},{1,2,3}]                     ),
    (( {1,2,3}, [set(),{1},{2}] )                              , [{1},{2},{1,2},{1,3},{2,3},{1,2,3}]           ),
    (( {1,2,3}, [set(),{1},{2},{3}] )                          , [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}]       ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , [{1,2},{1,2,3}]                               ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3}] )              , [{1,2},{1,3},{1,2,3}]                         ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3}] )        , [{1,2},{1,3},{2,3},{1,2,3}]                   ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [{1,2,3}]                                     ),
])
def test_spanning_sets_from_independent_matroid(independent_matroid, expected):
    Ss1 = spanning_sets_from_independent_matroid(independent_matroid)
    Ss2 = expected
    assert all(map(lambda S1: S1 in Ss2, Ss1)) and all(map(lambda S2: S2 in Ss1, Ss2))


@pytest.mark.parametrize('bases_matroid, expected', [
    (( {1,2,3}, [set()] )            , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
    (( {1,2,3}, [{1}] )              , [{1},{1,2},{1,3},{1,2,3}]                     ),
    (( {1,2,3}, [{1},{2}] )          , [{1},{2},{1,2},{1,3},{2,3},{1,2,3}]           ),
    (( {1,2,3}, [{1},{2},{3}] )      , [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}]       ),
    (( {1,2,3}, [{1,2}] )            , [{1,2},{1,2,3}]                               ),
    (( {1,2,3}, [{1,2},{1,3}] )      , [{1,2},{1,3},{1,2,3}]                         ),
    (( {1,2,3}, [{1,2},{1,3},{2,3}] ), [{1,2},{1,3},{2,3},{1,2,3}]                   ),
    (( {1,2,3}, [{1,2,3}] )          , [{1,2,3}]                                     ),
])
def test_spanning_sets_from_bases_matroid(bases_matroid, expected):
    Ss1 = spanning_sets_from_bases_matroid(bases_matroid)
    Ss2 = expected
    assert all(map(lambda S1: S1 in Ss2, Ss1)) and all(map(lambda S2: S2 in Ss1, Ss2))


@pytest.mark.parametrize('rank_matroid, expected', [
    (( {1,2,3}, lambda X: 0 )                                   , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
    (( {1,2,3}, lambda X: 1 if 1 in X else 0 )                  , [{1},{1,2},{1,3},{1,2,3}]                     ),
    (( {1,2,3}, lambda X: 0 if X <= {0,3} else 1 )              , [{1},{2},{1,2},{1,3},{2,3},{1,2,3}]           ),
    (( {1,2,3}, lambda X: 1 if X else 0 )                       , [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}]       ),
    (( {1,2,3}, lambda X: len(X) - 1 if 3 in X else len(X) )    , [{1,2},{1,2,3}]                               ),
    (( {1,2,3}, lambda X: len(X) - 1 if {2,3} <= X else len(X) ), [{1,2},{1,3},{1,2,3}]                         ),
    (( {1,2,3}, lambda X: 2 if X == {1,2,3} else len(X) )       , [{1,2},{1,3},{2,3},{1,2,3}]                   ),
    (( {1,2,3}, len )                                           , [{1,2,3}]                                     ),
])
def test_spanning_sets_from_rank_matroid(rank_matroid, expected):
    Ss1 = spanning_sets_from_rank_matroid(rank_matroid)
    Ss2 = expected
    assert all(map(lambda S1: S1 in Ss2, Ss1)) and all(map(lambda S2: S2 in Ss1, Ss2))