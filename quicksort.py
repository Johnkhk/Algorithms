from quickselect import partition
### My try Implementation ###

def quicksort(arr,l,r):
    """
    (l,r) Determine part of array that wants to be sorted. (Default is start and end)
    """
    if l>=r:
        return
    idx = partition(arr,l,r) # quickselect

    # recurse for left & right
    quicksort(arr,l,idx-1)
    quicksort(arr,idx+1,r)
arr=[3,1,2,78,3,2,1,2,99]

quicksort(arr,0,len(arr)-1)
print(arr)



