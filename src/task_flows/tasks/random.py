import random
from prefect import task


@task
def get_fact(start=1, end=100):
    return random.randint(start, end)
