def binary_search(arr, start, end, target):
    if start <= end:
        middle = (start + end) // 2
        print(start,middle, end)
        if arr[middle] == target:
            # found
            return middle

        if arr[middle] > target:
            return binary_search (arr, start, middle-1, target)

        if arr[middle] < target:
            return binary_search(arr, middle+1, end, target)
    # not found
    return -1  


def search(arr, key):
    return binary_search(arr, 0, len(arr)-1, key)



def kthElement(arr1: list, arr2: list, k: int):
    """
    Function that finds the kth element of two sorted arrays when they are combined
    This solution is based on the fact that the kth element must be contained within
    array1[0: point1] and array2[0: point2] if point1+point2 = k. We can cut the arrays in half
    until array1[point1] < array2[point2+1] and array2[point2] < array1[point1+1]
    """
    n = len(arr1)
    m = len(arr2)
    # conquer: solve the sub-problems with all of the base cases
    if n ==1 or m == 1:
        #Make arr 1 the array with only one element and n = 1
        if m == 1:
            place_holder = arr1
            arr1 = arr2
            arr2 = place_holder
            m = n
            n = 1
        if k == 1:
            return min(arr1[0], arr2[0])
        if k == 2:
            return maximum(arr[0], arr2[0])
        else: #if k is greater than 2
            if arr2[k-1] < arr[0]:
                return arr2[k-1] #this is the kth element
            else:
                return max(arr[0],arr2[k-2]) #the kth is the larger of the two
    #divide/ break down the arrays into smaller more manageable sub parts
    middle1 = (n-1)//2
    middle2 = (m-1)//2
    if k > middle1+middle2+1:
    # we don’t need to consider elements smaller than the largest of the other array, adjust k and arrays accordingly
        if arr1[middle2]> arr2[middle2]:
        # reduce the size of the second array by half
            return kthElement(arr1, arr2[middle2+1:], k - middle2 -1)
        else:
            #reduce the size of the first array by half
            return kthElement(arr1[middle1+1:], arr2, k - middle1 - 1)
    else: # k is smaller or equal to the number elements contained in the first halves.
        if arr1[middle2]> arr2[middle2]:
            # reduce the size of the first array by half
            return kthElement(arr1[:middle1+1], arr2, k)
        else:
            # reduce the size of the second array by halfReturn Def kthElement(arr1, arr2[:middle1+1], k)
            return kthElement(arr1, arr2[:middle2],k)


if __name__ == '__main__':

    arr1 = [1,2,3,5,6]
    arr2= [3,4,5,6,7]
    k= 5

    print(kthElement(arr1, arr2, 5))