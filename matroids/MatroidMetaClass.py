class MatroidMetaClass(type):
    def __new__(meta: type, name: str, bases: tuple, attributes: dict):
        """Run when a class is generated.

        Args:
            meta (type): The metaclass of the class
            name (str): The class name
            bases (tuple): The parent classes
            attributes (dict): The class attributes

        Returns:
            [type]: The generated matroid.
        """
        return type.__new__(meta,name,bases,attributes)