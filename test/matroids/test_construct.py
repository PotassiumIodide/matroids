import pytest

from src.utils.set_operator import powset

from src.matroids.construct import (
    indeps_from_deps_matroid,
    indeps_from_bases_matroid,
    indeps_from_circuits_matroid,
    indeps_from_rank_matroid,
    indeps_from_closure_matroid,
    deps_from_indeps_matroid,
    deps_from_bases_matroid,
    deps_from_circuits_matroid,
    deps_from_rank_matroid,
    deps_from_closure_matroid,
    bases_from_indeps_matroid,
    bases_from_deps_matroid,
    bases_from_circuits_matroid,
    bases_from_rank_matroid,
    bases_from_closure_matroid,
    circuits_from_indeps_matroid,
    circuits_from_deps_matroid,
    circuits_from_bases_matroid,
    circuits_from_rank_matroid,
    circuits_from_closure_matroid,
    rank_function_from_indeps_matroid,
    rank_function_from_deps_matroid,
    rank_function_from_bases_matroid,
    rank_function_from_circuits_matroid,
    rank_function_from_closure_matroid,
    closure_function_from_indeps_matroid,
    closure_function_from_deps_matroid,
    closure_function_from_bases_matroid,
    closure_function_from_circuits_matroid,
    closure_function_from_rank_matroid,
)


# TODO: Make a test case when a given pair is not a matroid.
@pytest.mark.parametrize('deps_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [set()]                                       ),
    (( {1,2,3}, [{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )    , [set(), {1}]                                  ),
    (( {1,2,3}, [{3},{1,2},{1,3},{2,3},{1,2,3}] )        , [set(), {1},{2}]                              ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )            , [set(), {1},{2},{3}]                          ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )              , [set(), {1},{2},{1,2}]                        ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                        , [set(),{1},{2},{3},{1,2},{1,3}]               ),
    (( {1,2,3}, [{1,2,3}] )                              , [set(),{1},{2},{3},{1,2},{1,3},{2,3}]         ),
    (( {1,2,3}, [] )                                     , [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
])
def test_indeps_from_deps_matroid(deps_matroid, expected):
    Is1 = indeps_from_deps_matroid(deps_matroid)
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
def test_indeps_from_bases_matroid(bases_matroid, expected):
    Is1 = indeps_from_bases_matroid(bases_matroid)
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
def test_indeps_from_circuits_matroid(circuits_matroid, expected):
    Is1 = indeps_from_circuits_matroid(circuits_matroid)
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
def test_indeps_from_rank_matroid(rank_matroid, expected):
    Is1 = indeps_from_rank_matroid(rank_matroid)
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
def test_indeps_from_closure_matroid(closure_matroid, expected):
    Is1 = indeps_from_closure_matroid(closure_matroid)
    Is2 = expected
    assert all(map(lambda I1: I1 in Is2, Is1)) and all(map(lambda I2: I2 in Is1, Is2))


@pytest.mark.parametrize('indeps_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ),
    (( {1,2,3}, [set(),{1}] )                                  , [{2},{3},{1,2},{1,3},{2,3},{1,2,3}]     ),
    (( {1,2,3}, [set(),{1},{2}] )                              , [{3},{1,2},{1,3},{2,3},{1,2,3}]         ),
    (( {1,2,3}, [set(),{1},{2},{3}] )                          , [{1,2},{1,3},{2,3},{1,2,3}]             ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , [{3},{1,3},{2,3},{1,2,3}]               ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3}] )              , [{2,3},{1,2,3}]                         ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3}] )        , [{1,2,3}]                               ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), []                                      ),
])
def test_deps_from_indeps_matroid(indeps_matroid, expected):
    Ds1 = deps_from_indeps_matroid(indeps_matroid)
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
def test_deps_from_bases_matroid(bases_matroid, expected):
    Ds1 = deps_from_bases_matroid(bases_matroid)
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
def test_deps_from_circuits_matroid(circuits_matroid, expected):
    Ds1 = deps_from_circuits_matroid(circuits_matroid)
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
def test_deps_from_rank_matroid(rank_matroid, expected):
    Ds1 = deps_from_rank_matroid(rank_matroid)
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
def test_deps_from_closure_matroid(closure_matroid, expected):
    Ds1 = deps_from_closure_matroid(closure_matroid)
    Ds2 = expected
    assert all(map(lambda D1: D1 in Ds2, Ds1)) and all(map(lambda D2: D2 in Ds1, Ds2))


