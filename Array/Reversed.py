def ReversedArray(arr, start, end) :
    while start < end :
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    
A = [1, 2, 3, 4, 5, 6]
print(A)
end = len(A)
ReversedArray(A, 0, (end - 1))
print(A)