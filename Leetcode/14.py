def longestCommonPrefix(strs):
    longest_str = ''
    
    for item in strs:
        if len(item) > len(longest_str):
            longest_str = item
    
    shortest_str = longest_str
    for item in strs:
        if len(item) < len(shortest_str):
            shortest_str = item
            
    for i in range(len(shortest_str)):
        char = longest_str[i]
        for item in strs:
            if item[i] != char:
                return shortest_str[:i]
    
    return shortest_str

print(longestCommonPrefix(strs = ["dog","racecar","car"]))
        
    
    