from functools import reduce
from typing import Iterable


def accumulate(current: int, iterable: Iterable[str]) -> int:
    """Accumulate a value across all lines of a file."""
    for line in iterable:
        line = line.strip()
        positive_count = line.count("+")
        negative_count = line.count("-")

        current = current + positive_count - negative_count

    return current

def main():
    with open("record.txt", "r") as f:
        count = reduce(accumulate, f.readlines(), 0)
        print(count)

if __name__ == "__main__":
    main()