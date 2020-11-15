import math
from typing import Callable, Generic, TypeVar, Union

from matroids.construct import (
    independent_sets,
    dependent_sets,
    bases,
    circuits,
    rank_function,
    closure_function,
    flats,
    open_sets,
    hyperplanes,
    spanning_sets,
)
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
            return independent_sets.from_dependent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return independent_sets.from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return independent_sets.from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return independent_sets.from_rank_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return independent_sets.from_closure_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.FLATS:
            return independent_sets.from_flats_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.OPEN_SETS:
            return independent_sets.from_open_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.HYPERPLANES:
            return independent_sets.from_hyperplanes_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.SPANNING_SETS:
            return independent_sets.from_spanning_matroid((self.__first, self.__second))
        
        raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")
    
    @property
    def dependent_sets(self) -> list[set[T]]:
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return dependent_sets.from_independent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return dependent_sets.from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return dependent_sets.from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return dependent_sets.from_rank_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return dependent_sets.fromclosure_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.FLATS:
            return dependent_sets.fromflats_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.OPEN_SETS:
            return dependent_sets.fromopen_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.HYPERPLANES:
            return dependent_sets.fromhyperplanes_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.SPANNING_SETS:
            return dependent_sets.fromspanning_matroid((self.__first, self.__second))

        raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")
    
    @property
    def bases(self) -> list[set[T]]:
        if self.__base_axiom is MatroidAxiom.BASES:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return bases.from_independent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return bases.from_dependent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return bases.from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return bases.from_rank_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return bases.from_closure_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.FLATS:
            return bases.from_flats_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.OPEN_SETS:
            return bases.from_open_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.HYPERPLANES:
            return bases.from_hyperplanes_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.SPANNING_SETS:
            return bases.from_spanning_matroid((self.__first, self.__second))

        raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")
    
    @property
    def circuits(self) -> list[set[T]]:
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return circuits.from_independent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return circuits.from_dependent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return circuits.from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return circuits.from_rank_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return circuits.from_closure_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.FLATS:
            return circuits.from_flats_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.OPEN_SETS:
            return circuits.from_open_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.HYPERPLANES:
            return circuits.from_hyperplanes_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.SPANNING_SETS:
            return circuits.from_spanning_matroid((self.__first, self.__second))
        
        raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")

    @property
    def rank_function(self) -> Callable[[set[T]], int]:
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return rank_function.from_independent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return rank_function.from_dependent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return rank_function.from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return rank_function.from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return rank_function.from_closure_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.FLATS:
            return rank_function.from_flats_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.OPEN_SETS:
            return rank_function.from_open_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.HYPERPLANES:
            return rank_function.from_hyperplanes_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.SPANNING_SETS:
            return rank_function.from_spanning_matroid((self.__first, self.__second))
        
        raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")
    

    @property
    def closure_function(self) -> Callable[[set[T]], set[T]]:
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return closure_function.from_independent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return closure_function.from_dependent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return closure_function.from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return closure_function.from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return closure_function.from_rank_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.FLATS:
            return closure_function.from_flats_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.OPEN_SETS:
            return closure_function.from_open_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.HYPERPLANES:
            return closure_function.from_hyperplanes_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.SPANNING_SETS:
            return closure_function.from_spanning_matroid((self.__first, self.__second))
        
        raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")
    
    @property
    def flats(self) -> list[set[T]]:
        if self.__base_axiom is MatroidAxiom.FLATS:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return flats.from_independent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return flats.from_dependent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return flats.from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return flats.from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return flats.from_rank_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return flats.from_closure_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.OPEN_SETS:
            return flats.from_open_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.HYPERPLANES:
            return flats.from_hyperplanes_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.SPANNING_SETS:
            return flats.from_spanning_matroid((self.__first, self.__second))
        
        raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")

    @property
    def open_sets(self) -> list[set[T]]:
        if self.__base_axiom is MatroidAxiom.OPEN_SETS:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return open_sets.from_independent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return open_sets.from_dependent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return open_sets.from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return open_sets.from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return open_sets.from_rank_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return open_sets.from_closure_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.FLATS:
            return open_sets.from_flats_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.HYPERPLANES:
            return open_sets.from_hyperplanes_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.SPANNING_SETS:
            return open_sets.from_spanning_matroid((self.__first, self.__second))
        
        raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")
    
    @property
    def hyperplanes(self) -> list[set[T]]:
        if self.__base_axiom is MatroidAxiom.HYPERPLANES:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return hyperplanes.from_independent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return hyperplanes.from_dependent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return hyperplanes.from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return hyperplanes.from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return hyperplanes.from_rank_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return hyperplanes.from_closure_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.FLATS:
            return hyperplanes.from_flats_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.OPEN_SETS:
            return hyperplanes.from_open_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.SPANNING_SETS:
            return hyperplanes.from_spanning_matroid((self.__first, self.__second))
        
        raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")
    
    @property
    def spanning_sets(self) -> list[set[T]]:
        if self.__base_axiom is MatroidAxiom.SPANNING_SETS:
            return self.__second
        if self.__base_axiom is MatroidAxiom.INDEPENDENT_SETS:
            return spanning_sets.from_independent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.DEPENDENT_SETS:
            return spanning_sets.from_dependent_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.BASES:
            return spanning_sets.from_bases_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CIRCUITS:
            return spanning_sets.from_circuits_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.RANK_FUNCTION:
            return spanning_sets.from_rank_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return spanning_sets.from_closure_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.FLATS:
            return spanning_sets.from_flats_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.OPEN_SETS:
            return spanning_sets.from_open_matroid((self.__first, self.__second))
        if self.__base_axiom is MatroidAxiom.HYPERPLANES:
            return spanning_sets.from_hyperplanes_matroid((self.__first, self.__second))
        
        raise NotImplementedError(f"Implementation for {self.__base_axiom} has not defined yet!")


    def rank(self, subset: Union[set[T], None]=None) -> int:
        """Calcurate the rank of a given subset. If no subset is given, returns the rank of the matroid.

        Args:
            subset (Union[set[T], None], optional): A subset of the ground set of the matroid. Defaults to self.ground_set.

        Returns:
            int: The rank of a given subset in the matroid.
        """
        X = subset if subset is not None else self.ground_set
        r = self.rank_function
        return r(X)
    
    def girth(self, subset: set[T]) -> Union[int, float]:
        """Calcurate the girth of a given subset.

        Args:
            subset (set[T]): A subset of the ground set of the matroid.

        Returns:
            int: The girth (the minimum cardinality of circuits) of a given subset in the matroid.
        """
        g = min(map(len, self.circuits))
        return g if g else math.inf