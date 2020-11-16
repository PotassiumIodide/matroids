from typing import TypeVar

from .core.checker import satisfies_independent_axiom
from .core.exception import MatroidAxiomError
from .Matroid import Matroid
from .core.types import MatroidAxiom

T = TypeVar("T")

class IndependentMatroid(Matroid):
    __axiom = MatroidAxiom.INDEPENDENT_SETS

    def __init__(self, matroid: tuple[set[T],list[set[T]]]):
        if not satisfies_independent_axiom(matroid):
            raise MatroidAxiomError(f"The given family doesn't satisfy {self.axiom.value}!")

        self.__ground_set = matroid[0]
        self.__independent_sets = matroid[1]
    
    @property
    def axiom(self) -> MatroidAxiom:
        return self.__axiom

    @property
    def ground_set(self) -> set[T]:
        return self.__ground_set
    
    @property
    def independent_sets(self) -> list[set[T]]:
        return self.__independent_sets
    
    # Other attributes are given from independent sets by defaults.
