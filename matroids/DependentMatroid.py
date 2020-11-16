from typing import Callable, TypeVar

from matroids.construct import (
    independent_sets,
    bases,
    circuits,
    rank_function,
    closure_function,
    flats,
    open_sets,
    hyperplanes,
    spanning_sets,
)

from .core.checker import satisfies_dependent_axiom
from .core.exception import MatroidAxiomError
from .Matroid import Matroid
from .core.types import MatroidAxiom

T = TypeVar("T")

class DependentMatroid(Matroid):
    __axiom = MatroidAxiom.DEPENDENT_SETS

    def __init__(self, matroid: tuple[set[T],list[set[T]]]):
        if not satisfies_dependent_axiom(matroid):
            raise MatroidAxiomError(f"The given family doesn't satisfy {self.axiom.value}!")

        self.__ground_set = matroid[0]
        self.__dependent_sets = matroid[1]
    
    @property
    def axiom(self) -> MatroidAxiom:
        return self.__axiom

    @property
    def ground_set(self) -> set[T]:
        return self.__ground_set
    
    @property
    def independent_sets(self) -> list[set[T]]:
        return independent_sets.from_dependent_matroid((self.ground_set, self.dependent_sets))
    
    @property
    def dependent_sets(self) -> list[set[T]]:
        return self.__dependent_sets
    
    @property
    def bases(self) -> list[set[T]]:
        return bases.from_dependent_matroid((self.ground_set, self.dependent_sets))
    
    @property
    def circuits(self) -> list[set[T]]:
        return circuits.from_dependent_matroid((self.ground_set, self.dependent_sets))
    
    @property
    def rank_function(self) -> Callable[[set[T]], int]:
        return rank_function.from_dependent_matroid((self.ground_set, self.dependent_sets))
    
    @property
    def closure_function(self) -> Callable[[set[T]], set[T]]:
        return closure_function.from_dependent_matroid((self.ground_set, self.dependent_sets))
    
    @property
    def flats(self) -> list[set[T]]:
        return flats.from_dependent_matroid((self.ground_set, self.dependent_sets))
    
    @property
    def open_sets(self) -> list[set[T]]:
        return open_sets.from_dependent_matroid((self.ground_set, self.dependent_sets))
    
    @property
    def hyperplanes(self) -> list[set[T]]:
        return hyperplanes.from_dependent_matroid((self.ground_set, self.dependent_sets))
    
    @property
    def spanning_sets(self) -> list[set[T]]:
        return spanning_sets.from_dependent_matroid((self.ground_set, self.dependent_sets))