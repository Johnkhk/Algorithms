"""
May need to review when the time comes.
1. need to know how to implement the random quickselect from scartch
2. need to know how to implement partition,select,quicksort from scratch
"""
import random
def select(left, right, k_smallest):
    """
    Returns the k-th smallest element of list within left..right
    """
    if left == right:       # If the list contains only one element,
        return nums[left]   # return that element
    
    # select a random pivot_index between 
    pivot_index = random.randint(left, right)     
                    
    # find the pivot position in a sorted list 
    # pivot_index = partition(left, right, pivot_index)  
    pivot_index = partition(nums,left, right) # Min doesnt use random
    
    # the pivot is in its final sorted position
    if k_smallest == pivot_index:
            return nums[k_smallest]
    # go left
    elif k_smallest < pivot_index:
        return select(left, pivot_index - 1, k_smallest)
    # go right
    else:
        return select(pivot_index + 1, right, k_smallest)

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



"""
# random partition
def partition(left, right, pivot_index):
    pivot = nums[pivot_index]
    # 1. move pivot to end
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
    
    # 2. move all smaller elements to the left
    store_index = left
    for i in range(left, right):
        if nums[i] < pivot:
            nums[store_index], nums[i] = nums[i], nums[store_index]
            store_index += 1

    # 3. move pivot to its final place
    nums[right], nums[store_index] = nums[store_index], nums[right]  
    
    return store_index

"""