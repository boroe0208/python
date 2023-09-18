# get a string of numbers from the user and convert it to a list of those numbers in the order it was writen in  # noqa: E501

num_list = input('what is your list of numbers you want to sort? ')


# sort the list of numbers from least to greatest

def insertion_sort(list_of_numbers):

    for i in range(1, len(list_of_numbers)):
        j = i
    while list_of_numbers[j - 1] > list_of_numbers[j] and j > 0:
        list_of_numbers[j - 1], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[j - 1]
        j -= 1


insertion_sort(num_list)
