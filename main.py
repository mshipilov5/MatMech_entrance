from src.sorting import insertion_sort_evens_inplace


def main():
    print("Enter numbers one by one (press Enter after each number):")
    print("When finished, press Enter on an empty line to process the sorting.")

    arr = []
    while True:
        line = input()
        if line == "":
            break
        try:
            num = int(line)
            arr.append(num)
        except ValueError:
            print("Please enter a valid integer or empty line to finish.")

    print("\nOriginal array:", arr)
    sorted_arr = insertion_sort_evens_inplace(arr.copy())
    print("Array with even numbers sorted (odds remain in place):", sorted_arr)


if __name__ == "__main__":
    main()