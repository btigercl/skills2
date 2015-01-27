def sum_zero(list1):
    """Return list of x,y number pair lists from a list where x+y==0

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

        
    For example:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together, 
    that's fine, too:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 0, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
    # sort list
    # discover pairs that are +/- and ==0
    # insert into dictionary, as key --> to make sure each unique (not duplicated)
        # iterate through list
        # 
    # return list of the keys
    list1_sort = sorted(list1)
    working_dict={}
    for numbers in list1_sort:
        for nums in list1_sort:
            if numbers+nums==0:
                if (nums, numbers) not in working_dict: 
                    working_dict[(numbers,nums)] = ""

    return_list = working_dict
    print return_list
    # list1_sort = sorted(list1)
    # working_dict = {}
    # return_list = []
    # for num in list1_sort:
    #     if (-num) in list1_sort:
    #         key = [num, -num]
    #         working_dict[key] = working_dict.get(key, 0) + 1
    # print working_dict
    # return word_list

sum_zero([1, 2, 3, -2, -1, 1, 0, 1, 0])