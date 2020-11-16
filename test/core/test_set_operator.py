import pytest

from matroids.core.set_operator import (
    powset,
    is_minimal,
    is_maximal,
    find_minimal_sets,
    find_maximal_sets
)

@pytest.mark.parametrize('someset, expected', [
    (set()  , [set()]),
    ({1}    , [set(),{1}]),
    ({1,2}  , [set(),{1},{2},{1,2}]),
    ({1,2,3}, [set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}]),
    ({1,2,3,4}, [set(),{1},{2},{3},{4},{1,2},{1,3},{1,4},{2,3},{2,4},{3,4},{1,2,3},{1,2,4},{1,3,4},{2,3,4},{1,2,3,4}])
])
def test_powset(someset, expected):
    P = powset(someset)
    assert all(map(lambda X: X in expected, P)) and all(map(lambda X: X in P, expected))


@pytest.mark.parametrize("someset, family, expected", [
    ({1,2}  , [{1,2},{1,3},{2,3}]                    ,  True),
    ({1}    , [set(),{1},{2},{3},{1,2},{1,3},{1,2,3}],  True),
    (set()  , [set()]                                , False),
    ({1,2,3}, [{1,2},{1,2,3}]                        , False),
    ({1,2}  , [{1},{1,2},{1,2,3}]                    , False)
])
def test_is_minimal(someset, family, expected):
    assert is_minimal(someset, family) == expected


@pytest.mark.parametrize("someset, family, expected", [
    ({1,2,3}, [{1,2},{1,3},{2,3},{1,2,3}]  ,  True),
    ({1,2}, [set(),{1},{2},{3},{1,2},{1,3}],  True),
    (set(), [set()]                        ,  True),
    (set(), [set(), {1}]                   , False),
    ({1,2}, [{1,2},{1,2,3}]                , False),
    ({1}, [{1},{1,2}]                      , False)
])
def test_is_maximal(someset, family, expected):
    assert is_maximal(someset, family) == expected