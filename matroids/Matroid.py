from __future__ import annotations

from abc import abstractmethod
from math import inf
from typing import Callable, TypeVar, Union

from matroids.MatroidMetaClass import MatroidMetaClass
from matroids.core.checker import satisfies_bases_axiom
from matroids.core.exception import MatroidAxiomError

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

T = TypeVar('T')

class Matroid(object, metaclass=MatroidMetaClass):
    def __init__(self, matroid: tuple[set[T],list[set[T]]]):
        """!!!!! - Caution - !!!!!
        This is implemented only for giving the default settings for dual of the matroid.
        Though this class is exactly the same as BasesMatroid class, it is not recommended to use this Matroid class directly.

        Args:
            matroid (tuple[set[T], list[set[T]]]): The pair of a ground set and bases

        Raises:
            MatroidAxiomError: If the given pair is not a matroid under the axiom of bases.
        """
        if not satisfies_bases_axiom(matroid):
            raise MatroidAxiomError(f"The given family doesn't satisfy {self.axiom.value}!")
        self.__ground_set = matroid[0]
        self.__bases = matroid[1]

    @property
    def ground_set(self):
        return self.__ground_set
    
    @property
    def E(self) -> set[T]:
        return self.ground_set
    
    @property
    def size(self) -> int:
        return len(self.ground_set)

    # ----------------------------------------------------------------------------------------- #
    # By defaults, the class Matroid forces you to give a construction of bases, and construct  #
    # other attributes from the bases.                                                          #
    # Since the algorithms can be the worst, each method should be overridden if necessary.     #
    # ----------------------------------------------------------------------------------------- #

    # ----------------------------------------------------------------------------------------- #
    #                                Axiomatic Properties                                       #
    # ----------------------------------------------------------------------------------------- #
    @property
    @abstractmethod
    def independent_sets(self):
        return independent_sets.from_bases_matroid((self.ground_set, self.bases))

    @property
    def dependent_sets(self) -> list[set[T]]:
        return dependent_sets.from_bases_matroid((self.ground_set, self.independent_sets))

    @property
    def bases(self) -> list[set[T]]:
        return self.__bases
        
    @property
    def circuits(self) -> list[set[T]]:
        return circuits.from_bases_matroid((self.ground_set, self.independent_sets))

    @property
    def rank_function(self) -> Callable[[set[T]], int]:
        return rank_function.from_bases_matroid((self.ground_set, self.independent_sets))
    
    @property
    def closure_function(self) -> Callable[[set[T]], set[T]]:
        return closure_function.from_bases_matroid((self.ground_set, self.independent_sets))

    @property
    def flats(self) -> list[set[T]]:
        return flats.from_bases_matroid((self.ground_set, self.independent_sets))
    
    @property
    def open_sets(self) -> list[set[T]]:
        return open_sets.from_bases_matroid((self.ground_set, self.independent_sets))
    
    @property
    def hyperplanes(self) -> list[set[T]]:
        return hyperplanes.from_bases_matroid((self.ground_set, self.independent_sets))
    
    @property
    def spanning_sets(self) -> list[set[T]]:
        return spanning_sets.from_bases_matroid((self.ground_set, self.independent_sets))
    
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
    
    # ----------------------------------------------------------------------------------------------- #
    #                                           Duality                                               #
    # ----------------------------------------------------------------------------------------------- #

    @property
    def dual(self) ->  Matroid:
        """Construct the dual matroid. By default, it is given as BaseMatroid.

        Returns:
            Matroid: The dual of the matroid.
        """
        # Bs* = { E - B : B ∈ Bs }
        Bs_ast = [ self.E - B for B in self.bases ]
        return Matroid((self.E, Bs_ast))

    @property
    def coindependent_sets(self) -> list[set[T]]:
        """Construct the coindependent sets; the independent sets of the dual matroid.

        Returns:
            list[set[T]]: The coindependent sets of the matroid.
        """
        return self.dual.independent_sets
    
    @property
    def codependent_sets(self) -> list[set[T]]:
        """Construct the codependent sets; the dependent sets of the dual matroid.

        Returns:
            list[set[T]]: The codependent sets of the matroid.
        """
        return self.dual.dependent_sets
    
    @property
    def cobases(self) -> list[set[T]]:
        """Construct the cobases; the bases of the dual matroid.

        Returns:
            list[set[T]]: The cobases of the matroid.
        """
        return [ self.E - B for B in self.bases ]
    
    @property
    def cocircuits(self) -> list[set[T]]:
        """Construct the cocircuits; the circuits of the dual matroid.

        Returns:
            list[set[T]]: The cocircuits of the matroid.
        """
        return self.dual.circuits
    
    @property
    def corank_function(self) -> Callable[[set[T]], int]:
        """Construct the corank function; the rank function of the dual matroid.

        Returns:
            Callable[[set[T]], int]: The corank function of the matroid.
        """
        r = self.rank_function
        E = self.ground_set
        # r*(X) = r(E - X) + |X| - r(M)
        return lambda X: r(E - X) + len(X) - r(E)
    
    @property
    def coclosure_function(self) -> Callable[[set[T]], set[T]]:
        """Construct the coclosure function; the closure function of the dual matroid.

        Returns:
            Callable[[set[T]], set[T]]: The coclosure function of the matroid.
        """
        return self.dual.closure_function
    
    @property
    def coflats(self) -> list[set[T]]:
        """Construct the coflats; the flats of the dual matroid.

        Returns:
            list[set[T]]: The coflats of the matroid.
        """
        return self.dual.flats
    
    @property
    def coopen_sets(self) -> list[set[T]]:
        """Construct the coopen sets; the open sets of the dual matroid.

        Returns:
            list[set[T]]: The coopen sets of the matroid.
        """
        return self.dual.open_sets
    
    @property
    def cohyperplanes(self) -> list[set[T]]:
        """Construct the cohyperplanes; the hyperplanes of the matroid.

        Returns:
            list[set[T]]: The cohyperplanes of the matroid.
        """
        return self.dual.hyperplanes
    
    @property
    def cospanning_sets(self) -> list[set[T]]:
        """Construct the cospanning sets; the spanning sets of the matroid.

        Returns:
            list[set[T]]: The cospanning sets of the matroid.
        """
        return self.dual.spanning_sets
    
    def corank(self, subset: Union[set[T], None]=None) -> int:
        """Calculate the corank, the rank in the dual matroid, of a given subset. If no subset is given, returns the corank of the matroid.

        Args:
            subset (Union[set[T], None], optional): A subset of the ground set of the matroid. Defaults to self.ground_set.

        Returns:
            int: The corank of a given subset in the matroid.
        """
        X = subset if subset is not None else self.ground_set
        # r*(X) = r(E - X) + |X| - r(M)
        return self.rank(self.ground_set - X) + len(X) - self.rank()

    # ----------------------------------------------------------------------------------------------- #
    #                                      Other Properties                                           #
    # ----------------------------------------------------------------------------------------------- #

    @property
    def is_free(self) -> bool:
        """Check whether the matroid is free, that is, it has no dependent set.

        Returns:
            bool: True when the matroid is free, False otherwise
        """
        return not self.dependent_sets
    
    @property
    def is_empty(self) -> bool:
        """Check whether the matroid is empty, that is, it has no element in ground set.

        Returns:
            bool: True when the matroid is emtpy, False otherwise
        """
        return not self.ground_set