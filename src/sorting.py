def insertion_sort_evens_inplace(arr):
    even_idx = [i for i, v in enumerate(arr) if v % 2 == 0]
    for k in range(1, len(even_idx)):
        i = even_idx[k]
        key = arr[i]
        j = k - 1
        while j >= 0 and arr[even_idx[j]] > key:
            arr[even_idx[j + 1]] = arr[even_idx[j]]
            j -= 1
        arr[even_idx[j + 1]] = key
    return arr

# ---- пример использования / решение в формате задачи ----
if __name__ == "__main__":
    # ввод: сначала n, затем n целых чисел в одной строке
    try:
        n = int(input().strip())
        arr = list(map(int, input().split()))
        assert len(arr) == n
    except Exception:
        # на случай если дадут только массив
        arr = list(map(int, input().split()))
    insertion_sort_evens_inplace(arr)
    print(*arr)