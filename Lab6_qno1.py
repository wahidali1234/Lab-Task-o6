def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    freq_table1 = {}
    freq_table2 = {}
    
    for char in str1:
        freq_table1[char] = freq_table1.get(char, 0) + 1

    for char in str2:
        freq_table2[char] = freq_table2.get(char, 0) + 1
   
    return freq_table1 == freq_table2

string1 = "Listen"
string2 = "Silent"
result = are_anagrams(string1, string2)
print(f"Are '{string1}' and '{string2}' anagrams? {result}")