@pytest.mark.parametrize('indeps_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , [set()]             ),
    (( {1,2,3}, [set(),{1}] )                                  , [{1}]               ),
    (( {1,2,3}, [set(),{1},{2}] )                              , [{1},{2}]           ),
    (( {1,2,3}, [set(),{1},{2},{3}] )                          , [{1},{2},{3}]       ),
    (( {1,2,3}, [set(),{1},{1,2}] )                            , [{1,2}]             ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3}] )              , [{1,2},{1,3}]       ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3}] )        , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [{1,2,3}]           ),
])
def test_bases_from_indeps_matroid(indeps_matroid, expected):
    Bs1 = bases_from_indeps_matroid(indeps_matroid)
    Bs2 = expected
    assert all(map(lambda B1: B1 in Bs2, Bs1)) and all(map(lambda B2: B2 in Bs1, Bs2))


@pytest.mark.parametrize('deps_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [set()]             ),
    (( {1,2,3}, [{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )    , [{1}]               ),
    (( {1,2,3}, [{3},{1,2},{1,3},{2,3},{1,2,3}] )        , [{1},{2}]           ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )            , [{1},{2},{3}]       ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )              , [{1,2}]             ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                        , [{1,2},{1,3}]       ),
    (( {1,2,3}, [{1,2,3}] )                              , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [] )                                     , [{1,2,3}]           ),
])
def test_bases_from_deps_matroid(deps_matroid, expected):
    Bs1 = bases_from_deps_matroid(deps_matroid)
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


@pytest.mark.parametrize('indeps_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , [{1},{2},{3}]       ),
    (( {1,2,3}, [set(),{1}] )                                  , [{2},{3}]           ),
    (( {1,2,3}, [set(),{1},{2}] )                              , [{1,2},{3}]         ),
    (( {1,2,3}, [set(),{1},{2},{3}] )                          , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , [{3}]               ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3}] )              , [{2,3}]             ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3}] )        , [{1,2,3}]           ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), []                  ),
])
def test_circuits_from_indeps_matroid(indeps_matroid, expected):
    Cs1 = circuits_from_indeps_matroid(indeps_matroid)
    Cs2 = expected
    assert all(map(lambda C1: C1 in Cs2, Cs1)) and all(map(lambda C2: C2 in Cs1, Cs2))


@pytest.mark.parametrize('deps_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), [{1},{2},{3}]       ),
    (( {1,2,3}, [{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )    , [{2},{3}]           ),
    (( {1,2,3}, [{3},{1,2},{1,3},{2,3},{1,2,3}] )        , [{1,2},{3}]         ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )            , [{1,2},{1,3},{2,3}] ),
    (( {1,2,3}, [{3},{1,3},{2,3}] )                      , [{3}]               ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                        , [{2,3}]             ),
    (( {1,2,3}, [{1,2,3}] )                              , [{1,2,3}]           ),
    (( {1,2,3}, [] )                                     , []                  ),
])
def test_circuits_from_deps_matroid(deps_matroid, expected):
    Cs1 = circuits_from_deps_matroid(deps_matroid)
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


