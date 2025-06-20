def selection_sort(arr):
    # TODO: Implement selection sort
    arr_length = len(arr)
    for i in range(arr_length  -1):
        min_index = i
        for j in range(i+1, arr_length):
            if arr[j]<arr[min_index]:
                min_index = j

        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

    pass
