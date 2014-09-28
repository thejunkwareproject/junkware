import random

bases = "ACGT"

def random_dna_sequence(length):
    return ''.join(random.choice(bases) for _ in range(length))

def base_frequency(dna):
    d = {}
    for base in bases:
        d[base] = dna.count(base)/float(len(dna))
    return d

#yields a strand with an A-T mutation frequency of 0.066%
def mutate(orig_string, mutation_rate=0.0066):
    result = []
    mutations = []
    for base in orig_string:
        if random.random() < mutation_rate:
            new_base = bases[bases.index(base) - random.randint(1, 3)] # negatives are OK
            result.append(new_base)
            mutations.append((base, new_base))
        else:
            result.append(base)
    return "".join(result), mutations

def get_random_dna() :
    dna = random_dna_sequence(4028)
    # print dna
    return dna
