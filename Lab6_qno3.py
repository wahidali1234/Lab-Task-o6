def longest_subarray_sum(arr, K):
   
    sum_table = {}
    max_length = 0
    current_sum = 0

    for i, num in enumerate(arr):
        
        current_sum += num

        if current_sum == K:
            max_length = i + 1

        if current_sum - K in sum_table:
            max_length = max(max_length, i - sum_table[current_sum - K])

        if current_sum not in sum_table:
            sum_table[current_sum] = i

    return max_length

array = [10, 5, 2, 7, 1, 9]
target_sum = 15
result = longest_subarray_sum(array, target_sum)
print(result)