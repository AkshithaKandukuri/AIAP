def calculate_average(scores):
    """Return the average of a list of scores."""
    return sum(scores) / len(scores)


def find_highest(scores):
    """Return the highest score."""
    highest = scores[0]
    for s in scores:
        if s > highest:
            highest = s
    return highest


def find_lowest(scores):
    """Return the lowest score."""
    lowest = scores[0]
    for s in scores:
        if s < lowest:
            lowest = s
    return lowest


def process_scores(scores):
    """Process and display score statistics."""
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)

    print("\n--- Score Statistics ---")
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)


# -------- INPUT FUNCTION -------- #

def main():
    raw = input("Enter scores (comma-separated numbers): ")

    try:
        scores = [float(x.strip()) for x in raw.split(",") if x.strip()]
    except ValueError:
        print("Invalid input! Please enter only numbers.")
        return

    if len(scores) == 0:
        print("No scores provided.")
        return

    process_scores(scores)


# Run the program
main()