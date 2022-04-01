import itertools

arr = ['A', 'B', 'C']
r = 2
nPr = itertools.permutations(arr, r)
print(list(nPr))

# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]


arr = ['A', 'B', 'C']
r = 2
nCr = itertools.combinations(arr, r)
print(list(nCr))

# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]
