from __future__ import annotations
from typing import Iterable, Tuple


def sum_even_and_odd(lst: Iterable) -> Tuple[int, int]:
    sum_even = 0
    sum_odd = 0
    for x in lst:
        # Exclude booleans (True/False) which are instances of int
        if isinstance(x, bool):
            continue
        if isinstance(x, int):
            if x % 2 == 0:
                sum_even += x
            else:
                sum_odd += x
        else:
            continue
    return sum_even, sum_odd

TESTS = [
    ([], (0, 0)),
    ([1], (0, 1)),
    ([2], (2, 0)),
    ([1, 2, 3, 4], (6, 4)),
    ([0, -1, -2, 5], (-2, 4)),
    ([True, False, 1, 2], (2, 1)),  
    ([1.0, 2.0, 3.0], (0, 0)), 
    ([10, 'a', None, 7], (10, 7)),
]


def _run_tests() -> None:
    for i, (inp, expected) in enumerate(TESTS, 1):
        out = sum_even_and_odd(inp)
        assert out == expected, f"Test {i} failed: in={inp} expected={expected} got={out}"
    print(f"All {len(TESTS)} tests passed.")


def _demo() -> None:
    examples = [
        [1, 2, 3, 4, 5],
        [10, 20, 33, 47, 0],
        [True, False, 2, 3],
    ]
    for ex in examples:
        even_sum, odd_sum = sum_even_and_odd(ex)
        print(f"input={ex} -> sum_even={even_sum}, sum_odd={odd_sum}")


if __name__ == "__main__":
    print("Running built-in tests...")
    _run_tests()
    print("\nDemo examples:")
    _demo()
