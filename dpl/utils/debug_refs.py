import gc
from pprint import pprint


def print_referrers(instance: object) -> None:
    """
    Print referrers of object instance
    :param instance: studied instance
    :return: None
    """
    print(instance)
    pprint(gc.get_referents(instance))
    print()
