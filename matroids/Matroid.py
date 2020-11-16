from abc import abstractmethod
from math import inf
from typing import Callable, TypeVar, Union

from .MatroidMetaClass import MatroidMetaClass

from matroids.construct import (
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

T = TypeVar('T')

class Matroid(object, metaclass=MatroidMetaClass):

    @property
    @abstractmethod
    def axiom(self):
        pass

    @property
    @abstractmethod
    def ground_set(self):
        pass

    # ----------------------------------------------------------------------------------------- #
    # By defaults, the class Matroid forces you to give a construction of independent sets Is,  #
    # and construct other attributes from Is.                                                   #
    # Since the algorithms can be the worst, each method should be overridden if necessary.     #
    # ----------------------------------------------------------------------------------------- #

    @property
    @abstractmethod
    def independent_sets(self):
        pass

    @property
    def dependent_sets(self) -> list[set[T]]:
        return dependent_sets.from_independent_matroid((self.ground_set, self.independent_sets))

    @property
    def bases(self) -> list[set[T]]:
        return bases.from_independent_matroid((self.ground_set, self.independent_sets))
    
    @property
    def circuits(self) -> list[set[T]]:
        return circuits.from_independent_matroid((self.ground_set, self.independent_sets))

    @property
    def rank_function(self) -> Callable[[set[T]], int]:
        return rank_function.from_independent_matroid((self.ground_set, self.independent_sets))
    
    @property
    def closure_function(self) -> Callable[[set[T]], set[T]]:
        return closure_function.from_independent_matroid((self.ground_set, self.independent_sets))

    @property
    def flats(self) -> list[set[T]]:
        return flats.from_independent_matroid((self.ground_set, self.independent_sets))
    
    @property
    def open_sets(self) -> list[set[T]]:
        return open_sets.from_independent_matroid((self.ground_set, self.independent_sets))
    
    @property
    def hyperplanes(self) -> list[set[T]]:
        return hyperplanes.from_independent_matroid((self.ground_set, self.independent_sets))
    
    @property
    def spanning_sets(self) -> list[set[T]]:
        return spanning_sets.from_independent_matroid((self.ground_set, self.independent_sets))
    
    def rank(self, subset: Union[set[T], None]=None) -> int:
        """Calculate the rank of a given subset. If no subset is given, returns the rank of the matroid.

        Args:
            subset (Union[set[T], None], optional): A subset of the ground set of the matroid. Defaults to self.ground_set.

        Returns:
            int: The rank of a given subset in the matroid.
        """
        X = subset if subset is not None else self.ground_set
        r = self.rank_function
        return r(X)
