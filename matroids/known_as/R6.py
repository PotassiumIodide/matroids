from matroids.Matroid import Matroid

class R6(Matroid):
    def __init__(self):
        pass

    def __repr__(self) -> str:
        return "R6: Identically self-dual ternary connected matroid of rank 3 on 6 elements, type 2+"

    @property
    def ground_set(self) -> set[int]:
        return {1,2,3,4,5,6}
    
    @property
    def size(self) -> int:
        return 6
    
    @property
    def independent_sets(self) -> list[set[int]]:
        return [
            set(),{1},{2},{3},{4},{5},{6},{1,2},{1,3},{1,4},{1,5},{1,6},
            {2,3},{2,4},{2,5},{2,6},{3,4},{3,5},{3,6},{4,5},{4,6},{5,6},
            {1,2,3},{1,2,4},{1,2,6},{1,3,4},{1,3,5},{1,3,6},{1,4,5},
            {1,4,6},{1,5,6},{2,3,4},{2,3,5},{2,3,6},{2,4,5},{2,4,6},
            {2,5,6},{3,4,5},{3,5,6},{4,5,6}
        ]
    
    @property
    def bases(self) -> list[set[int]]:
        return [
            {1,2,3},{1,2,4},{1,2,6},{1,3,4},{1,3,5},{1,3,6},{1,4,5},
            {1,4,6},{1,5,6},{2,3,4},{2,3,5},{2,3,6},{2,4,5},{2,4,6},
            {2,5,6},{3,4,5},{3,5,6},{4,5,6}
        ]
    
    @property
    def circuits(self) -> list[set[int]]:
        return [
            {1,2,5},{3,4,6},{1,2,3,4},{1,2,3,6},{1,2,4,6},{1,3,4,5},
            {1,3,5,6},{1,4,5,6},{2,3,4,5},{2,3,5,6},{2,4,5,6}
        ]
    
    @property
    def hyperplanes(self) -> list[set[int]]:
        return [{1,3},{1,4},{1,6},{2,3},{2,4},{2,6},{3,5},{4,5},{5,6},{1,2,5},{3,4,6}]
    
    @property
    def cocircuits(self) -> list[set[int]]:
        return [
            {1,2,5},{3,4,6},{1,2,3,4},{1,2,3,6},{1,2,4,6},{1,3,4,5},
            {1,3,5,6},{1,4,5,6},{2,3,4,5},{2,3,5,6},{2,4,5,6}
        ]
    
    def is_binary(self) -> bool:
        return False

    def is_ternary(self) -> bool:
        return True