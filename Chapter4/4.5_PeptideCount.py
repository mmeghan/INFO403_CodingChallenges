'''
Goal:The Cyclopeptide Sequencing Problem
Input: an integer m
Output: The number of linear peptides having integer mass m
'''

def get_amino_acid_mass():
    mass = {
        "G": 57,
        "A": 71,
        "S": 87,
        "P": 97,
        "V": 99,
        "T": 101,
        "C": 103,
        "I": 113,
        "L": 113,
        "N": 114,
        "D": 115,
        "K": 128,
        "Q": 128,
        "E": 129,
        "M": 131,
        "H": 137,
        "F": 147,
        "R": 156,
        "Y": 163,
        "W": 186,
    }

    return mass

def get_all_combinations_worker(mass, aa_masses, counter):
    #counter remembers number of combinations for each mass in process so we don't have to compute it every time
    if mass in counter:
        return counter[mass]
    if mass < 0:
        return 0
    if mass == 0:
        return 1
    counter[mass] = 0
    for aa_mass in aa_masses:
        counter[mass] += get_all_combinations_worker(mass - aa_mass, aa_masses, counter)

    return counter[mass]


def get_all_combinations(mass):
    aa_masses = set(get_amino_acid_mass().values())
    counter = dict()
    res = get_all_combinations_worker(mass, aa_masses, counter)
    return res


x=1426
result=get_all_combinations(x)
print(result)