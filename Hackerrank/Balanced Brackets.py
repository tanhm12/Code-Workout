def  isBalanced(s):
    from queue import LifoQueue
    open_brackets = set([i for i in r'([{'])
    # close_brackes = set([i for i in r')]}'])
    
    open_to_close = {s[0]: s[1] for s in [r'()', r'{}', r'[]']}
    
    checker = LifoQueue(len(s))
    
    for c in s:
        if c in open_brackets:
            checker.put(c)
        else:
            if checker.empty():
                return "NO"
            last_open_bracket = checker.get()
            if open_to_close[last_open_bracket] != c:
                return "NO"
    
    if checker.empty():
        return "YES"

    return "NO"

s = r"{[()]}"
s = r"{[(])}"
s = r"{{[[(())]]}}"

print(isBalanced(s))
    