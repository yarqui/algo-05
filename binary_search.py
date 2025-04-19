from typing import List, Tuple, Optional


def binary_search(arr: List[float], x: float) -> Tuple[int, Optional[float]]:
    """
    Perform binary search on a sorted array with fractional numbers.

    Returns:
        Tuple[int, Optional[float]]: A tuple containing:
            - The number of iterations performed during the search.
            - The smallest element in the list that is greater than or equal to `x` (upper bound),
              or None if no such element exists.
    """
    count = low = 0
    high = len(arr) - 1
    upper_bound = None

    while low <= high:
        mid = (low + high) // 2
        count += 1

        if x < arr[mid]:
            upper_bound = arr[mid]
            high = mid - 1
        elif x > arr[mid]:
            low = mid + 1
        else:
            return count, arr[mid]

    return count, upper_bound


if __name__ == "__main__":
    array = [10.9, 10.11, 10.13, 10.13, 10.14, 10.15, 10.16, 10.17]
    NUMBER = 10.13

    result = binary_search(array, NUMBER)
    print("result:", result)
