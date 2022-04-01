import itertools


def solution(numbers):
    answer = ''
    r = len(numbers)
    nPr = list(itertools.permutations(numbers, r))
    print(nPr)
    candidates = []
    for element in nPr:
        candidates.append(''.join(map(str, element)))
    candidates.sort(reverse=True)
    answer = candidates[0]
    return answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
