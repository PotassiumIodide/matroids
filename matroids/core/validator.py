from functools import wraps

from .checker import (
    satisfies_independent_axiom,
    satisfies_dependent_axiom,
    satisfies_bases_axiom,
    satisfies_circuits_axiom,
    satisfies_rank_function_axiom,
    satisfies_closure_axiom,
    satisfies_open_sets_axiom,
    satisfies_hyperplanes_axiom,
    satisfies_spanning_sets_axiom,
)
from .exception import MatroidAxiomError
from .types import MatroidAxiom

def validate_matroid_axiom(func):

    @wraps(func)
    def __wrapper(*args, **kwargs):
        maybe_matroid, axiom = args[0], args[1]
        if any([
            axiom is MatroidAxiom.INDEPENDENT_SETS and not satisfies_independent_axiom(maybe_matroid),
            axiom is MatroidAxiom.DEPENDENT_SETS   and not satisfies_dependent_axiom(maybe_matroid),
            axiom is MatroidAxiom.BASES            and not satisfies_bases_axiom(maybe_matroid),
            axiom is MatroidAxiom.CIRCUITS         and not satisfies_circuits_axiom(maybe_matroid),
            axiom is MatroidAxiom.RANK_FUNCTION    and not satisfies_rank_function_axiom(maybe_matroid),
            axiom is MatroidAxiom.CLOSURE_FUNCTION and not satisfies_closure_axiom(maybe_matroid),
            axiom is MatroidAxiom.OPEN_SETS        and not satisfies_open_sets_axiom(maybe_matroid),
            axiom is MatroidAxiom.HYPERPLANES      and not satisfies_hyperplanes_axiom(maybe_matroid),
            axiom is MatroidAxiom.SPANNING_SETS    and not satisfies_spanning_sets_axiom(maybe_matroid),
        ]):
            raise MatroidAxiomError(f"The given family doesn't satisfy {axiom.value}!")

        return func(*args, **kwargs)
    
    return __wrapper


def validate_independent_sets(func):

    @wraps(func)
    def __wrapper(*args, **kwargs):
        if not satisfies_independent_axiom(args[0]):
            raise MatroidAxiomError("The given family doesn't satisfy the axiom of Independent Sets!")
        return func(*args, **kwargs)
    
    return __wrapper


def validate_dependent_sets(func):

    @wraps(func)
    def __wrapper(*args, **kwargs):
        if not satisfies_dependent_axiom(args[0]):
            raise MatroidAxiomError("The given family doesn't satisfy the axiom of Dependent Sets!")
        return func(*args, **kwargs)
    
    return __wrapper


def validate_bases(func):

    @wraps(func)
    def __wrapper(*args, **kwargs):
        if not satisfies_bases_axiom(args[0]):
            raise MatroidAxiomError("The given family doesn't satisfy the axiom of Bases!")
        return func(*args, **kwargs)
    
    return __wrapper


def validate_circuits(func):

    @wraps(func)
    def __wrapper(*args, **kwargs):
        if not satisfies_circuits_axiom(args[0]):
            raise MatroidAxiomError("The given family doesn't satisfy the axiom of Circuits!")
        return func(*args, **kwargs)
    
    return __wrapper


def validate_rank_function(func):

    @wraps(func)
    def __wrapper(*args, **kwargs):
        if not satisfies_rank_function_axiom(args[0]):
            raise MatroidAxiomError("The given family doesn't satisfy the axiom of Rank Function!")
        return func(*args, **kwargs)
    
    return __wrapper


def validate_closure_function(func):

    @wraps(func)
    def __wrapper(*args, **kwargs):
        if not satisfies_closure_axiom(args[0]):
            raise MatroidAxiomError("The given family doesn't satisfy the axiom of Closure Function!")
        return func(*args, **kwargs)
    
    return __wrapper


def validate_open_sets(func):

    @wraps(func)
    def __wrapper(*args, **kwargs):
        if not satisfies_open_sets_axiom(args[0]):
            raise MatroidAxiomError("The given family doesn't satisfy the axiom of Open Sets!")
        return func(*args, **kwargs)
    
    return __wrapper


def validate_hyperplanes(func):

    @wraps(func)
    def __wrapper(*args, **kwargs):
        if not satisfies_hyperplanes_axiom(args[0]):
            raise MatroidAxiomError("The given family doesn't satisfy the axiom of Hyperplanes!")
        return func(*args, **kwargs)
    
    return __wrapper


def validate_spanning_sets(func):

    @wraps(func)
    def __wrapper(*args, **kwargs):
        if not satisfies_spanning_sets_axiom(args[0]):
            raise MatroidAxiomError("The given family doesn't satisfy the axiom of Spanning Sets!")
        return func(*args, **kwargs)
    
    return __wrapper