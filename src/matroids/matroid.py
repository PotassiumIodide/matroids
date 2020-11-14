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
            return construct.independent_sets_from_dependent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return construct.independent_sets_from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return construct.independent_sets_from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return construct.independent_sets_from_rank_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return construct.independent_sets_from_closure_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.FLATS:
            return construct.independent_sets_from_flats_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.OPEN_SETS:
            return construct.independent_sets_from_open_sets_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.HYPERPLANES:
            return construct.independent_sets_from_hyperplanes_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.SPANNING_SETS:
            return construct.independent_sets_from_spanning_sets_matroid((self.__first, self.__second))
        
        raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")
    
    @property
    def dependent_sets(self) -> list[set[T]]:
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return construct.dependent_sets_from_independent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return construct.dependent_sets_from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return construct.dependent_sets_from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return construct.dependent_sets_from_rank_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return construct.dependent_sets_from_closure_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.FLATS:
            return construct.dependent_sets_from_flats_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.OPEN_SETS:
            return construct.dependent_sets_from_open_sets_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.HYPERPLANES:
            return construct.dependent_sets_from_hyperplanes_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.SPANNING_SETS:
            return construct.dependent_sets_from_spanning_sets_matroid((self.__first, self.__second))

        raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")
    
    @property
    def bases(self) -> list[set[T]]:
        if self.__base_axiom is MatroidAxiom.BASES:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return construct.bases_from_independent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return construct.bases_from_dependent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return construct.bases_from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return construct.bases_from_rank_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return construct.bases_from_closure_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.FLATS:
            return construct.bases_from_flats_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.OPEN_SETS:
            return construct.bases_from_open_sets_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.HYPERPLANES:
            return construct.bases_from_hyperplanes_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.SPANNING_SETS:
            return construct.bases_from_spanning_sets_matroid((self.__first, self.__second))

        raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")
    
    @property
    def circuits(self) -> list[set[T]]:
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return construct.circuits_from_independent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return construct.circuits_from_dependent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return construct.circuits_from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return construct.circuits_from_rank_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return construct.circuits_from_closure_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.FLATS:
            return construct.circuits_from_flats_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.OPEN_SETS:
            return construct.circuits_from_open_sets_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.HYPERPLANES:
            return construct.circuits_from_hyperplanes_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.SPANNING_SETS:
            return construct.circuits_from_spanning_sets_matroid((self.__first, self.__second))
        
        raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")

    @property
    def rank_function(self) -> Callable[[set[T]], int]:
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return construct.rank_function_from_independent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return construct.rank_function_from_dependent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return construct.rank_function_from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return construct.rank_function_from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return construct.rank_function_from_closure_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.FLATS:
            return construct.rank_function_from_flats_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.OPEN_SETS:
            return construct.rank_function_from_open_sets_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.HYPERPLANES:
            return construct.rank_function_from_hyperplanes_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.SPANNING_SETS:
            return construct.rank_function_from_spanning_sets_matroid((self.__first, self.__second))
        
        raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")
    

    @property
    def closure_function(self) -> Callable[[set[T]], set[T]]:
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return construct.closure_function_from_independent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return construct.closure_function_from_dependent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return construct.closure_function_from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return construct.closure_function_from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return construct.closure_function_from_rank_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.FLATS:
            return construct.closure_function_from_flats_matroid((self.__first, self.__second))
        
        # TODO: Implement the other constructions from other axioms
        else:
            raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")
    
    @property
    def flats(self) -> list[set[T]]:
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return construct.flats_from_rank_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return construct.flats_from_closure_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.OPEN_SETS:
            return construct.flats_from_open_sets_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.HYPERPLANES:
            return construct.flats_from_hyperplanes_matroid((self.__first, self.__second))
        
        # TODO: Implement the other constructions from other axioms
        else:
            raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")
    
    @property
    def hyperplanes(self) -> list[set[T]]:
        if self.__base_axiom is MatroidAxiom.BASES:
            return construct.hyperplanes_from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.FLATS:
            return construct.hyperplanes_from_flats_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.SPANNING_SETS:
            return construct.hyperplanes_from_spanning_sets_matroid((self.__first, self.__second))
        
        # TODO: Implement the other constructions from other axioms
        else:
            raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")
    
    @property
    def spanning_sets(self) -> list[set[T]]:
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return construct.spanning_sets_from_rank_matroid((self.__first, self.__second))
        
        # TODO: Implement the other constructions from other axioms
        else:
            raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")


    def rank(self, subset: Union[set[T], None]=None) -> int:
        """Calcurate the rank of a given subset. If no subset is given, returns the rank of the matroid.

        Args:
            subset (Union[set[T], None], optional): A subset of the ground set of the matroid. Defaults to the ground set.

        Returns:
            int: The rank of a given subset in the matroid.
        """
        X = subset if subset is not None else self.ground_set
        r = self.rank_function
        return r(X)