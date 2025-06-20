def main():
     #values that require sorting
    unsorted_list=[1,2,3,3,79,54,67]

    # prints out sorted array
    result = bubble_sort(unsorted_list)
    print(result)


    # # prints out reverse, sorted array
    # reverse_result = bubble_sort_reverse(unsorted_list)
    # print(reverse_result)

def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort

    #stores length of the array to check number of iterations the sort has to go through
    unsorted_list_length=len(unsorted_list)

    for i in range(unsorted_list_length-1):
        for j in range(unsorted_list_length-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                temp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j+1]
                unsorted_list[j+1]=temp

    print("Sorted array:", unsorted_list)
    return unsorted_list



# def bubble_sort_reverse(unsorted_list):
#     # Sort first, then reverse
#     sorted_list = bubble_sort(unsorted_list)
#     return sorted_list[::-1]




# def bubble_sort_duplicates():
#     pass

# main()