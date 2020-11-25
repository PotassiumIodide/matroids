from __future__ import annotations
from typing import Callable

from matroids.core.set_operator import powset

from matroids.Matroid import Matroid

class UniformMatroid(Matroid):
    def __init__(self, k: int, n: int):
        if k > n:
            raise ValueError("The rank must be smaller than the size!!")
        self.__k = k
        self.__n = n
    
    def __repr__(self) -> str:
        article = "an" if self.n in {8,11,18} or str(self.n)[0] == '8' else "a"
        return f"The rank-{self.k} uniform matroid on {article} {self.n}-element set."
    
    @property
    def k(self) -> int:
        return self.__k

    @property
    def n(self) -> int:
        return self.__n
    
    @property
    def ground_set(self) -> set[int]:
        return {*map(lambda i: i+1, range(self.n))}

    @property
    def independent_sets(self) -> list[set[int]]:
        # Is(U_{k,n}) = { I ⊆ E : |I| ≦ k }
        return [ I for I in powset(self.E) if len(I) <= self.k ]
    
    @property
    def dependent_sets(self) -> list[set[int]]:
        # Ds(U_{k,n}) = { D ⊆ E : |D| > k }
        return [ D for D in powset(self.E) if len(D) > self.k ]
    
    @property
    def bases(self) -> list[set[int]]:
        # Bs(U_{k,n}) = { B ⊆ E : |B| = k }
        return [ B for B in powset(self.E) if len(B) == self.k ]
    
    @property
    def circuits(self) -> list[set[int]]:
        # Cs(U_{n,n}) = ∅
        if self.k == self.n:
            return []        
        # Cs(U_{k,n}) = { C ⊆ E : |C| = k + 1 } (k ≠ n)
        return [C for C in powset(self.E) if len(C) == self.k + 1]
    
    @property
    def rank_function(self) -> Callable[[set[int]], int]:
        # r(X) = |X| if |X| < k, k if |X| ≧ k
        return lambda X: min({len(X), self.k})
    
    @property
    def closure_function(self) -> Callable[[set[int]], set[int]]:
        # cl(X) = X if |X| ≦ k, E if |X| > k
        return lambda X: X if len(X) <= self.k else self.E
    
    @property
    def dual(self) -> UniformMatroid:
        # U_{k,n}* = U_{n-k,n}
        return UniformMatroid(self.n - self.k, self.n)
    
    @property
    def coindependent_sets(self) -> list[set[int]]:
        # Is*(U_{k,n}) = { I* ⊆ E : |I*| ≦ n - k }
        return [ I_ast for I_ast in powset(self.E) if len(I_ast) <= self.n - self.k ]
    
    @property
    def codependent_sets(self) -> list[set[int]]:
        # Ds*(U_{k,n}) = { D* ⊆ E : |D*| > n - k }
        return [ D_ast for D_ast in powset(self.E) if len(D_ast) > self.n - self.k ]

    @property
    def cobases(self) -> list[set[int]]:
        # Bs*(U_{k,n}) = { B* ⊆ E : |B*| = n - k }
        return [ B_ast for B_ast in powset(self.E) if len(B_ast) == self.n - self.k ]
    
    @property
    def cocircuits(self) -> list[set[int]]:
        # Cs*(U_{0,n}) = ∅
        if self.k == 0:
            return []        
        # Cs*(U_{k,n}) = { C* ⊆ E : |C*| = n - k + 1 } (k ≠ 0)
        return [C_ast for C_ast in powset(self.E) if len(C_ast) == self.n - self.k + 1]

    @property
    def corank_function(self) -> Callable[[set[int]], int]:
        # r*(X) = |X| if |X| < n - k, n - k if |X| ≧ n - k
        return lambda X: min({len(X), self.n - self.k})
    
    @property
    def coclosure_function(self) -> Callable[[set[int]], set[int]]:
        # cl*(X) = X if |X| ≦ n - k, E if |X| > n - k
        return lambda X: X if len(X) <= self.n - self.k else self.E
    
    def description(self) -> str:
        k, n = self.k, self.n
        q = {2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41,43,47,49,53,59,61,64,67,71,73,79,81,83,89,97}
        article = "an" if n in {8,11,18} or str(n)[0] == '8' else "a"
        selfdual = "identically self-dual " if n == 2*k else ""
        description = [f"The rank-{k} {selfdual}uniform matroid on {article} {n}-element set."]
        if (k,n) == (2,4):
            description.append("・The 4-point line; isomorphic to the rank-2 whirl.")
            description.append("・The unique excluded minor for the class of binary matroids.")
            description.append("・F-representable if and only if |F| ≧ 3; near-regular.")
            description.append("・The unique 3-connected non-binary matroid M having an element e such that both M\e and M/e are binary.")
            description.append("・The unique matroid M with at least four elements such that { M } is 2-rounded.")
        if (k,n) in {(2,5), (3,5)}:
            if (k,n) == (2,5):
                description.append("・The 5-point line.")
                description.append("・U_{2,5} is obtained from U_{3,5} by a Y-Δ exchange.")
            else:
                description.append("・The five points freely placed in the plane.")
                description.append("・U_{3,5} is obtained from U_{2,5} by a Δ-Y exchange.")
            description.append("・F-representable if and only if |F| ≧ 4.")
            description.append("・One of the excluded minors for the class of ternary matroids.")
            description.append("・Not graphic, not cographic, not regular, and not near-regular.")
        if (k,n) == (3,6):
            description.append("・Six points freely placed in the plane; the tipless free 3-spike.")
            description.append("・F-representable if and only if |F|≧ 4.")
            description.append("・Not graphic, not cographic, not regular, not near-regular.")
            description.append("・The unique relaxation of P6.")
        else:
            if ((n-2) in q) and (k in {2, n-2}):
                description.append(f"・Excluded minor for GF({n-2})-representability.")
            description.append("・Transversal, a strict gammoid, a gammoid.")
            description.append("・Automorphism group is the symmetric group.")
            description.append("・Every minor is also uniform.")
            if not ((n > 0 and 0 in {k, n-k}) or (n > 3 and 1 in {k, n-k})):
                description.append("・3-connected.")
            description.append("・Algebraic over all fields.")
        return "\n".join(description)


class FreeMatroid(UniformMatroid):
    def __init__(self, n: int):
        super().__init__(n, n)
    
    def __repr__(self) -> str:
        article = "an" if self.n in {8,11,18} or str(self.n)[0] == '8' else "a"
        return f"The rank-{self.n} free matroid on {article} {self.n}-element set."


class TrivialMatroid(UniformMatroid):
    def __init__(self, n: int):
        super().__init__(0, n)
    
    def __repr__(self) -> str:
        article = "an" if self.n in {8,11,18} or str(self.n)[0] == '8' else "a"
        return f"The trivial matroid on {article} {self.n}-element set."

class EmptyMatroid(UniformMatroid):
    def __init__(self):
        super().__init__(0, 0)
    
    def __repr__(self) -> str:
        return "The empty matroid."
