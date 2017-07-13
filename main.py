from data import Dataset
from domain_pruning import domain_pruning
import denial_constraint
import ground_constraints
import statistical_quant

# creating dataset structure from CSV file
filename = "test.csv"
threshold = 0.5

dataset = Dataset(filename)

noisy_cells = error_dectection(dataset)

domain_noisy_cells = domain_pruning(noisy_cells, dataset, threshold)

denial_constraints = denial_constraint.create_denial_constraints()

denial_constraint_grounding = ground_constraints.ground_constraints(dataset, noisy_cells, domain_noisy_cells, denial_constraints)

quant_stat_grounding = statistical_quant.statistical_quant(dataset, noisy_cells)

