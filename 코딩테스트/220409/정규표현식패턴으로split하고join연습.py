patterns = ["ab", "abc", "abcde", "hi", "jk"]
patterns.sort(key=lambda x: -len(x))
print(patterns)

example = "abxdeydeabz"
for pattern in patterns:
    example = "".join(example.split(pattern))
print(example)
