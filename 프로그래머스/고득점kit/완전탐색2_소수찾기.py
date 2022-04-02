import itertools


def check_prime(num):
    result = True
#     소수 여부 로직 구현
    if num == 1 or num == 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            result = False
            return result
    return result


def solution(numbers):
    answer = 0
    numbers = list(map(str, numbers))
    print(numbers)
    numbers_set = set()

    for i in range(1, len(numbers)+1):
        r = i
        nPr = list(itertools.permutations(numbers, r))
        for nums in nPr:
            numbers_set.add(int(''.join(nums)))
        print(nPr)
    print(numbers_set)
    for num in numbers_set:
        if check_prime(num):
            answer += 1
    return answer


print(solution("011"))
print(solution("17"))
