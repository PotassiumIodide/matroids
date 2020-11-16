from typing import Callable, TypeVar

from matroids.construct import (
    independent_sets,
    dependent_sets,
    circuits,
    rank_function,
    closure_function,
    flats,
    open_sets,
    hyperplanes,
    spanning_sets,
)

from .core.checker import satisfies_bases_axiom
from .core.exception import MatroidAxiomError
from .Matroid import Matroid
from .core.types import MatroidAxiom

T = TypeVar("T")

class BasesMatroid(Matroid):
    __axiom = MatroidAxiom.BASES

    def __init__(self, matroid: tuple[set[T],list[set[T]]]):
        if not satisfies_bases_axiom(matroid):
            raise MatroidAxiomError(f"The given family doesn't satisfy {self.axiom.value}!")

        self.__ground_set = matroid[0]
        self.__bases = matroid[1]
    
    @property
    def axiom(self) -> MatroidAxiom:
        return self.__axiom

    @property
    def ground_set(self) -> set[T]:
        return self.__ground_set
    
    @property
    def independent_sets(self) -> list[set[T]]:
        return independent_sets.from_bases_matroid((self.ground_set, self.bases))
    
    @property
    def dependent_sets(self) -> list[set[T]]:
        return dependent_sets.from_bases_matroid((self.ground_set, self.bases))
    
    @property
    def bases(self) -> list[set[T]]:
        return self.__bases
    
    @property
    def circuits(self) -> list[set[T]]:
        return circuits.from_bases_matroid((self.ground_set, self.bases))
    
    @property
    def rank_function(self) -> Callable[[set[T]], int]:
        return rank_function.from_bases_matroid((self.ground_set, self.bases))
    
    @property
    def closure_function(self) -> Callable[[set[T]], set[T]]:
        return closure_function.from_bases_matroid((self.ground_set, self.bases))
    
    @property
    def flats(self) -> list[set[T]]:
        return flats.from_bases_matroid((self.ground_set, self.bases))
    
    @property
    def open_sets(self) -> list[set[T]]:
        return open_sets.from_bases_matroid((self.ground_set, self.bases))
    
    @property
    def hyperplanes(self) -> list[set[T]]:
        return hyperplanes.from_bases_matroid((self.ground_set, self.bases))
    
    @property
    def spanning_sets(self) -> list[set[T]]:
        return spanning_sets.from_bases_matroid((self.ground_set, self.bases))