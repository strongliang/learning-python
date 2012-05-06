def combo(word, combo_len):
    res = []
    if len(word) == combo_len:
        return [word]
        
    tmp_res = reduce(word, len(word) - combo_len)
    for r in tmp_res:
        if len(r) == combo_len:
            res.append(r)
    return res
    
def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def reduce(word, to_cut):
    res = []
    for i in range(len(word)):
        new_word = word[0:i] + word[i+1:]
        res.append(new_word)
    if to_cut == 1:
        return res
    else:
        new_res = []
        for w in res:
            new_res += reduce(w, to_cut-1)
        union(res, new_res)
        return res 
        
        
print combo('abcde', 4)