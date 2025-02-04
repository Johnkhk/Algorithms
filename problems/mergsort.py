def merge_sort(arr):
    """
    Sort an array
    TC: O(nlogn)
    SC: O(n)
    """
    # base case (only 1 element in subproblem -> it's already sorted)
    if len(arr) ==1:
        return

    leftarr = arr[:len(arr)//2] # makes copies
    rightarr = arr[len(arr)//2:] # makes copies

    # recurse sub problems
    merge_sort(leftarr)
    merge_sort(rightarr)

    # merge the sorted lists
    i,j,k=0,0,0
    while i<len(leftarr) and j<len(rightarr):
        if leftarr[i]<rightarr[j]:
            arr[k] = leftarr[i]
            i+=1
        else:
            arr[k] = rightarr[j]
            j+=1
        k+=1

    #leftover is left
    while i<len(leftarr):
        arr[k]=leftarr[i]
        i+=1
        k+=1
    #leftover is right
    while j<len(rightarr):
        arr[k]=rightarr[j]
        j+=1
        k+=1

arr=[3,1,2,78,3,2,1,2,99]
merge_sort(arr)
print(arr)




