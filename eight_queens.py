from itertools import permutations
 
n = 5
cols = range(n)

def display_sol(sol, count):
    board = [['=' for col in range(n)] for row in range(n)]
    print '   ===solution', count, '==='
    for i in range(len(board)):
        board[i][sol[i]] = 'Q'
        print board[i]
        
count = 1

"The technique for checking the diagonals is to add or subtract the column number from each entry, so any two entries on the same diagonal will have the same value (in other words, the sum or difference is unique for each diagnonal). Now all we have to do is make sure that the diagonals for each of the eight queens are distinct. So, we put them in a set (which eliminates duplicates) and check that the set length is eight (no duplicates were removed)."
for vec in permutations(cols):
    if (n == len(set(vec[i] + i for i in cols))
          == len(set(vec[i] - i for i in cols))):         
        display_sol(vec, count)
        count += 1



