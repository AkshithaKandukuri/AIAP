def _prime(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError(f"_prime() expects an int, got {type(n).__name__}")
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    test_values = [
        -1, 0, 1, 2, 3, 4, 16, 17, 18, 19,
        20, 23, 24, 29, 97, 100, 101, 1024, 104729  
    ]

    print("n -> is_prime")
    for v in test_values:
        print(f"{v:6} -> { _prime(v) }")

    assert not _prime(-7)
    assert not _prime(0)
    assert not _prime(1)
    assert _prime(2)
    assert _prime(3)
    assert not _prime(4)
    assert _prime(97)
    assert _prime(104729)
    print("Basic tests passed.")