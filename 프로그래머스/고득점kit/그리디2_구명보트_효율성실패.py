def solution(people, limit):
  # 구명보트 최대 2명, params : 사람들 몸무게 리스트(people 40~240kg) 무게 제한 있음(limit 40~240kg)
    answer = 0
  # 1. 내림차순 정렬
    people.sort(reverse=True)
    while people:
        standard = limit
        standard -= people.pop(0)
        answer += 1
        for i in range(len(people)):
            if standard >= people[i]:
                del people[i]
                break
    return answer


print(solution([70, 50, 80, 50],	100))  # return 3
print(solution([70, 80, 50],	100))  # return 3
