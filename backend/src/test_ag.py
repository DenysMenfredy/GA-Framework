from core.algorithms.ga import GeneticAlgorithm
from core.problems.holder_table import HolderTable

if __name__ == '__main__':
    params = {
        "size_pop": 100,
        "generations": 100,
        "crossover_rate": 0.9,
        "mutation_rate": 0.05,
        "crossover_method": "twoPoint",
        "problem": "HolderTable",
        "dimension": 10

    }

    ga = GeneticAlgorithm(**params)
    best = ga.start()
    print(best)