def acmTeam(topics):
    # topics = [set([i for i in range(1, len(t)+1) if t[i-1]=='1']) for t in topics]
    topics = [int(t, 2) for t in topics]
    
    res = [0, 0]  # max subjects, num team
    
    for i in range(len(topics)-1):
        for j in range(i+1, len(topics)):
            current_subject = topics[i] | topics[j]
            current_num_subject = str(bin(current_subject)).count('1')
            if current_num_subject > res[0]:
                res[0] = current_num_subject
                res[1] = 1
            elif current_num_subject == res[0]:
                res[1] += 1
    
    return res
    
    