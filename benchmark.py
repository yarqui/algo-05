from timeit import timeit
from typing import Callable


def measure_execution_time(func: Callable, main_string, substring):
    execution_time = timeit(lambda: func(main_string, substring), number=1)

    print(
        f"Execution time of {func.__name__} for '{substring}': ",
        execution_time,
    )


# KMP
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if main_string[i] == pattern[j]:
            i += 1
            j += 1

        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1


# Boyer Moore
def build_shift_table(pattern):
    table = {}
    length = len(pattern)

    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1

    table.setdefault(pattern[-1], length)

    return table


def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            return i

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return -1


# Rabin-Karp
def polynomial_hash(s, base=256, modulus=(10**9 + 9)):
    n = len(s)
    hash_value = 0

    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus

    return hash_value


def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)

    base = 256
    modulus = 10**9 + 9

    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    h_multiplier = pow(base, substring_length - 1) % modulus

    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if substring == main_string[i : i + substring_length]:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (
                current_slice_hash - ord(main_string[i]) * h_multiplier
            ) % modulus

            current_slice_hash = (
                current_slice_hash * base + ord(main_string[i + substring_length])
            ) % modulus

            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


def run_tests(file_path: str, present_sub: str, absent_sub: str):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    print(f"\nTesting on file: {file_path}")
    substrings = [(present_sub, "present"), (absent_sub, "absent")]
    algorithms = [kmp_search, boyer_moore_search, rabin_karp_search]

    for func in algorithms:
        for substring, label in substrings:
            print(f"\nTesting {func.__name__} with {label} substring:")
            measure_execution_time(func, text, substring)


def main():
    absent_str = "we're going to build a wall"
    present_str_art1 = "int elementToSearch"
    present_str_art2 = "linked list"

    run_tests("article 1.txt", present_str_art1, absent_str)
    run_tests("article 2.txt", present_str_art2, absent_str)


if __name__ == "__main__":
    main()
