from multiprocessing.reduction import AbstractRepository


def allocate(line: OrderLine, repo: AbstractRepository, session) -> str: