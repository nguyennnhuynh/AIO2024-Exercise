def max_sliding_window(nums, k):
    sliding_window = []
    result_list = []
    
    for i in range(len(nums) - k + 1):
        sliding_window = nums[i:i + k]
        print(sliding_window)
        max_element = max(sliding_window)
        result_list.append(max_element)
    
    return result_list


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
assert max_sliding_window(num_list, k) == [5, 5, 5, 5, 10, 12, 33, 33]