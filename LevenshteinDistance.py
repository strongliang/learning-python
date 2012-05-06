def Levenshtein(s, t):
    # for all i and j, d[i,j] will hold the Levenshtein distance between
    # the first i characters of s and the first j characters of t;
    # note that d has (m+1)x(n+1) values
    m, n = len(s)+1, len(t)+1
    d = [[0 for col in range(n)] for row in range(m)]
        
    for i in range(m):
        d[i][0] = i  # the distance of any first string to an empty second string
    for j in range(n):
        d[0][j] = j  # the distance of any second string to an empty first string
    
    for j in range(1, n):
        for i in range(1, m):
            p, q = i-1, j-1
            if s[p] == t[q]:
                d[i][j] = d[i-1][j-1] # no operation required
            else:
                term1 = d[i-1][j] + 1 # a deletion
                term2 = d[i][j-1] + 1 # an insertion
                term3 = d[i-1][j-1] + 1 # a substitution
                d[i][j] = min(term1, term2, term3)
                
    for i in range(len(d)):
        print d[i]
    return d[m-1][n-1]
    
print Levenshtein('C++', 'C#')
#print Levenshtein('addd', 'absdfs')
#print Levenshtein ("A man, a plan, a canal - Panama!", "Doc, note: I dissent. A fast never prevents a fatness. I diet on cod.")
#print Levenshtein('fdsfds', 'fsdfsd')
#print Levenshtein('smotheredsdfdfdssdfsdfsdsdfsdfsdfsdfsd','thereaabdfdsdfsdfsdfsdfsdfsdfsdfsddf')