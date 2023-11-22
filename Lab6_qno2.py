def count_frequencies(numbers):
   
    freq_dict = {}

    
    for num in numbers:
       
        freq_dict[num] = freq_dict.get(num, 0) + 1

    return freq_dict

numbers_list = [1, 2, 3, 1, 2, 4, 5, 1, 2, 3]
result_dict = count_frequencies(numbers_list)
print(result_dict)