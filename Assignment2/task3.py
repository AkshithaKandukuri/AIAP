import math
import argparse
import sys


def area_circle(radius: float) -> float:
    return math.pi * radius * radius


def area_rectangle(length: float, width: float) -> float:
    return length * width

def area_square(side: float) -> float:
    return side * side


def area_triangle(base: float, height: float) -> float:
    return 0.5 * base * height


def area_trapezoid(a: float, b: float, height: float) -> float:
    return 0.5 * (a + b) * height


def area_ellipse(a: float, b: float) -> float:
    return math.pi * a * b


def _parse_positive(value: str) -> float:
    try:
        v = float(value)
    except ValueError:
        raise ValueError(f"invalid number: {value!r}")
    if v <= 0:
        raise ValueError(f"value must be positive: {value}")
    return v


def get_area_from_user() -> float:
    """Interactively asks the user to pick a shape and supply dimensions.
    Returns the computed area as a float. If the user types 'q' or 'quit', raises SystemExit.
    """
    print("Area calculator — type 'q' at any prompt to quit")
    shape_map = {
        "circle": (area_circle, ("radius",)),
        "rectangle": (area_rectangle, ("length", "width")),
        "square": (area_square, ("side",)),
        "triangle": (area_triangle, ("base", "height")),
        "trapezoid": (area_trapezoid, ("a (base1)", "b (base2)", "height")),
        "ellipse": (area_ellipse, ("a (semi-major)", "b (semi-minor)")),
    }

    while True:
        shapes_list = ", ".join(sorted(shape_map.keys()))
        choice = input(f"Choose a shape ({shapes_list}): ").strip().lower()
        if choice in ("q", "quit", "exit"):
            raise SystemExit(0)
        if choice not in shape_map:
            print("Unknown shape — try again.")
            continue
        func, params = shape_map[choice]
        values = []
        try:
            for p in params:
                raw = input(f"Enter {p}: ").strip()
                if raw.lower() in ("q", "quit", "exit"):
                    raise SystemExit(0)
                values.append(_parse_positive(raw))
        except ValueError as e:
            print("Invalid input:", e)
            print("Let's start over.\n")
            continue
        area = func(*values)
        print(f"Area of {choice}: {area:.6f}\n")
        # Ask to compute another
        again = input("Compute another? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            return area


def demo() -> None:
    examples = [
        ("circle", (3.0,), area_circle(3.0)),
        ("rectangle", (4.0, 5.0), area_rectangle(4.0, 5.0)),
        ("square", (2.5,), area_square(2.5)),
        ("triangle", (3.0, 4.0), area_triangle(3.0, 4.0)),
        ("trapezoid", (3.0, 5.0, 4.0), area_trapezoid(3.0, 5.0, 4.0)),
        ("ellipse", (2.0, 1.0), area_ellipse(2.0, 1.0)),
    ]
    print("Demo: example area calculations")
    for name, args, result in examples:
        args_str = ", ".join(str(x) for x in args)
        print(f"- {name:<9} ({args_str}) -> {result:.6f}")


def _build_cli():
    p = argparse.ArgumentParser(description="Area calculator (interactive or demo)")
    p.add_argument("--demo", action="store_true", help="Run demo examples and exit")
    p.add_argument("--no-input", action="store_true", help="Run and exit without interactive prompts (alias for --demo)")
    return p


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = _build_cli()
    args = parser.parse_args(argv)
    if args.demo or args.no_input:
        demo()
        return 0
    try:
        get_area_from_user()
    except SystemExit as e:
        # Normal exit via 'q' or ctrl-c
        return 0

def _name_():
    if _name_ == "_main_":
        raise SystemExit(main())