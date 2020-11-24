from functools import cached_property
from typing import Callable, TypeVar

from .Matroid import Matroid

from matroids.construct import (
    independent_sets,
    dependent_sets,
    bases,
    rank_function,
    nulity_function,
    closure_function,
    flats,
    open_sets,
    hyperplanes,
    spanning_sets,
)

from .core.checker import satisfies_circuits_axiom
from .core.exception import MatroidAxiomError
from .core.types import MatroidAxiom

T = TypeVar("T")

class CircuitsMatroid(Matroid):
    __axiom = MatroidAxiom.CIRCUITS

    def __init__(self, matroid: tuple[set[T],list[set[T]]]):
        if not satisfies_circuits_axiom(matroid):
            raise MatroidAxiomError(f"The given family doesn't satisfy {self.axiom.value}!")

        self.__ground_set = matroid[0]
        self.__circuits = matroid[1]
    
    @property
    def axiom(self) -> MatroidAxiom:
        return self.__axiom

    @property
    def ground_set(self) -> set[T]:
        return self.__ground_set
    
    @cached_property
    def independent_sets(self) -> list[set[T]]:
        return independent_sets.from_circuits_matroid((self.ground_set, self.circuits))
    
    @cached_property
    def dependent_sets(self) -> list[set[T]]:
        return dependent_sets.from_circuits_matroid((self.ground_set, self.circuits))
    
    @cached_property
    def bases(self) -> list[set[T]]:
        return bases.from_circuits_matroid((self.ground_set, self.circuits))
    
    @property
    def circuits(self) -> list[set[T]]:
        return self.__circuits
    
    @cached_property
    def rank_function(self) -> Callable[[set[T]], int]:
        return rank_function.from_circuits_matroid((self.ground_set, self.circuits))
    
    @cached_property
    def nulity_function(self) -> Callable[[set[T]], int]:
        return nulity_function.from_circuits_matroid((self.ground_set, self.circuits))
    
    @cached_property
    def closure_function(self) -> Callable[[set[T]], set[T]]:
        return closure_function.from_circuits_matroid((self.ground_set, self.circuits))
    
    @cached_property
    def flats(self) -> list[set[T]]:
        return flats.from_circuits_matroid((self.ground_set, self.circuits))
    
    @cached_property
    def open_sets(self) -> list[set[T]]:
        return open_sets.from_circuits_matroid((self.ground_set, self.circuits))
    
    @cached_property
    def hyperplanes(self) -> list[set[T]]:
        return hyperplanes.from_circuits_matroid((self.ground_set, self.circuits))
    
    @cached_property
    def spanning_sets(self) -> list[set[T]]:
        return spanning_sets.from_circuits_matroid((self.ground_set, self.circuits))