@pytest.mark.parametrize('indeps_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , lambda X: 0                                    ),
    (( {1,2,3}, [set(),{1}] )                                  , lambda X: 1 if 1 in X else 0                   ),
    (( {1,2,3}, [set(),{1},{2}] )                              , lambda X: 0 if X <= {3} else 1                 ),
    (( {1,2,3}, [set(),{1},{2},{3}] )                          , lambda X: 1 if X else 0                        ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , lambda X: len(X) - 1 if 3 in X else len(X)     ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3}] )              , lambda X: len(X) - 1 if {2,3} <= X else len(X) ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3}] )        , lambda X: 2 if X == {1,2,3} else len(X)        ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), len                                            ),
])
def test_rank_function_from_indeps_matroid(indeps_matroid, expected):
    E, _ = indeps_matroid
    r1 = rank_function_from_indeps_matroid(indeps_matroid)
    r2 = expected
    assert all(r1(X) == r2(X) for X in powset(E))


@pytest.mark.parametrize('deps_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), lambda X: 0                                    ),
    (( {1,2,3}, [{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )    , lambda X: 1 if 1 in X else 0                   ),
    (( {1,2,3}, [{3},{1,2},{1,3},{2,3},{1,2,3}] )        , lambda X: 0 if X <= {3} else 1                 ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )            , lambda X: 1 if X else 0                        ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )              , lambda X: len(X) - 1 if 3 in X else len(X)     ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                        , lambda X: len(X) - 1 if {2,3} <= X else len(X) ),
    (( {1,2,3}, [{1,2,3}] )                              , lambda X: 2 if X == {1,2,3} else len(X)        ),
    (( {1,2,3}, [] )                                     , len                                            ),
])
def test_rank_function_from_deps_matroid(deps_matroid, expected):
    E, _ = deps_matroid
    r1 = rank_function_from_deps_matroid(deps_matroid)
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


@pytest.mark.parametrize('indeps_matroid, expected', [
    (( {1,2,3}, [set()] )                                      , lambda X: {1,2,3}                              ),
    (( {1,2,3}, [set(),{1}] )                                  , lambda X: {1,2,3} if 1 in X else {2,3}         ),
    (( {1,2,3}, [set(),{1},{2}] )                              , lambda X: {3} if X <= {3} else {1,2,3}         ),
    (( {1,2,3}, [set(),{1},{2},{3}] )                          , lambda X: {1,2,3} if X else X                  ),
    (( {1,2,3}, [set(),{1},{2},{1,2}] )                        , lambda X: X | {3}                              ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3}] )              , lambda X: X if X <= {1} else X | {2,3}         ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3}] )        , lambda X: X if len(X) <= 1 else {1,2,3}        ),
    (( {1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), lambda X: X                                    ),
])
def test_closure_function_from_indeps_matroid(indeps_matroid, expected):
    E, _ = indeps_matroid
    cl1 = closure_function_from_indeps_matroid(indeps_matroid)
    cl2 = expected
    assert all(cl1(X) == cl2(X) for X in powset(E))


@pytest.mark.parametrize('deps_matroid, expected', [
    (( {1,2,3}, [{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}] ), lambda X: {1,2,3}                              ),
    (( {1,2,3}, [{2},{3},{1,2},{1,3},{2,3},{1,2,3}] )    , lambda X: {1,2,3} if 1 in X else {2,3}         ),
    (( {1,2,3}, [{3},{1,2},{1,3},{2,3},{1,2,3}] )        , lambda X: {3} if X <= {3} else {1,2,3}         ),
    (( {1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}] )            , lambda X: {1,2,3} if X else X                  ),
    (( {1,2,3}, [{3},{1,3},{2,3},{1,2,3}] )              , lambda X: X | {3}                              ),
    (( {1,2,3}, [{2,3},{1,2,3}] )                        , lambda X: X if X <= {1} else X | {2,3}         ),
    (( {1,2,3}, [{1,2,3}] )                              , lambda X: X if len(X) <= 1 else {1,2,3}        ),
    (( {1,2,3}, [] )                                     , lambda X: X                                    ),
])
def test_closure_function_from_deps_matroid(deps_matroid, expected):
    E, _ = deps_matroid
    cl1 = closure_function_from_deps_matroid(deps_matroid)
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