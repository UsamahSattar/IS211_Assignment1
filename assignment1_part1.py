# assignment1_part1.py

class ListDivideException(Exception):
    """Raised when a list_divide test fails."""
    pass


def list_divide(numbers, divide=2):
    """Return how many elements in `numbers` are divisible by `divide`."""
    if divide == 0:
        raise ValueError("divide must not be zero")
    return sum(1 for n in numbers if n % divide == 0)


def test_list_divide():
    """Run the required tests. Raise ListDivideException on any failure."""
    tests = [
        (([1, 2, 3, 4, 5],), {}, 2),
        (([2, 4, 6, 8, 10],), {}, 5),
        (([30, 54, 63, 98, 100],), {"divide": 10}, 2),
        (([],), {}, 0),
        (([1, 2, 3, 4, 5],), {"divide": 1}, 5),
    ]
    for args, kwargs, expected in tests:
        result = list_divide(*args, **kwargs)
        if result != expected:
            raise ListDivideException(
                f"Expected {expected} for args={args}, kwargs={kwargs}, got {result}"
            )


if __name__ == "__main__":
    test_list_divide()

