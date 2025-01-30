import random

# Deterministic Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]  # Choose the last element as the pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

# Randomized Quicksort
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)  # Randomly choose a pivot
    pivot = arr[pivot_index]
    left = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
    right = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]
    return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)

# Function to accept user input for the array
def accept_input():
    arr = input("Enter the elements of the array (space-separated): ").strip().split()
    arr = [int(x) for x in arr]  # Convert input strings to integers
    return arr

# Main program
if __name__ == "__main__":
    # Accept user input
    arr = accept_input()
    print("Original Array:", arr)

    # Sort using Deterministic Quicksort
    sorted_arr_deterministic = quicksort(arr.copy())
    print("Sorted Array (Deterministic Quicksort):", sorted_arr_deterministic)

    # Sort using Randomized Quicksort
    sorted_arr_randomized = randomized_quicksort(arr.copy())
    print("Sorted Array (Randomized Quicksort):", sorted_arr_randomized)