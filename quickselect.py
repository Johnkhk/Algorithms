def partition(arr, l, r):
    """
    input: r is the current pivot
    output: returns index of sorted pivot
    """
    x = arr[r]
    i = l
    for j in range(l, r):
          
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
              
    arr[i], arr[r] = arr[r], arr[i]
    return i


nums =[3,2,5,4,1,23,11]
ans = partition(nums,0,len(nums)-1)
print(ans,nums)