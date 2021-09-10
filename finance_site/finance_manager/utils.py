from typing import Optional

def fibonacci(n: int) -> Optional[int]:
    """
    Function to calculate n'th fibonacci number.
    Examples:
        fibonacci(0) -> 0
        fibonacci(7) -> 13
        fibonacci(-1) -> None
        fibonacci(N) = fibonacci(N-1) + fibonacci(N-2)
    """
    memory = [0, 1]

    # Case for n out of function input range
    if n < 0:
        return None

    # Perform summation of memory members to get n == 1
    while n > 1:
        memory[0], memory[1] = memory[1], memory[0] + memory[1]
        n -= 1

    # Case for n == 1 and n == 0  
    return memory[n]

    