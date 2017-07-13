
class GroundingConstraint:
    def __init__(self, t_index, denial_constraint, noisy_cell, domain, truth_value):
        """
        :type t_index: int
        :type denial_constraint: DenialConstraint
        :type noisy_cell: List((int, int))
        :type domain: string
        :type truth_value: int
        """
        self.t_index = t_index
        self.denial_constraint = denial_constraint
        self.noisy_cell = noisy_cell
        self.domain = domain
        self.truth_value = truth_value


def ground_constraints(dataset, noisy_data, noisy_data_domains, denial_constraints):
    """
    Create list of GroundingConstraint objects and return it
    :type dataset: Dataset
    :type noisy_data: List(tuple(int, int))
    :type noisy_data_domains:  List(Set(string))
    :type denial_constraints: List(DenialConstraint)
    :return: List(GroundingConstraint)
    """

    pass