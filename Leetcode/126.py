from typing import List


def findLadders(beginWord: str, endWord: str, wordList: List[str]):
    try: 
        wordList.remove(beginWord)
    except ValueError as e:
        pass
    def is_adjacent(s1, s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                if count  > 1:
                    return False
        if count == 1:
            return True
        else:
            return False

    from collections import defaultdict
    edges = defaultdict(set)
    for w in wordList:
        for w2 in wordList:
            if is_adjacent(w, w2):
                edges[w].add(w2)
                edges[w2].add(w)

    for w in wordList:
        if is_adjacent(beginWord, w):
            edges[beginWord].add(w)

    from queue import Queue
    q = Queue()
    q.put(beginWord)

    parents = defaultdict(set)
    check = {e: {e:False for e in edges} for e in edges}
    while not q.empty():
        e = q.get()

        for ne in edges[e]:
            if not check[e][ne]:
                parents[ne].add(e)
                check[e][ne] = True
                if ne != endWord:
                    q.put(ne)

    if len(parents[endWord] ) ==0 :
        return []
    
    all_res = []
    res = [None for i in range(len(edges))]
    res[0] = endWord
    def get_path(e, i):
        if e == beginWord:
            t = res[:i]
            t.reverse()
            all_res.append(t)
        elif e in parents and i < len(edges):
            prev_resi = res[i]
            for ne in parents[e]:
                res[i] = ne
                get_path(ne, i+1)
                res[i] = prev_resi
    
    get_path(endWord, 1)
    return all_res


def findLadders(beginWord: str, endWord: str, wordList: List[str]):
    try: 
        wordList.remove(beginWord)
    except ValueError as e:
        pass
    def is_adjacent(s1, s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                if count  > 1:
                    return False
        if count == 1:
            return True
        else:
            return False
        
    # print(len(wordList))
    
    from collections import defaultdict
    edges = defaultdict(set)
    for w in wordList:
        for w2 in wordList:
            if is_adjacent(w, w2):
                edges[w].add(w2)
                edges[w2].add(w)
                
    for w in wordList:
        if is_adjacent(beginWord, w):
            edges[beginWord].add(w)
    
    from queue import Queue
    q = Queue()
    q.put(beginWord)
    
    parents = defaultdict(set)
    check = {e: 501 for e in edges}
    check[beginWord] = 0
    while not q.empty():
        e = q.get()
        
        for ne in edges[e]:
            if check[e] < check[ne] - 1:
                # print(e, check[e], ne, check[ne])
                parents[ne] = set([e])
                check[ne] = check[e] + 1
                q.put(ne)
            elif check[e] == check[ne] - 1:
                parents[ne].add(e)
    
    
    # print(parents)
    if len(parents[endWord] ) == 0 :
        return []
    
    all_res = []
    res = [None for i in range(len(edges))]
    res[0] = endWord
    def get_path(e, i):
        if e == beginWord:
            t = res[:i]
            t.reverse()
            all_res.append(t)
        elif e in parents and i < len(edges):
            prev_resi = res[i]
            for ne in parents[e]:
                res[i] = ne
                get_path(ne, i+1)
                res[i] = prev_resi
    
    get_path(endWord, 1)
    return all_res
                    


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# beginWord = "a"
# endWord = "c"
# wordList = ["a","b","c"]

# beginWord = "red"
# endWord =  "tax"
# wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
beginWord = "aaaaa"
endWord = "ggggg"
wordList = ["aaaaa","caaaa","cbaaa","daaaa","dbaaa","eaaaa","ebaaa","faaaa","fbaaa","gaaaa","gbaaa","haaaa","hbaaa","iaaaa","ibaaa","jaaaa","jbaaa","kaaaa","kbaaa","laaaa","lbaaa","maaaa","mbaaa","naaaa","nbaaa","oaaaa","obaaa","paaaa","pbaaa","bbaaa","bbcaa","bbcba","bbdaa","bbdba","bbeaa","bbeba","bbfaa","bbfba","bbgaa","bbgba","bbhaa","bbhba","bbiaa","bbiba","bbjaa","bbjba","bbkaa","bbkba","bblaa","bblba","bbmaa","bbmba","bbnaa","bbnba","bboaa","bboba","bbpaa","bbpba","bbbba","abbba","acbba","dbbba","dcbba","ebbba","ecbba","fbbba","fcbba","gbbba","gcbba","hbbba","hcbba","ibbba","icbba","jbbba","jcbba","kbbba","kcbba","lbbba","lcbba","mbbba","mcbba","nbbba","ncbba","obbba","ocbba","pbbba","pcbba","ccbba","ccaba","ccaca","ccdba","ccdca","cceba","cceca","ccfba","ccfca","ccgba","ccgca","cchba","cchca","cciba","ccica","ccjba","ccjca","cckba","cckca","cclba","cclca","ccmba","ccmca","ccnba","ccnca","ccoba","ccoca","ccpba","ccpca","cccca","accca","adcca","bccca","bdcca","eccca","edcca","fccca","fdcca","gccca","gdcca","hccca","hdcca","iccca","idcca","jccca","jdcca","kccca","kdcca","lccca","ldcca","mccca","mdcca","nccca","ndcca","occca","odcca","pccca","pdcca","ddcca","ddaca","ddada","ddbca","ddbda","ddeca","ddeda","ddfca","ddfda","ddgca","ddgda","ddhca","ddhda","ddica","ddida","ddjca","ddjda","ddkca","ddkda","ddlca","ddlda","ddmca","ddmda","ddnca","ddnda","ddoca","ddoda","ddpca","ddpda","dddda","addda","aedda","bddda","bedda","cddda","cedda","fddda","fedda","gddda","gedda","hddda","hedda","iddda","iedda","jddda","jedda","kddda","kedda","lddda","ledda","mddda","medda","nddda","nedda","oddda","oedda","pddda","pedda","eedda","eeada","eeaea","eebda","eebea","eecda","eecea","eefda","eefea","eegda","eegea","eehda","eehea","eeida","eeiea","eejda","eejea","eekda","eekea","eelda","eelea","eemda","eemea","eenda","eenea","eeoda","eeoea","eepda","eepea","eeeea","ggggg","agggg","ahggg","bgggg","bhggg","cgggg","chggg","dgggg","dhggg","egggg","ehggg","fgggg","fhggg","igggg","ihggg","jgggg","jhggg","kgggg","khggg","lgggg","lhggg","mgggg","mhggg","ngggg","nhggg","ogggg","ohggg","pgggg","phggg","hhggg","hhagg","hhahg","hhbgg","hhbhg","hhcgg","hhchg","hhdgg","hhdhg","hhegg","hhehg","hhfgg","hhfhg","hhigg","hhihg","hhjgg","hhjhg","hhkgg","hhkhg","hhlgg","hhlhg","hhmgg","hhmhg","hhngg","hhnhg","hhogg","hhohg","hhpgg","hhphg","hhhhg","ahhhg","aihhg","bhhhg","bihhg","chhhg","cihhg","dhhhg","dihhg","ehhhg","eihhg","fhhhg","fihhg","ghhhg","gihhg","jhhhg","jihhg","khhhg","kihhg","lhhhg","lihhg","mhhhg","mihhg","nhhhg","nihhg","ohhhg","oihhg","phhhg","pihhg","iihhg","iiahg","iiaig","iibhg","iibig","iichg","iicig","iidhg","iidig","iiehg","iieig","iifhg","iifig","iighg","iigig","iijhg","iijig","iikhg","iikig","iilhg","iilig","iimhg","iimig","iinhg","iinig","iiohg","iioig","iiphg","iipig","iiiig","aiiig","ajiig","biiig","bjiig","ciiig","cjiig","diiig","djiig","eiiig","ejiig","fiiig","fjiig","giiig","gjiig","hiiig","hjiig","kiiig","kjiig","liiig","ljiig","miiig","mjiig","niiig","njiig","oiiig","ojiig","piiig","pjiig","jjiig","jjaig","jjajg","jjbig","jjbjg","jjcig","jjcjg","jjdig","jjdjg","jjeig","jjejg","jjfig","jjfjg","jjgig","jjgjg","jjhig","jjhjg","jjkig","jjkjg","jjlig","jjljg","jjmig","jjmjg","jjnig","jjnjg","jjoig","jjojg","jjpig","jjpjg","jjjjg","ajjjg","akjjg","bjjjg","bkjjg","cjjjg","ckjjg","djjjg","dkjjg","ejjjg","ekjjg","fjjjg","fkjjg","gjjjg","gkjjg","hjjjg","hkjjg","ijjjg","ikjjg","ljjjg","lkjjg","mjjjg","mkjjg","njjjg","nkjjg","ojjjg","okjjg","pjjjg","pkjjg","kkjjg","kkajg","kkakg","kkbjg","kkbkg","kkcjg","kkckg","kkdjg","kkdkg","kkejg","kkekg","kkfjg","kkfkg","kkgjg","kkgkg","kkhjg","kkhkg","kkijg","kkikg","kkljg","kklkg","kkmjg","kkmkg","kknjg","kknkg","kkojg","kkokg","kkpjg","kkpkg","kkkkg","ggggx","gggxx","ggxxx","gxxxx","xxxxx","xxxxy","xxxyy","xxyyy","xyyyy","yyyyy","yyyyw","yyyww","yywww","ywwww","wwwww","wwvww","wvvww","vvvww","vvvwz","avvwz","aavwz","aaawz","aaaaz"]

print(findLadders(beginWord, endWord, wordList))
    