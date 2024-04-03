def machine_epsilon(b: int, p: int) -> float:
    return b ** (1 - p)

print(f'{machine_epsilon(2, 11)}')