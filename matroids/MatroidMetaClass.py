from .core.exception import MatroidAxiomError

class MatroidMetaClass(type):
    def __new__(meta: type, name: str, bases: tuple, attributes: dict):
        """Run when a class is generated.

        Args:
            meta (type): The metaclass of the class
            name (str): The class name
            bases (tuple): The parent classes
            attributes (dict): The class attributes

        Raises:
            MatroidAxiomError: occurs when a given object doesn't have any axioms.

        Returns:
            [type]: The generated matroid.
        """
        if bases != (object,): # The abstaract class won't be validated.
            try:
                attributes["axiom"]
            except KeyError:
                raise MatroidAxiomError(f"The Matroid doesn't have any axioms!!")
        return type.__new__(meta,name,bases,attributes)