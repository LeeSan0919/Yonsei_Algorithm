''' def selection_sort(arr):
    n = len(arr)
    arr = [69, 10, 30, 2, 16, 8, 31, 22]
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    print("Sorted array:", arr)
    return arr '''

def selection_sort(A):

    n = len(A)

    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]

    return A

AA = [69, 10, 30, 2, 16, 8, 31, 22]

print(selection_sort(AA))

