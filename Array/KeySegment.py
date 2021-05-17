def Finder(arr, x, k, n) :
    i = 0
    while i < n :
        
        j = 0
        while j < k :
            if arr[i + j] == x :
                break
            j += 1
        
        if j == k :
            return False
        
        i += k
    
    if i == n :
        return True

    j = i - k
    while i < n :
        if arr[j] == x:
            break
        j += 1

    if j == n :
        return False

    return True

if __name__ == "__main__" :
    arr = [5, 8, 7, 12, 14, 3, 9] 
    x, k = 8, 2
    n = len(arr)

    if(Finder(arr, x, k, n)) :
        print("Yes")
    else :
        print("No")
