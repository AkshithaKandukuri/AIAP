def calc(x, y):
    # add
    a = x + y
    # mult
    b = x * y
    # div
    c = x / y
    return a, b, c
def calc(x: float, y: float) -> tuple[float, float, float]:
    """
    Perform basic arithmetic operations on two numbers.

    Parameters
    ----------
    x : float
        The first input number.
    y : float
        The second input number. Must be non-zero to avoid division errors.

    Returns
    -------
    tuple of float
        A tuple containing:
        - Sum of x and y
        - Product of x and y
        - Quotient of x divided by y

    Raises
    ------
    ZeroDivisionError
        If y is zero when attempting division.
    """
    a = x + y
    b = x * y
    c = x / y
    return a, b, c