from typing import Callable, TypeVar

from matroids.construct import (
    independent_sets,
    dependent_sets,
    bases,
    circuits,
    rank_function,
    closure_function,
    flats,
    open_sets,
    spanning_sets,
)

from .core.checker import satisfies_hyperplanes_axiom
from .core.exception import MatroidAxiomError
from .Matroid import Matroid
from .core.types import MatroidAxiom

T = TypeVar("T")

class HyperplanesMatroid(Matroid):
    __axiom = MatroidAxiom.HYPERPLANES

    def __init__(self, matroid: tuple[set[T],list[set[T]]]):
        if not satisfies_hyperplanes_axiom(matroid):
            raise MatroidAxiomError(f"The given family doesn't satisfy {self.axiom.value}!")

        self.__ground_set = matroid[0]
        self.__hyperplanes = matroid[1]
    
    @property
    def axiom(self) -> MatroidAxiom:
        return self.__axiom

    @property
    def ground_set(self) -> set[T]:
        return self.__ground_set
    
    @property
    def independent_sets(self) -> list[set[T]]:
        return independent_sets.from_hyperplanes_matroid((self.ground_set, self.hyperplanes))
    
    @property
    def dependent_sets(self) -> list[set[T]]:
        return dependent_sets.from_hyperplanes_matroid((self.ground_set, self.hyperplanes))
    
    @property
    def bases(self) -> list[set[T]]:
        return bases.from_hyperplanes_matroid((self.ground_set, self.hyperplanes))
    
    @property
    def circuits(self) -> list[set[T]]:
        return circuits.from_hyperplanes_matroid((self.ground_set, self.hyperplanes))
    
    @property
    def rank_function(self) -> Callable[[set[T]], int]:
        return rank_function.from_hyperplanes_matroid((self.ground_set, self.hyperplanes))
    
    @property
    def closure_function(self) -> Callable[[set[T]], set[T]]:
        return closure_function.from_hyperplanes_matroid((self.ground_set, self.hyperplanes))
    
    @property
    def flats(self) -> list[set[T]]:
        return flats.from_hyperplanes_matroid((self.ground_set, self.hyperplanes))
    
    @property
    def open_sets(self) -> list[set[T]]:
        return open_sets.from_hyperplanes_matroid((self.ground_set, self.hyperplanes))
    
    @property
    def hyperplanes(self) -> list[set[T]]:
        return self.__hyperplanes
    
    @property
    def spanning_sets(self) -> list[set[T]]:
        return spanning_sets.from_hyperplanes_matroid((self.ground_set, self.hyperplanes))