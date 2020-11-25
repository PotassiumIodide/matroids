from __future__ import annotations

from itertools import combinations, permutations
from functools import cached_property, reduce
from operator import or_
from typing import Any, Callable, TypeVar, Union

from matroids.MatroidMetaClass import MatroidMetaClass
from matroids.core.exception import MatroidAxiomError
from matroids.core.set_operator import powset
from matroids.core.types import MatroidAxiom

from matroids.core.checker import (
    satisfies_independent_axiom,
    satisfies_dependent_axiom,
    satisfies_bases_axiom,
    satisfies_circuits_axiom,
    satisfies_rank_function_axiom,
    satisfies_nulity_function_axiom,
    satisfies_closure_axiom,
    satisfies_flats_axiom,
    satisfies_open_sets_axiom,
    satisfies_hyperplanes_axiom,
    satisfies_spanning_sets_axiom,
)
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
    __axiom = MatroidAxiom.BASES
    def __init__(self, matroid: tuple[set[T],list[set[T]]], axiom: MatroidAxiom=MatroidAxiom.BASES, axiom_check: bool=True):
        """!!!!! - Caution - !!!!!
        It is not recommended to use this Matroid class directly.

        Args:
            matroid (tuple[set[T], list[set[T]]]): The pair of a ground set and bases
            axiom (MatroidAxiom): A matroid axiom for constructing a matroid.
            axiom_check (bool, optional): If this is False, the check of axom will be skipped, and so recommended to be True.
                                          Defaults to True.

        Raises:
            MatroidAxiomError: If the given pair is not a matroid.
        """
        if axiom_check:
            if not any([
                axiom is MatroidAxiom.INDEPENDENT_SETS and satisfies_independent_axiom(matroid),
                axiom is MatroidAxiom.DEPENDENT_SETS and satisfies_dependent_axiom(matroid),
                axiom is MatroidAxiom.BASES and satisfies_bases_axiom(matroid),
                axiom is MatroidAxiom.CIRCUITS and satisfies_circuits_axiom(matroid),
                axiom is MatroidAxiom.RANK_FUNCTION and satisfies_rank_function_axiom(matroid),
                axiom is MatroidAxiom.NULITY_FUNCTION and satisfies_nulity_function_axiom(matroid),
                axiom is MatroidAxiom.CLOSURE_FUNCTION and satisfies_closure_axiom(matroid),
                axiom is MatroidAxiom.FLATS and satisfies_flats_axiom(matroid),
                axiom is MatroidAxiom.OPEN_SETS and satisfies_open_sets_axiom(matroid),
                axiom is MatroidAxiom.HYPERPLANES and satisfies_hyperplanes_axiom(matroid),
                axiom is MatroidAxiom.SPANNING_SETS and satisfies_spanning_sets_axiom(matroid),
            ]):
                raise MatroidAxiomError(f"The given family doesn't satisfy {axiom.name}!")
        self.__first = matroid[0]
        self.__second = matroid[1]
        self.__axiom = axiom
    
    def __repr__(self) -> str:
        """Return a string representation of the matroid.

        Returns:
            str: A string representation of the matroid.
        """
        return f"Matroid of rank {self.rank()} on {self.size} elements"
    
    def __eq__(self, matroid: Matroid) -> bool:
        """Check whether the matroid and a given one are equal.

        Args:
            matroid (Matroid): A matroid

        Returns:
            bool: True if the two matroids are equal, False otherwise.
        """
        return self.is_equal_to(matroid)
    
    def __add__(self, matroid: Matroid) -> Matroid:
        """Calculate the direct sum or 1-sum of this and another matroids whose ground sets are disjoint.
        It can be calculate by the operation `+`.

        Args:
            matroid (Matroid): A matroid.
        
        Raises:
            ValueError: When the ground sets are not disjoint.

        Returns:
            Matroid: The direct sum of this and the other matroids.
        """
        return self.direct_sum(matroid)
    
    def __sub__(self, X: Union[set[T], T]) -> Matroid:
        """Delete a given set X from the matroid.
        For faster calculation and saving memory, the circuits are used in this operation.

        Args:
            X (Union[set[T], T]): A subset or an element of the ground set of the matroid.

        Raises:
            ValueError: if the given set X is not included in the ground set.

        Returns:
            Matroid: The deletion of X from the matroid
        """
        return self.delete(X)
    
    def __mul__(self, matroid: Matroid) -> Matroid:
        """Calculate the free product of this and another matroids whose ground sets are disjoint.

        Args:
            matroid (Matroid): A matroid.

        Raises:
            ValueError: When the ground sets are not disjoint.

        Returns:
            Matroid: The free product of this and the other matroids.
        """
        return self.free_product(matroid)

    def __truediv__(self, X: Union[set[T], T]) -> Matroid:
        """Contract a given set X from the matroid.
        For faster calculation and saving memory, the circuits are used in this operation.

        Args:
            X (Union[set[T], T]): A subset or an element of the ground set of the matroid.

        Raises:
            ValueError: if the given set X is not included in the ground set.

        Returns:
            Matroid: The contraction of X from the matroid
        """
        return self.contract(X)

    def __or__(self, X: Union[set[T], T, Matroid]) -> Matroid:
        """If the given X is a set or index, restrict the matroid to X.
        If the given X is a matroid, return the union of this matroid and X.

        Args:
            X (Union[set[T], T, Matroid]): A subset or an element of the ground set of the matroid, or a matroid.
        
        Raises:
            ValueError: if the given set X is not included in the ground set.

        Returns:
            Matroid: The restriction of the matroid to X or the union of this matroid and X.
        """
        if isinstance(X, Matroid):
            return self.union(X)
        return self.restrict_to(X)
    
    def __len__(self) -> int:
        """Return the size of the ground set.

        Returns:
            int: the size of the ground set.
        """
        return self.size

    @property
    def ground_set(self) -> set[T]:
        return self.__first
    
    @property
    def E(self) -> set[T]:
        return self.ground_set
    
    @property
    def size(self) -> int:
        return len(self.ground_set)
    
    @property
    def axiom(self) -> MatroidAxiom:
        return self.__axiom

    # ----------------------------------------------------------------------------------------- #
    #                                Axiomatic Properties                                       #
    # ----------------------------------------------------------------------------------------- #
    @cached_property
    def independent_sets(self) -> list[set[T]]:
        if self.axiom is MatroidAxiom.INDEPENDENT_SETS:
            return self.__second
        return independent_sets.from_bases_matroid((self.ground_set, self.bases))

    @cached_property
    def dependent_sets(self) -> list[set[T]]:
        if self.axiom is MatroidAxiom.DEPENDENT_SETS:
            return self.__second
        return dependent_sets.from_bases_matroid((self.ground_set, self.independent_sets))

    @cached_property
    def bases(self) -> list[set[T]]:
        if self.axiom is MatroidAxiom.BASES:
            return self.__second
        if self.axiom is MatroidAxiom.INDEPENDENT_SETS:
            return bases.from_independent_matroid((self.__first, self.__second))
        if self.axiom is MatroidAxiom.DEPENDENT_SETS:
            return bases.from_dependent_matroid((self.__first, self.__second))
        if self.axiom is MatroidAxiom.CIRCUITS:
            return bases.from_circuits_matroid((self.__first, self.__second))
        if self.axiom is MatroidAxiom.RANK_FUNCTION:
            return bases.from_rank_matroid((self.__first, self.__second))
        if self.axiom is MatroidAxiom.NULITY_FUNCTION:
            return bases.from_nulity_matroid((self.__first, self.__second))
        if self.axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return bases.from_closure_matroid((self.__first, self.__second))
        if self.axiom is MatroidAxiom.FLATS:
            return bases.from_flats_matroid((self.__first, self.__second))
        if self.axiom is MatroidAxiom.OPEN_SETS:
            return bases.from_open_matroid((self.__first, self.__second))
        if self.axiom is MatroidAxiom.HYPERPLANES:
            return bases.from_hyperplanes_matroid((self.__first, self.__second))
        if self.axiom is MatroidAxiom.SPANNING_SETS:
            return bases.from_spanning_matroid((self.__first, self.__second))
        
    @cached_property
    def circuits(self) -> list[set[T]]:
        if self.axiom is MatroidAxiom.CIRCUITS:
            return self.__second
        return circuits.from_bases_matroid((self.ground_set, self.independent_sets))

    @cached_property
    def rank_function(self) -> Callable[[set[T]], int]:
        if self.axiom is MatroidAxiom.RANK_FUNCTION:
            return self.__second
        return rank_function.from_bases_matroid((self.ground_set, self.independent_sets))
    
    @cached_property
    def nulity_function(self) -> Callable[[set[T]], int]:
        if self.axiom is MatroidAxiom.NULITY_FUNCTION:
            return self.__second
        return nulity_function.from_bases_matroid((self.ground_set, self.independent_sets))
    
    @cached_property
    def closure_function(self) -> Callable[[set[T]], set[T]]:
        if self.axiom is MatroidAxiom.CLOSURE_FUNCTION:
            return self.__second
        return closure_function.from_bases_matroid((self.ground_set, self.independent_sets))

    @cached_property
    def flats(self) -> list[set[T]]:
        if self.axiom is MatroidAxiom.FLATS:
            return self.__second
        return flats.from_bases_matroid((self.ground_set, self.independent_sets))
    
    @property
    def closed_sets(self) -> list[set[T]]:
        return self.flats
    
    @cached_property
    def open_sets(self) -> list[set[T]]:
        if self.axiom is MatroidAxiom.OPEN_SETS:
            return self.__second
        return open_sets.from_bases_matroid((self.ground_set, self.independent_sets))
    
    @cached_property
    def hyperplanes(self) -> list[set[T]]:
        if self.axiom is MatroidAxiom.HYPERPLANES:
            return self.__second
        return hyperplanes.from_bases_matroid((self.ground_set, self.independent_sets))
    
    @cached_property
    def spanning_sets(self) -> list[set[T]]:
        if self.axiom is MatroidAxiom.SPANNING_SETS:
            return self.__second
        return spanning_sets.from_bases_matroid((self.ground_set, self.independent_sets))

    # ----------------------------------------------------------------------------------------- #
    #                                    Basic Properties                                       #
    # ----------------------------------------------------------------------------------------- #
    
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
    
    def closure(self, subset: set[T]) -> set[T]:
        """Find the closure of a given subset.

        Args:
            subset (set[T]): A subset of the ground set of the matroid.

        Returns:
            set[T]: The closure of a given subset.
        """
        return self.closure_function(subset)
    
    def is_closed(self, subset: set[T]) -> bool:
        """Check a given subset is closed or not.
        A closed set of M is a flat, that is, it satisfies cl(X) = X.

        Args:
            subset (set[T]): A subset of the ground set of the matroid.

        Returns:
            bool: True if a given subset is closed, False otherwise.
        """
        return self.closure(subset) == subset
    
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
        return e in self.loops
    
    def are_parallel(self, f: T, g: T) -> bool:
        """Check whether given elements f and g are parallel or not.

        Args:
            f (T): An element in the ground set of the matroid.
            g (T): An element in the ground set of the matroid.

        Returns:
            bool: True if given elements f and g are parallel, False otherwise.
        """
        return ({f, g} in self.circuits) or (f == g)
    
    @property
    def loops(self) -> set[T]:
        """Return the set of all the loops in the matroid.

        Returns:
            list[set[T]]: The set of all the loops in the matroid.
        """
        return self.closure(set())

    @property    
    def parallel_classes(self) -> list[set[T]]:
        """Return all the parallel classes of the matroid.
        A parallel class of a matroid is a maximal subset X of its ground set
        such that any two distinct member of X are parallel and no member of X is a loop.

        Returns:
            list[set[T]]: The set of all the parallel classes of the matroid.
        """
        if set() in self.bases:
            return []
        E = self.ground_set
        parallels = [{g for g in E if self.are_parallel(f,g) and (not self.is_loop(g))} for f in E if not self.is_loop(f)]
        parallel_sets = [*map(set, list({*map(tuple, parallels)}))] # Remove redundants
        return [pc for pc in parallel_sets if all(map(lambda ps: not pc < ps, parallel_sets))]
    
    @property
    def parallel_classes_are_trivial(self) -> bool:
        """Check whether the parallel classes are trivial or not.
        A parallel class is trivial if it contains just one element.

        Returns:
            bool: True if the parallel classes are trivial, False otherwise.
        """
        return {*map(len, self.parallel_classes)} == {1}
    
    @property
    def triangles(self) -> list[set[T]]:
        """Return the list of all triangles in the matroid.
        A triangle is a 3-element circuit.

        Returns:
           list[set[T]]: The set of all triangles in the matroid.
        """
        return [C for C in self.circuits if len(C) == 3]
    
    @cached_property
    def nonbases(self) -> list[set[T]]:
        """Return the set of all non-bases in the matroid.
        A non-basis is a set with cardinality r which is not a basis.

        Returns:
            list[set[T]]: The list of all non-bases.
        """
        return [NB for NB in map(set, combinations(self.ground_set, self.rank())) if self.rank(NB) < len(NB)]
    
    def is_isomorphic_to(self, matroid: Matroid, certificate: bool=False) -> Union[bool, tuple[bool, Union[dict[T,Any], None]]]:
        """Check whether the matroid and a given one are isomorphic.
        Two matroids M and N are isomorphic if there is a bijection f from the ground set of M to the ground set of N
        such that a subset X is independent in M if and only if f(X) is independent in N.

        Args:
            matroid (Matroid): A matroid
            certificate (bool, optional): If this is True, also returns an isomorphism as a dictionary. Defaults to False.


        Returns:
            Union[bool, tuple[bool, Union[dict[T,Any],None]]]: True if the two matroids are isomorphic, False otherwise.
                                           If certificate is True, also returns a dictionary representing a isomorphism.
        """
        if certificate:
            return (self.is_isomorphic_to(matroid), self.isomorphism_to(matroid))
        return (self.rank() == matroid.rank()) and (self.isomorphism_to(matroid) is not None)
    
    def isomorphism_to(self, matroid: Matroid) -> Union[dict[T, Any], None]:
        """Return an isomorphism from the matroid to a given one.
        The isomorphism is constructed with respect to nonbases.

        Args:
            matroid (Matroid): A matroid.

        Returns:
            Union[dict[T, Any], None]: If there exists an isomorphism, return the dictionary representing it, otherwise None.
        """
        if self.size != matroid.size:
            return None
        if self.rank() != matroid.rank():
            return None
        
        E1 = self.ground_set
        E2 = matroid.ground_set
        Nbs1 = self.nonbases
        Nbs2 = matroid.nonbases

        if len(Nbs1) != len(Nbs2):
            return None
        
        for perms in permutations(E2, matroid.size):
            morphism = dict(zip(E1, perms))
            transformed = [*map(lambda Nb: {*map(lambda e: morphism[e], Nb)} ,map(list, Nbs1))]
            if all(Nb in Nbs2 for Nb in transformed):
                return morphism
        return None
    
    def is_equal_to(self, matroid: Matroid) -> bool:
        """Check whether the matroid and a given one are equal.

        Args:
            matroid (Matroid): A matroid

        Returns:
            bool: True if the two matroids are equal, False otherwise.
        """
        if self.ground_set != matroid.ground_set:
            return False
        
        Nbs1 = self.nonbases
        Nbs2 = matroid.nonbases
        if len(Nbs1) != len(Nbs2):
            return False
        return all(map(lambda Nb: Nb in Nbs2, Nbs1))
    
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
        return Matroid((self.E, Bs_ast), axiom_check=False)

    @cached_property
    def coindependent_sets(self) -> list[set[T]]:
        """Construct the coindependent sets; the independent sets of the dual matroid.

        Returns:
            list[set[T]]: The coindependent sets of the matroid.
        """
        return self.dual.independent_sets
    
    @cached_property
    def codependent_sets(self) -> list[set[T]]:
        """Construct the codependent sets; the dependent sets of the dual matroid.

        Returns:
            list[set[T]]: The codependent sets of the matroid.
        """
        return self.dual.dependent_sets
    
    @cached_property
    def cobases(self) -> list[set[T]]:
        """Construct the cobases; the bases of the dual matroid.

        Returns:
            list[set[T]]: The cobases of the matroid.
        """
        return [ self.E - B for B in self.bases ]
    
    @cached_property
    def cocircuits(self) -> list[set[T]]:
        """Construct the cocircuits; the circuits of the dual matroid.

        Returns:
            list[set[T]]: The cocircuits of the matroid.
        """
        return self.dual.circuits
    
    @cached_property
    def corank_function(self) -> Callable[[set[T]], int]:
        """Construct the corank function; the rank function of the dual matroid.

        Returns:
            Callable[[set[T]], int]: The corank function of the matroid.
        """
        r = self.rank_function
        E = self.ground_set
        # r*(X) = r(E - X) + |X| - r(M)
        return lambda X: r(E - X) + len(X) - r(E)
    
    @cached_property
    def coclosure_function(self) -> Callable[[set[T]], set[T]]:
        """Construct the coclosure function; the closure function of the dual matroid.

        Returns:
            Callable[[set[T]], set[T]]: The coclosure function of the matroid.
        """
        return self.dual.closure_function
    
    @cached_property
    def coflats(self) -> list[set[T]]:
        """Construct the coflats; the flats of the dual matroid.

        Returns:
            list[set[T]]: The coflats of the matroid.
        """
        return self.dual.flats
    
    @cached_property
    def coopen_sets(self) -> list[set[T]]:
        """Construct the coopen sets; the open sets of the dual matroid.

        Returns:
            list[set[T]]: The coopen sets of the matroid.
        """
        return self.dual.open_sets
    
    @cached_property
    def cohyperplanes(self) -> list[set[T]]:
        """Construct the cohyperplanes; the hyperplanes of the matroid.

        Returns:
            list[set[T]]: The cohyperplanes of the matroid.
        """
        return self.dual.hyperplanes
    
    @cached_property
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
    
    def coclosure(self, subset: set[T]) -> set[T]:
        """Find the coclosure of a given subset of the ground set of the matroid.

        Args:
            subset (set[T]): A subset of the ground set.

        Returns:
            set[T]: The closure of a given subset.
        """
        return self.closure_function(subset)
    
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
        return e in self.coloops
    
    def are_coparallel(self, f: T, g: T) -> bool:
        """Check whether given elements f and g are coparallel or not.

        Args:
            f (T): An element in the ground set of the matroid.
            g (T): An element in the ground set of the matroid.

        Returns:
            bool: True if given elements f and g are coparallel, False otherwise.
        """
        return ({f, g} in self.cocircuits) or (f == g)
    
    @property
    def coloops(self) -> set[T]:
        """Return the set of all the coloops in the matroid.

        Returns:
            list[set[T]]: The set of all the coloops in the matroid.
        """
        return self.coclosure(set())

    @property    
    def coparallel_classes(self) -> list[set[T]]:
        """Return all the coparallel classes of the matroid.
        A coparallel class of a matroid is a maximal subset X of its ground set
        such that any two distinct member of X are coparallel and no member of X is a coloop.

        Returns:
            list[set[T]]: The set of all the coparallel classes of the matroid.
        """
        if set() in self.cobases:
            return []
        E = self.ground_set
        coparallels = [{g for g in E if self.are_parallel(f,g) and (not self.is_coloop(g))} for f in E if not self.is_coloop(f)]
        coparallel_sets = [*map(set, list({*map(tuple, coparallels)}))] # Remove redundants
        max_size = max(map(len, coparallel_sets))
        return [coparallel_class for coparallel_class in coparallel_sets if len(coparallel_class) == max_size]
    
    @property
    def coparallel_classes_are_trivial(self) -> bool:
        """Check whether the coparallel classes are trivial or not.
        A coparallel class is trivial if it contains just one element.

        Returns:
            bool: True if the coparallel classes are trivial, False otherwise.
        """
        return {*map(len, self.coparallel_classes)} == {1}
    
    @property
    def triads(self) -> list[set[T]]:
        """Return the list of all triads in the matroid.
        A triangle is a 3-element cocircuit.

        Returns:
           list[set[T]]: The set of all triads in the matroid.
        """
        return [C_ast for C_ast in self.cocircuits if len(C_ast) == 3]
    
    # ----------------------------------------------------------------------------------------------- #
    #                                    Matroid Construction                                         #
    # ----------------------------------------------------------------------------------------------- #

    def restrict_to(self, X: Union[set[T], T]) -> Matroid:
        """Restrict the matroid to X.
        For faster calculation and saving memory, the circuits are used in this operation.

        Args:
            X (Union[set[T], T]): A subset of the ground set of the matroid.
        
        Raises:
            ValueError: if the given set X is not included in the ground set.

        Returns:
            Matroid: The restriction of the matroid to X
        """
        E = self.ground_set
        if isinstance(X, set):
            if not X <= E:
                raise ValueError("The set for the restriction must be a subset of the ground set!")
            # Cs|X = { C ⊆ X : C ∈ Cs }
            CsX = [C for C in self.circuits if C <= X]
            return Matroid((X, CsX), axiom=MatroidAxiom.CIRCUITS, axiom_check=False)
        
        return self.restrict_to({X})

    def delete(self, X: Union[set[T], T]) -> Matroid:
        """Delete a given set X from the matroid.
        For faster calculation and saving memory, the circuits are used in this operation.

        Args:
            X (Union[set[T], T]): A subset of the ground set of the matroid.

        Raises:
            ValueError: if the given set X is not included in the ground set.

        Returns:
            Matroid: The deletion of X from the matroid
        """
        if isinstance(X, set):
            return self | (self.ground_set - X)

        return self | (self.ground_set - {X})
    
    def contract(self, X: Union[set[T], T]) -> Matroid:
        """Contract a given set X from the matroid.
        For faster calculation and saving memory, the circuits are used in this operation.

        Args:
            X (Union[set[T], T]): A subset of the ground set of the matroid.

        Raises:
            ValueError: if the given set X is not included in the ground set.

        Returns:
            Matroid: The contraction of X from the matroid
        """
        if isinstance(X, set):
            return (self.dual - X).dual

        return (self.dual - {X}).dual

    def simplification(self) -> Matroid:
        """Construct a simple matroid associated with the matroid.

        Returns:
            Matroid: The simplification of the matroid.
        """
        return self.restrict_to({*map(min, self.parallel_classes)})

    @staticmethod
    def si(matroid: Matroid) -> Matroid:
        """Construct a simple matroid associated with a given matroid.

        Args:
            matroid (Matroid): A matroid.

        Returns:
            Matroid: The simplification of a given matroid.
        """
        return matroid.restrict_to({*map(min, matroid.parallel_classes)})
    
    def union(self, matroid: Matroid) -> Matroid:
        """Calculate the union of this and another matroids.

        Args:
            matroid (Matroid): A matroid.

        Returns:
            Matroid: The union of this and the other matroids.
        """
        r1 = self.rank_function
        r2 = matroid.rank_function
        # r(X) = min{ r1(Y) + r2(Y) + |X - Y| : Y ⊆ X }
        r = lambda X: min(r1(Y) + r2(Y) + len(X - Y) for Y in powset(X))
        return Matroid((self.ground_set | matroid.ground_set, r), axiom=MatroidAxiom.RANK_FUNCTION, axiom_check=False)
    
    def direct_sum(self, matroid: Matroid) -> Matroid:
        """Calculate the direct sum or 1-sum of this and another matroids whose ground sets are disjoint.

        Args:
            matroid (Matroid): A matroid.
        
        Raises:
            ValueError: When the ground sets are not disjoint.

        Returns:
            Matroid: The direct sum of this and the other matroids.
        """
        if not self.ground_set.isdisjoint(matroid.ground_set):
            raise ValueError("The ground sets of two matroids must be disjoint!!")

        # E = E1 ⊔ E2 (disjoint union), Cs = Cs1 ⊔ Cs2 (disjoint union)
        return Matroid((self.ground_set | matroid.ground_set, self.circuits + matroid.circuits), axiom=MatroidAxiom.CIRCUITS, axiom_check=False)
    
    def free_product(self, matroid: Matroid) -> Matroid:
        """Calculate the free product of this and another matroids whose ground sets are disjoint.

        Args:
            matroid (Matroid): A matroid.

        Raises:
            ValueError: When the ground sets are not disjoint.

        Returns:
            Matroid: The free product of this and the other matroids.
        """
        if not self.ground_set.isdisjoint(matroid.ground_set):
            raise ValueError("The ground sets of two matroids must be disjoint!!")
        
        # E = E1 ⊔ E2 (disjoint union)
        E1 = self.ground_set
        E2 = matroid.ground_set
        E = E1 | E2
        # Bs = { B ⊆ E1 ⊔ E2 : |B| = r(M1) + r(M2), B ∩ E1 ∈ Is1, B ∩ E2 ∈ Ss2 }
        size = self.rank() + matroid.rank()
        Is1 = self.independent_sets
        Ss2 = matroid.spanning_sets
        Bs = [B for B in map(set, combinations(E, size)) if (B & E1 in Is1) and (B & E2 in Ss2)]
        return Matroid((E, Bs))

    # ----------------------------------------------------------------------------------------------- #
    #                                      Other Properties                                           #
    # ----------------------------------------------------------------------------------------------- #

    @property
    def is_free(self) -> bool:
        """Check whether the matroid is free, that is, it has no dependent set.

        Returns:
            bool: True when the matroid is free, False otherwise.
        """
        return not self.dependent_sets
    
    @property
    def is_trivial(self) -> bool:
        """Check whether the matroid is trivial, that is, it has only one basis, empty set.

        Returns:
            bool: True when the matroid is trivial, False otherwise.
        """
        return len(self.bases) == 1
    
    @property
    def is_empty(self) -> bool:
        """Check whether the matroid is empty, that is, it has no element in ground set.

        Returns:
            bool: True when the matroid is emtpy, False otherwise.
        """
        return not self.ground_set
    
    @property
    def is_simple(self) -> bool:
        """Check whether the matroid is simple, that is, it has no loops and no non-trivial parallel classes.

        Returns:
            bool: True when the matroid is simple, False otherwise
        """
        return (not self.loops) and self.parallel_classes_are_trivial
    
    @property
    def is_cosimple(self) -> bool:
        """Check whether the matroid is cosimple, that is, it has no coloops and no non-trivial coparallel classes.

        Returns:
            bool: True when the matroid is simple, False otherwise
        """
        return (not self.coloops) and self.coparallel_classes_are_trivial
    
    @property
    def is_paving(self) -> bool:
        """Check whether the matroid is paving or not.
        A matroid is called paving if it has no circuit of size less than r(M).

        Returns:
            bool: True if the matroid is paving, False otherwise.
        """
        return all(map(lambda C: self.rank(C) >= self.rank() ,self.circuits))
    
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
        
        Raises:
            ValueError: when the length of the code doesn't match nCr, where n is the size, and r is the rank.
            ValueError: when the given code includes any invalid symbol.

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
    
    def is_independent(self, X: set[T]) -> bool:
        """Check whether a given subset X is independent or not.
        It can be checked more efficiently than X in self.independent_sets.

        Args:
            X (set[T]): A subset of the ground set of the matroid.

        Returns:
            bool: True if a given subset is independent, False otherwise.
        """
        return len(X) == self.rank(X)

    def is_coindependent(self, X: set[T]) -> bool:
        """Check whether a given subset X is coindependent or not.
        It can be checked more efficiently than X in self.coindependent_sets.

        Args:
            X (set[T]): A subset of the ground set of the matroid.

        Returns:
            bool: True if a given subset is coindependent, False otherwise.
        """
        return len(X) == self.corank(X)
    
    def is_dependent(self, X: set[T]) -> bool:
        """Check whether a given subset X is dependent or not.
        It can be checked more efficiently than X in self.dependent_sets

        Args:
            X (set[T]): A subset of the ground set of the matroid.

        Returns:
            bool: True if a given subset is dependent, False otherwise.
        """
        return len(X) != self.rank(X)

    def is_codependent(self, X: set[T]) -> bool:
        """Check whether a given subset X is codependent or not.
        It can be checked more efficiently than X in self.codependent_sets

        Args:
            X (set[T]): A subset of the ground set of the matroid.

        Returns:
            bool: True if a given subset is codependent, False otherwise.
        """
        return len(X) != self.corank(X)
    
    def is_basis(self, X: set[T]) -> bool:
        """Check whether a given subset X is a basis or not.
        It can be checked more efficiently than X in self.bases.

        Args:
            X (set[T]): A subset of the ground set of the matroid.

        Returns:
            bool: True if a given subset is a basis, False otherwise.
        """
        return (len(X) == self.rank()) and (len(X) == self.rank(X))
    
    def is_cobasis(self, X: set[T]) -> bool:
        """Check whether a given subset X is a cobasis or not.
        It can be checked more efficiently than X in self.cobases.

        Args:
            X (set[T]): A subset of the ground set of the matroid.

        Returns:
            bool: True if a given subset is a cobasis, False otherwise.
        """
        return (len(X) == self.corank()) and (len(X) == self.corank(X))