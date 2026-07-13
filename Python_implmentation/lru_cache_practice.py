
from functools import lru_cache

@lru_cache(maxsize=128)
def finding_sq(number : int) -> int:
    """
    Function to find the square of a number using LRU cache for optimization.

    Args:
    number (int): The number to find the square of.

    Returns:
    int: The square of the input number.
    """
    print(f"Calculating square of {number}")
    return number * number


def main():
    # Test the finding_sq function with some numbers
    test_numbers = [2, 3, 4, 5, 2, 5, 7,]

    for num in test_numbers:
        result = finding_sq(num)
        print(f"The square of {num} is {result}")


if __name__ == "__main__":
    main()