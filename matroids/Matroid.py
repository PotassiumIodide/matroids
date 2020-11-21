from __future__ import annotations

from abc import abstractmethod
from itertools import combinations
from math import inf
from typing import Callable, TypeVar, Union

from matroids.MatroidMetaClass import MatroidMetaClass
from matroids.core.checker import satisfies_bases_axiom
from matroids.core.exception import MatroidAxiomError
from matroids.core.set_operator import powset

from matroids.construct import (
    independent_sets,
    dependent_sets,
    bases,
    circuits,
    rank_function,
    nulity_function,
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
            raise MatroidAxiomError(f"The given family doesn't satisfy the axiom of bases!")
        self.__ground_set = matroid[0]
        self.__bases = matroid[1]
    
    def __or__(self, X: set[T]) -> Matroid:
        """Restrict the matroid to X.
        For faster calculation and saving memory, the circuits are used in this operation.

        Args:
            X (set[T]): A subset of the ground set of the matroid.
        
        Raises:
            ValueError: if the given set X is not included in the ground set.

        Returns:
            Matroid: The restriction of the matroid to X
        """
        E = self.ground_set
        if not X <= E:
            raise ValueError("The set for the restriction must be a subset of the ground set!")
        # Cs|X = { C ⊆ X : C ∈ Cs }
        CsX = [C for C in self.circuits if C <= X]
        return Matroid((X, bases.from_circuits_matroid((X, CsX))))
    
    def __sub__(self, X: set[T]) -> Matroid:
        """Delete a given set X from the matroid.
        For faster calculation and saving memory, the circuits are used in this operation.

        Args:
            X (set[T]): A subset of the ground set of the matroid.

        Raises:
            ValueError: if the given set X is not included in the ground set.

        Returns:
            Matroid: The deletion of X from the matroid
        """
        return self | (self.ground_set - X)

    @property
    def ground_set(self) -> set[T]:
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
    def independent_sets(self) -> list[set[T]]:
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
    def nulity_function(self) -> Callable[[set[T]], int]:
        return nulity_function.from_bases_matroid((self.ground_set, self.independent_sets))
    
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
    
    def fundamental_circuit(self, e: T, B: set[T]) -> set[T]:
        """Find the fundamental circuit C(e, B) of e with respect to B.
        Let B be a basis of a matroid M. If e ∈ E - B, then B ∪ {e} contains a unique circuit, C(e,B).
        Moreover, e ∈ C(e, B).

        Args:
            e (T): An element in E - B
            B (set[T]): A basis in the matroid.

        Raises:
            ValueError: if the given e is not in E - B. 
            ValueError: if the given B is not a basis.

        Returns:
            set[T]: The fundamental circuit of e with respect to B.
        """
        if e not in (self.E - B):
            raise ValueError("The element e needs to be in E - B!!")
        if B not in self.bases:
            raise ValueError("The set B needs to be a basis!!")
        C_ = [C for C in self.circuits if C <= B | {e} ]
        return C_[0]
    
    def fundamental_circuits_with_respect_to(self, B: set[T]) -> list[set[T]]:
        """Find the fundamental circuits with respect to B.
        They consist of the fundamental circuits of every element e in E - B with respect to B.

        Args:
            B (set[T]): A basis in the matroid.

        Raises:
            ValueError: if the given B is not a basis.

        Returns:
            list[set[T]]: The fundamental circuits with respect to B.
        """
        Cs_ = [self.fundamental_circuit(e, B) for e in (self.ground_set - B)]
        return [C for C in self.circuits if C in Cs_]
    
    def is_loop(self, e: T) -> bool:
        """Check whether a given element e is a loop or not.

        Args:
            e (T): An element in the ground set of the matroid.

        Returns:
            bool: True if a given element e is a loop, False otherwise.
        """
        return {e} in self.circuits
    
    def are_parallel(self, f: T, g: T) -> bool:
        """Check whether given elements f and g are parallel or not.

        Args:
            f (T): An element in the ground set of the matroid.
            g (T): An element in the ground set of the matroid.

        Returns:
            bool: True if given elements f and g are parallel, False otherwise.
        """
        return {f, g} in self.circuits
    
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
    
    def fundamental_cocircuit(self, e: T, B: set[T]) -> set[T]:
        """Find the fundamental cocircuit C(e, B) of e with respect to B.
        Let B be a basis of the matroid. If e ∈ B, denote C_{M*}(e, E - B) by C*(e,B).
        C*(e, B) is called the fundamental cocircuit of e with respect to B.

        Args:
            e (T): An element in B.
            B (set[T]): A basis in the matroid.

        Raises:
            ValueError: if the given e is not in B. 
            ValueError: if the given B is not a basis.

        Returns:
            set[T]: The fundamental circuit of e with respect to B.
        """
        if e not in B:
            raise ValueError("The element e needs to be in B!!")
        if B not in self.bases:
            raise ValueError("The set B needs to be a basis!!")
        return self.dual.fundamental_circuit(e, self.ground_set - B)
    
    def fundamental_cocircuits_with_respect_to(self, B: set[T]) -> list[set[T]]:
        """Find the fundamental cocircuits with respect to B.
        They consist of the fundamental cocircuits of every element e in B with respect to B.

        Args:
            B (set[T]): A basis in the matroid.

        Raises:
            ValueError: if the given B is not a basis.

        Returns:
            list[set[T]]: The fundamental circuits with respect to B.
        """
        Cs_ = [self.fundamental_cocircuit(e, B) for e in B]
        return [C for C in self.cocircuits if C in Cs_]
    
    def is_coloop(self, e: T) -> bool:
        """Check whether a given element e is a coloop or not.

        Args:
            e (T): An element in the ground set of the matroid.

        Returns:
            bool: True if a given element e is a coloop, False otherwise.
        """
        return {e} in self.cocircuits
    
    def are_coparallel(self, f: T, g: T) -> bool:
        """Check whether given elements f and g are coparallel or not.

        Args:
            f (T): An element in the ground set of the matroid.
            g (T): An element in the ground set of the matroid.

        Returns:
            bool: True if given elements f and g are coparallel, False otherwise.
        """
        return {f, g} in self.cocircuits

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
    
    # ----------------------------------------------------------------------------------------------- #
    #                                          Utilities                                              #
    # ----------------------------------------------------------------------------------------------- #

    def encode(self, basis_symbol: str='*', non_basis_symbol='0', show_with_order: bool=False) -> str:
        """To encode matroids, we use RevLex-Index, which is used in Homepage of 
        Oriented Matroids by Lukas Finschi and Komei Fukuda.
        For a given rank r and a given size n of the ground set of a matroid,
        the RevLex-Index uniquely identifies isomorphism classes of matroids.
        The index is based on the representation of matroids by the sets of bases.
        The set of bases can be specified by describing whether each r-subset of the ground set is a basis or not.
        '*' means a basis and '0' (you can change these symbols by option). Each r-subset is ordered in reverse lexicographic orer.

        Args:
            basis_symbol (str, optional): A symbol for a bases. Defaults to '*'.
            non_basis_symbol (str, optional): A symbol for non-bases. Defaults to '0'.
            show_with_order (bool, optional): Show the order of enumerated r-subsets if this is True.

        Returns:
            str: Encoded matroid with respect to bases.
        """
        encoded = "".join(basis_symbol if set(X) in self.bases else non_basis_symbol for X in combinations(self.ground_set, self.rank()))
        if not show_with_order:
            return encoded
        
        return "\n".join(
            "".join(str(X[i]) for X in combinations(self.ground_set, self.rank()))
                      for i in range(self.rank())
            ) + f"\n{encoded}"
        
    @staticmethod
    def decode(encoded_matroid: str, size: int, rank: int, basis_symbol:str='*', non_basis_symbol:str='0') -> Matroid:
        """Decode an encoded matroid.

        Args:
            encoded_matroid (str): An encoded matroid.
            size (int): The size of a given matroid.
            rank (int): The rank of a given matroid.
            basis_symbol (str, optional): The symbol for bases. Defaults to '*'.
            non_basis_symbol (str, optional): The symbol for non-bases. Defaults to '0'.

        Returns:
            Matroid: The decoded matroid.
        """
        if len([*combinations(range(size), rank)]) != len(encoded_matroid):
            raise ValueError(f"The number of {rank}-subsets of E doesn't match that of the given encoded matroid!!")
        if any(symbol not in (basis_symbol, non_basis_symbol) for symbol in encoded_matroid):
            raise ValueError(f"A given matroid isn't encoded properly.")
        E = {*range(1,size+1)}
        Bs = [ set(X) for X, symbol in zip(combinations(E, rank), encoded_matroid) if symbol == basis_symbol ]
        return Matroid((E, Bs))
