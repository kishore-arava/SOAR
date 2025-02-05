from prefect import flow
from src.task_flows.tasks.random import get_fact


@flow
def random_flow():
    get_fact.map()
