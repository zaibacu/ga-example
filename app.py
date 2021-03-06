import click


def manual_fitness(dnr: list) -> int:
    print(dnr)
    score = input("Enter score> ")
    return int(score)


def random_dnr(size: int, seq: list) -> list:
    from random import choice
    return [choice(seq) for _ in range(0, size)]


def evaluate(population: list, fitness_fn: callable) -> list:
    for pop in population:
        yield fitness_fn(pop), pop


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


def evolution(population, fitness_fn, size, seq, limit):
    top = sorted(evaluate(population, fitness_fn), key=lambda x: x[0], reverse=True)[:limit]
    print(top)
    population.clear()
    for i in range(0, len(top)):
        for j in range(i, len(top)):
            population.append(mix(top[i][1], top[j][1], size))

    population += top

    for pop in population:
        mutate(pop, seq)


@click.command()
@click.option("--size", help="Sequance length", type=int)
@click.option("--population_size", help="Population size", type=int, default=6)
@click.option("--fitness_fn", help="Fitness function", type=str, default="__main__.manual_fitness")
@click.argument("seq", nargs=-1)
def main(size, population_size, fitness_fn,  seq):

    population = [random_dnr(size, seq)
                  for i in range(0, population_size)]

    def get_function():
        buff = fitness_fn.split(".")
        mod = ".".join(buff[:-1])
        fn = buff[-1]
        m = __import__(mod)
        return getattr(m, fn)

    fitness = get_function()
    iteration = 1
    while True:
        print("iteration: {0}".format(iteration))
        evolution(population, fitness, size, seq, int(population_size / 2))
        iteration += 1

if __name__ == "__main__":
    main()
