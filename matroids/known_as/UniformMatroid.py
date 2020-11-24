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


class FreeMatroid(UniformMatroid):
    def __init__(self, n: int):
        super().__init__(n, n)


class TrivialMatroid(UniformMatroid):
    def __init__(self, n: int):
        super().__init__(0, n)


class EmptyMatroid(UniformMatroid):
    def __init__(self):
        super().__init__(0, 0)
