

class DenialConstraint:
    """
    Represents a list of predicates which make up a denial contraint.
    e.g. !(predicate_1 and ... and predicate_n)
    """
    def __init__(self):
        self.operators = {
            '=': 0,
            '<': 1,
            '>': 2,
            '!=': 3,
            '<=': 4,
            '~=': 5
        }

        self.predicates = []

        # TODO: Initialize the List of predicates (unknown)


class Predicate:
    """
    Represents a single predicate within a denial constraint.
    e.g. t1.attr > t2.attr
    """
    def __init__(self, attr, operator):
        self.attr = attr
        self.operator = operator

def create_denial_constraints():
    """
    unknown if this function is needed
    :return:
    """
    pass