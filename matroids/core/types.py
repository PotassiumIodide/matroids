from enum import Enum

class MatroidAxiom(Enum):
    INDEPENDENT_SETS = "The axiom for Independent Sets"
    DEPENDENT_SETS   = "The axiom for Dependent Sets"
    BASES            = "The axiom for Bases"
    CIRCUITS         = "The axiom for Circuits"
    RANK_FUNCTION    = "The axiom for Rank Function"
    NULITY_FUNCTION  = "The axiom for Nulity Function"
    CLOSURE_FUNCTION = "The axiom for Closure Function"
    FLATS            = "The axiom for Flats"
    OPEN_SETS        = "The axiom for Open Sets"
    HYPERPLANES      = "The axiom for Hyperplanes"
    SPANNING_SETS    = "The axiom for Spanning Sets"
