def insertion_sort(A):

    n = len(A)

    for i in range (1, n):   
        key = A[i]  
        j = i-1

        while key < A[j] and j>= 0:
            A[j+1] = A[j]
            j -= 1
            
        A[j+1] = key

    return A

        







A = [69, 10, 30, 2, 16, 8, 31, 22]
print(insertion_sort(A))
  