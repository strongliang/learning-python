# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and outputs the last position in the search string
# where the target string appears, or -1 if there
# are no occurences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(target, search):
    last = -1
    idx = target.find(search, 0)
    while idx != -1:
        last = idx
        idx = target.find(search, idx+1)
    print last
        
        
find_last('abca', 'b')        







