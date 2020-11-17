from typing import TypeVar

from .Matroid import Matroid

from .core.checker import satisfies_bases_axiom
from .core.exception import MatroidAxiomError
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
    def bases(self) -> list[set[T]]:
        return self.__bases
    
    # The rest part will be given by default implementation.