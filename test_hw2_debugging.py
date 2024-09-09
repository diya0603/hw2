import hw2_debugging

def test_merge_sort_random():
    array = [3,8,5,1,9,3]
    assert hw2_debugging.merge_sort(array) == [1,3,3,5,8,9]

def test_sorted_array():
    sorted_array = [1,3,5,7,9]
    assert hw2_debugging.merge_sort(sorted_array) == sorted_array

def test_reverse_sorted_array():
    array = [9,6,5,4,2,1]
    assert hw2_debugging.merge_sort(array) == [1,2,4,5,6,9]
