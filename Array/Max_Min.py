# using per defined function

def findMin(arr, n) :
    temp = arr[0]
    for i in range(1,n) :
        temp = min(temp, arr[i])
    return temp

def findMax(arr, n) :
    temp = arr[0]
    for i in range(1,n) :
        temp = max(temp, arr[i])
    return temp

if __name__ == "__main__" :
    arr = [12, 1234, 45, 67, 1]
    n = len(arr)
    print("MIN:", findMin(arr, n))
    print("MAX:", findMax(arr, n))



# use library: use min(arr) and max(arr)