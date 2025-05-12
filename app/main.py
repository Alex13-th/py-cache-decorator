from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cashed_result = {}

    def cache_wrapper(*args) -> Any:
        if args in cashed_result:
            print("Getting from cache")
            return cashed_result[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cashed_result[args] = result
            return result
    return cache_wrapper
