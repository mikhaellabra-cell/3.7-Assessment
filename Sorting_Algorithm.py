"""
Assessment 3.7: Sorting Algorithms
Name: Mikhael S. Labra | BSIT-2A | CC204 Data Structure and Algorithm

Sorting method: Bubble Sort
The user types a full name. The letters become an array:
    - symbols, spaces and numbers are left out
    - duplicate letters are discarded (the first one is kept)
Two arrays are shown: the unsorted array and the sorted array.
"""


def make_array(full_name):
    """Build the unsorted array: letters only, no duplicates."""
    array = []
    for ch in full_name.upper():
        if ch.isalpha() and ch not in array:   # skip symbols and duplicates
            array.append(ch)
    return array


def bubble_sort(array):
    """Bubble Sort: compare neighbors and swap them if they are in the wrong order."""
    data = array.copy()                  # copy, so the unsorted array stays unchanged
    n = len(data)
    passes = []
    for p in range(1, n):
        swaps = 0
        for i in range(n - p):           # the last p letters are already in place
            if data[i] > data[i + 1]:    # wrong order -> swap
                data[i], data[i + 1] = data[i + 1], data[i]
                swaps += 1
        passes.append((p, swaps, data.copy()))
        if swaps == 0:                   # no swaps -> already sorted, stop early
            break
    return data, passes


if __name__ == "__main__":
    full_name = input("Enter your full name (e.g. Mikhael S. Labra): ")
    unsorted_array = make_array(full_name)

    if not unsorted_array:
        print("No letters were entered.")
    else:
        sorted_array, passes = bubble_sort(unsorted_array)

        print("\nUnsorted array:", unsorted_array)
        print("\nBubble Sort passes:")
        for p, swaps, snapshot in passes:
            print(f"  Pass {p}: {snapshot}  (swaps: {swaps})")
        print("\nSorted array:  ", sorted_array)