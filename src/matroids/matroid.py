from typing import Callable, Generic, TypeVar, Union

import matroids.construct as construct
from .types import MatroidAxiom
from .validator import validate_matroid_axiom

T = TypeVar('T', int, str)

class Matroid(Generic[T]):
    @validate_matroid_axiom
    def __init__(self,
                 pair: Union[tuple[set[T], list[T]], tuple[set[T], Callable[[set[T]], int]], tuple[set[T], Callable[[set[T]], set[T]]]],
                 axiom: MatroidAxiom):
        self.__first     : set[T] = pair[0]
        self.__second    : Union[list[T], Callable[[set[T]], int], Callable[[set[T]], set[T]]] = pair[1]
        self.__base_axiom: MatroidAxiom = axiom

    @property
    def ground_set(self) -> set[T]:
        return self.__first

    @property
    def independent_sets(self) -> list[set[T]]:
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return self.__second
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return construct.indeps_from_deps_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return construct.indeps_from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return construct.indeps_from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return construct.indeps_from_rank_matroid((self.__first, self.__second))
        # TODO: Implement the other constructions from other axioms
        else:
            raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")
    
    @property
    def dependent_sets(self) -> list[set[T]]:
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return construct.deps_from_indeps_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return construct.deps_from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return construct.deps_from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return construct.deps_from_rank_matroid((self.__first, self.__second))
        # TODO: Implement the other constructions from other axioms
        else:
            raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")
    
    @property
    def bases(self) -> list[set[T]]:
        if self.__base_axiom is MatroidAxiom.BASES:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return construct.bases_from_indeps_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return construct.bases_from_deps_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return construct.bases_from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return construct.bases_from_rank_matroid((self.__first, self.__second))

        # TODO: Implement the other constructions from other axioms
        else:
            raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")
    
    @property
    def circuits(self) -> list[set[T]]:
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return construct.circuits_from_indeps_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return construct.circuits_from_deps_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return construct.circuits_from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return construct.circuits_from_rank_matroid((self.__first, self.__second))
        
        # TODO: Implement the other constructions from other axioms
        else:
            raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")

    @property
    def rank_function(self) -> Callable[[set[T]], int]:
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return construct.rank_function_from_indeps_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return construct.rank_function_from_deps_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return construct.rank_function_from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return construct.rank_function_from_circuits_matroid((self.__first, self.__second))
        
        # TODO: Implement the other constructions from other axioms
        else:
            raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")

    @property
    def closure_function(self) -> Callable[[set[T]], set[T]]:
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return construct.closure_function_from_indeps_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return construct.closure_function_from_deps_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return construct.closure_function_from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return construct.closure_function_from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return construct.closure_function_from_rank_matroid((self.__first, self.__second))
        
        # TODO: Implement the other constructions from other axioms
        else:
            raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")