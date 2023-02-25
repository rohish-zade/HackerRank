# itertools.permutations()

# itertools.permutations(iterable[, r])
# This tool returns successive r length permutations of elements in an iterable.
# If r is not specified or is None, then r defaults to the length of the iterable, and all possible full length permutations are generated.
# Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced
# in a sorted order.

# Task
# You are given a string S. 
# Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

# Input Format
# A single line containing the space separated string S and the integer value k.

# Constraints
# 0 < k <= len(S) 
# The string contains only UPPERCASE characters.

# Output Format
# Print the permutations of the string S on separate lines.

from itertools import permutations

#my solution
S, K = input().split()
N = int(K)
ans = list(permutations(S, N))
ans.sort()
res = [''.join(tuple_elements) for tuple_elements in ans]
for i in res:
    print(i)

# optimal solution
for i in sorted(permutations(S[0], int(S[1]))):
    print ''.join(i)
