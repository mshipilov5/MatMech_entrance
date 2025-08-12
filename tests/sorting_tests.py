from src.sorting import *

def test_insertion_sort_evens_inplace():
    # Test 1: Empty array
    assert insertion_sort_evens_inplace([]) == []

    # Test 2: Single odd element
    assert insertion_sort_evens_inplace([7]) == [7]

    # Test 3: Single even element
    assert insertion_sort_evens_inplace([4]) == [4]

    # Test 4: Only odd numbers
    assert insertion_sort_evens_inplace([3, 1, 7, 9]) == [3, 1, 7, 9]

    # Test 5: Only even numbers
    assert insertion_sort_evens_inplace([8, 2, 6, 4]) == [2, 4, 6, 8]

    # Test 6: Mixed elements
    assert insertion_sort_evens_inplace([5, 2, 8, 1, 6]) == [5, 2, 6, 1, 8]

    # Test 7: Even numbers already sorted
    assert insertion_sort_evens_inplace([3, 2, 4, 7, 6]) == [3, 2, 4, 7, 6]

    # Test 8: Even numbers in reverse order
    assert insertion_sort_evens_inplace([10, 8, 3, 6, 2]) == [2, 6, 3, 8, 10]

    # Test 9: Repeated even numbers
    assert insertion_sort_evens_inplace([4, 2, 4, 1, 2]) == [2, 2, 4, 1, 4]

    # Test 10: Negative even numbers
    assert insertion_sort_evens_inplace([0, -4, 3, -2, 5]) == [-4, -2, 3, 0, 5]

    # Test 11: All zeros
    assert insertion_sort_evens_inplace([0, 0, 0]) == [0, 0, 0]

    # Test 12: Non-integer values
    assert insertion_sort_evens_inplace([5, 2.5, 4, 1.0]) == [5, 2.5, 4, 1.0]

    print("All tests passed successfully!")


test_insertion_sort_evens_inplace()