'''Linear Search Dictionary'''


def linear_search_dictionary(dic, target_value):
    '''Linear Search Function'''
    for key, value in dic.items():
        if value == target_value:
            print(f'Found at key {key}')
            return key
    print('Target is not in the dictionary')
    return -1


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
