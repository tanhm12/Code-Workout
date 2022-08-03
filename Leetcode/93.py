def restoreIpAddresses(s: str):
    def is_valid(ip_part):
        if 0<=int(ip_part)<=255:
            return True
        else:
            return False
    res = []
    current = [None for _ in range(4)]
    def find(s, sid, current_part):
        if current_part == 4 or sid >len(s):
            if sid == len(s):
                res.append(".".join([i for i in current]))
            return 
        for i in range(sid+1, min(sid + 4, len(s) + 1)):
            part = s[sid:i]
            if is_valid(part):
                prev_current_part = current[current_part]
                current[current_part] = part
                find(s, i, current_part + 1)
                current[current_part] = prev_current_part
                if part == '0':
                    break
    
    find(s, 0, 0)
    return res


ip = "1111234"
ip = "101023"
print(restoreIpAddresses(ip))

"""["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]"""