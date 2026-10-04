def bubble_sort(A):
    n = len(A)
    for i in range(1,n):
        for j in range(n-i):
            if A[j] > A[j+1]:
                A[j] , A[j+1] = A[j+1] , A[j]

    return A
            


AA = [69, 10, 30, 2, 16, 8, 31, 22]

print(bubble_sort(AA))
