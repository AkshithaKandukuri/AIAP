from __future__ import annotations
from typing import List, Tuple, Dict

TARIFFS: Dict[str, Dict] = {
    "residential": {
        "slabs": [(100, 1.50), (100, 3.00), (300, 4.50), (float("inf"), 6.00)],
        "fixed_charges": 50.0,
        "customer_charges": 25.0,
        "duty_percent": 5.0,  # percent of EC
    },
    "commercial": {
        "slabs": [(100, 3.00), (100, 5.00), (300, 6.50), (float("inf"), 8.00)],
        "fixed_charges": 100.0,
        "customer_charges": 50.0,
        "duty_percent": 8.0,
    },
}


def parse_float_input(prompt: str) -> float:
    while True:
        try:
            raw = input(prompt).strip()
            val = float(raw)
            return val
        except ValueError:
            print("Invalid number. Please enter a numeric value.")


def parse_customer_type(prompt: str) -> str:
    while True:
        raw = input(prompt).strip().lower()
        if raw in TARIFFS:
            return raw
        print(f"Unknown customer type '{raw}'. Supported: {', '.join(TARIFFS.keys())}.")


def compute_energy_charges(units: int, slabs: List[Tuple[float, float]]) -> float:
    remaining = units
    ec = 0.0
    for slab_size, rate in slabs:
        if remaining <= 0:
            break
        take = min(remaining, slab_size)
        ec += take * rate
        remaining -= take
    return ec


def calculate_bill(pu: float, cu: float, customer_type: str) -> Dict[str, float]:
    if cu < pu:
        raise ValueError("Current reading (CU) must be >= Previous reading (PU)")
    units = int(round(cu - pu))
    if units < 0:
        units = 0

    tariff = TARIFFS[customer_type]
    ec = compute_energy_charges(units, tariff["slabs"])  
    fc = float(tariff["fixed_charges"])  
    cc = float(tariff["customer_charges"])  
    ed = ec * (tariff["duty_percent"] / 100.0)
    bill = ec + fc + cc + ed

    return {
        "units": units,
        "EC": round(ec, 2),
        "FC": round(fc, 2),
        "CC": round(cc, 2),
        "ED": round(ed, 2),
        "bill": round(bill, 2),
    }


def format_and_print(result: Dict[str, float]) -> None:
    print("\n--- Bill Details ---")
    print(f"Units consumed: {result['units']}")
    print(f"EC: {result['EC']:.2f}")
    print(f"FC: {result['FC']:.2f}")
    print(f"CC: {result['CC']:.2f}")
    print(f"ED: {result['ED']:.2f}")
    print(f"Bill amount: {result['bill']:.2f}")


def _demo_examples() -> None:
    examples = [
        # (PU, CU, type)
        (1000, 1100, "residential"),
        (2000, 2700, "commercial"),
        (500, 505, "residential"),
    ]
    for pu, cu, t in examples:
        r = calculate_bill(float(pu), float(cu), t)
        print(f"Example PU={pu}, CU={cu}, type={t} -> Units={r['units']}, Bill={r['bill']:.2f}")


def main() -> None:
    print("Electricity Bill Calculator")
    print("(reads Previous reading (PU), Current reading (CU) and customer type)")
    print("Supported customer types:", ", ".join(TARIFFS.keys()))

    pu = parse_float_input("Enter previous reading (PU): ")
    cu = parse_float_input("Enter current reading (CU): ")
    customer_type = parse_customer_type("Enter customer type: ")

    try:
        bill_parts = calculate_bill(pu, cu, customer_type)
    except ValueError as exc:
        print("Error:", exc)
        return

    format_and_print(bill_parts)

if __name__ == "__main__":
    main()