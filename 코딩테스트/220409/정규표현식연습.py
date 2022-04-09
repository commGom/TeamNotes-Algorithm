import re

# example = "abxdeydeabz"

# ex = example.split(" ")
# ex2 = re.split("(ab)|(de)", example)
# print(ex2)
# print(ex)

ex3 = "abcABCabCaBCAbbc"
p = re.compile('abc', re.I)
print(p)
print(p.match(ex3))
