import click


POPULATION_SIZE = 6


def fitness(dnr: list) -> int:
    print(dnr)
    score = input("Enter score> ")
    return int(score)


def random_dnr(size: int, seq: list) -> list:
    from random import choice
    return [choice(seq) for _ in range(0, size)]


def evaluate(population: list) -> list:
    for pop in population:
        yield fitness(pop), pop


def mix(dnr1: list, dnr2: list, size: int) -> list:
    from random import randint
    r = randint(1, size)
    return dnr1[:r] + dnr2[r:]


def mutate(dnr: list, seq: list):
    from random import randint, choice
    if randint(0, 1000) == 0:
        print("Mutating")
        r = randint(0, len(dnr) - 1)
        dnr[r] = choice(seq)


def evolution(population, size, seq):
    top = sorted(evaluate(population), key=lambda x: x[0])[:int(POPULATION_SIZE / 2)]
    population.clear()
    for i in range(0, len(top)):
        for j in range(i, len(top)):
            population.append(mix(top[i][1], top[j][1], size))

    for pop in population:
        mutate(pop, seq)


@click.command()
@click.option("--size", help="Sequance length", type=int)
@click.argument("seq", nargs=-1)
def main(size, seq):
    population = [random_dnr(size, seq)
                  for i in range(0, POPULATION_SIZE)]

    iteration = 1
    while True:
        print("iteration: {0}".format(iteration))
        evolution(population, size, seq)
        iteration += 1

if __name__ == "__main__":
    main()
