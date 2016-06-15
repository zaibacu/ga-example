import click


POPULATION_SIZE = 6


def fitness(dnr: list) -> int:
    return 0


def random_dnr(size: int, seq: list) -> list:
    from random import choice
    return [choice(seq) for _ in range(0, size)]


def evaluate(population: list) -> list:
    for pop in population:
        yield fitness(pop), pop


@click.command()
@click.option("--size", help="Sequance length", type=int)
@click.argument("seq", nargs=-1)
def main(size, seq):
    population = [random_dnr(size, seq)
                  for i in range(0, POPULATION_SIZE)]

    for pop in population:
        print(pop)

if __name__ == "__main__":
    main()
