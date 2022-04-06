
def solution(people, limit):
  # 구명보트 최대 2명, params : 사람들 몸무게 리스트(people 40~240kg) 무게 제한 있음(limit 40~240kg)
    answer = 0
  # 1. 내림차순 정렬
    people.sort(reverse=True)
    l = 0
    r = len(people)-1

    while l < r:
        total = people[l]+people[r]
        if(total > limit):
            l += 1
            # 큰 것 하나만 빠진다
        else:
            l += 1
            r -= 1
        answer += 1
    if l == r:
        answer += 1

    return answer


print(solution([70, 50, 80, 50],	100))  # return 3
print(solution([70, 80, 50],	100))  # return 3
