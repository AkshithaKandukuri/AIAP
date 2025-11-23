import argparse
import sys
from typing import Iterable, List


def sum_of_squares(numbers: Iterable[float]) -> float:
    """Return the sum of squares for the given iterable of numbers."""
    return sum((x * x) for x in numbers)


def sum_of_squares_range(n: int) -> int:
    """Return sum_{i=1..n} i^2 using closed-form formula.
    Formula: n(n+1)(2n+1)/6
    """
    return n * (n + 1) * (2 * n + 1) // 6


def _parse_float_list(s: str) -> List[float]:
    """Parse a string of numbers separated by commas or whitespace into a list of floats.
    Raises ValueError on invalid input or if any value is not finite.
    """
    if not s.strip():
        raise ValueError("empty input")
    # Normalize commas to whitespace then split
    parts = s.replace(",", " ").split()
    nums: List[float] = []
    for p in parts:
        try:
            v = float(p)
        except ValueError:
            raise ValueError(f"invalid number: {p!r}")
        if not (v == v):  # NaN check
            raise ValueError(f"invalid numeric value: {p!r}")
        nums.append(v)
    if not nums:
        raise ValueError("no numbers parsed")
    return nums


def get_sum_of_squares_from_user() -> float:
    """Interactive prompt that asks the user for input mode and dimensions
    Returns the computed sum of squares. Enter 'q' at any prompt to quit.
    """
    print("Sum of squares calculator — type 'q' at any prompt to quit")
    while True:
        mode = input("Choose mode: 'range' (1..n) or 'list' (numbers): ").strip().lower()
        if mode in ("q", "quit", "exit"):
            raise SystemExit(0)
        if mode not in ("range", "list"):
            print("Unknown mode — enter 'range' or 'list'.")
            continue
        try:
            if mode == "range":
                raw = input("Enter positive integer n: ").strip()
                if raw.lower() in ("q", "quit", "exit"):
                    raise SystemExit(0)
                n = int(raw)
                if n <= 0:
                    raise ValueError("n must be a positive integer")
                result = float(sum_of_squares_range(n))
                print(f"Sum of squares 1..{n} = {result:.6f}")
                return result
            else:  # list
                raw = input("Enter numbers separated by space or comma: ").strip()
                if raw.lower() in ("q", "quit", "exit"):
                    raise SystemExit(0)
                nums = _parse_float_list(raw)
                result = sum_of_squares(nums)
                print(f"Sum of squares = {result:.6f}")
                return result
        except ValueError as e:
            print("Invalid input:", e)
            print("Let's try again.\n")


def demo() -> None:
    examples = [
        ("range", 5, sum_of_squares_range(5)),  # 1^2+...+5^2 = 55
        ("list", [1, 2, 3], sum_of_squares([1, 2, 3])),
        ("list", [2.5, -1.5], sum_of_squares([2.5, -1.5])),
    ]
    print("Demo: sum of squares examples")
    for typ, inp, res in examples:
        if typ == "range":
            print(f"- range 1..{inp} -> {res:.6f}")
        else:
            print(f"- list {inp} -> {res:.6f}")


def _build_cli():
    p = argparse.ArgumentParser(description="Sum of squares calculator (interactive or demo)")
    p.add_argument("--demo", action="store_true", help="Run demo examples and exit")
    return p


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = _build_cli()
    args = parser.parse_args(argv)
    if args.demo:
        demo()
        return 0
    try:
        get_sum_of_squares_from_user()
    except SystemExit:
        return 0

def _name_():
    if _name_ == "_main_":
        raise SystemExit(main())