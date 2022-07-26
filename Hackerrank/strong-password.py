import re

number = re.compile("[0-9]")
lowercase = re.compile("[a-z]")
uppercase = re.compile("[A-Z]")
special = re.compile("[!@#\$%\^&\*\(\)\-\+]")
conditions = [number, lowercase, uppercase, special]

def minimumNumber(n, password):
    minimum = len(conditions)
    total_len = 0
    for condition in conditions:
        temp = len(condition.findall(password))
        total_len += temp
        # print(temp)
        minimum -= min(temp, 1)
        
    return minimum + 6 - min(total_len+minimum, 6)