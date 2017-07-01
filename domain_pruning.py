from sets import Set


def domain_pruning(noisy_data, dataset, threshold):
    """
    :type noisy_data: list[(int,string)]
    :type dataset: list[dict[string, string]]
    :type threshold: float
    :rtype: list[set[string]]
    """
    repair_candidates = []
    for c in noisy_data:
        # Initialize repair candidates
        repair_candidate = Set()
        c_row = c[0]
        c_attr = c[1]
        domain_c_attr = domain(dataset, c_attr)
        for attr in dataset[c_row]:
            if attr != c_attr:
                v_attr = dataset[c_row][attr]
                for c_v in domain_c_attr:
                    # Calculate the Pr(v_c | v_attr)
                    num_both = 0
                    num_v_attr = 0
                    for i in xrange(len(dataset)):
                        if dataset[i][c_attr] == c_v and dataset[i][attr] == v_attr:
                            num_both += 1

                        if dataset[i][attr] == v_attr:
                            num_v_attr += 1

                    pr = float(num_both) / num_v_attr
                    if pr >= threshold:
                        repair_candidate.add(c_v)
        repair_candidates.append(list(repair_candidate))

    return repair_candidates


def domain(dataset, attr):
    """
    Returns the full domain of an attribute
    :type dataset: list[dict[string, string]]
    :type attr: string
    :rtype: list[string]
    """
    domain = Set()
    for i in xrange(len(dataset)):
        domain.add(dataset[i][attr])
    return list(domain)


# Tests
data = [
    ['toronto', '94133', 'canada', 'CA'],
    ['toronto', '94133', 'usa', 'CA'],
    ['toronto', '94133', 'canada', 'CA'],
    ['waterloo', '94133', 'canada', 'ON'],
    ['waterloo', '94133', 'canada', 'ON'],
    ['waterloo', '94133', 'usa', 'ON'],
    ['vaughan', '94156', 'canada', 'NM'],
]
lst_attr = ['city', 'zip', 'country', 'state']

dataset = []
for i in xrange(len(data)):
    row = {}
    for j in xrange(len(data[i])):
        row[lst_attr[j]] = data[i][j]
    dataset.append(row)

dirty = [[3, "city"]]
assert( set(domain_pruning(dirty, dataset, 0.5)[0]) == set(['toronto', 'waterloo']))
