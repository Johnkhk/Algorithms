def partition(arr, l, r):
    """
    input: r is the pivot
    output: returns index of sorted pivot, also puts pivot in its correct place
    """
    x = arr[r] # pivot element
    i = l # left pointer (looks for element > pivot)
    for j in range(l, r): # j is right pointer (looks for element < pivot)
        if arr[j] <= x: # when such an element is found, swap
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # swap i with pivot
    arr[i], arr[r] = arr[r], arr[i]
    return i

if __name__ == "__main__":
    nums =[3,2,5,4,1,23,11] # -> [3, 2, 5, 4, 1, 11, 23] # -> 11 is now at index 5
    ans = partition(nums,0,len(nums)-1)
    print(ans,nums)