from collections import Counter


def solution(n, lost, reserve):
    answer = 0
    # 1. n 만큼 리스트 (체육복 갯수 1 로 초기화)
    # 2. lost 반복문 돌리면서 해당 번호의 학생 체육복 갯수 -1
    # 3. reserve 반복문 돌리면서 해당 번호의 학생 체육복 갯수 +1
    # 4. 해당 index가 0일 때, 앞의 index나 뒤의 index가 2일 때 카운트(해당 index의 체육복 갯수 -1), 나머지 경우는 노카운트

    # 1
    clothes = [1 for i in range(n)]
    print(clothes)
    # 2
    for i in lost:
        clothes[i-1] -= 1
    print(clothes)
    # 3
    for i in reserve:
        clothes[i-1] += 1
    print(clothes)

    for i in range(len(clothes)):
        if clothes[i] == 0:
            if i > 0 and clothes[i-1] == 2:
                clothes[i-1] -= 1
                clothes[i] += 1
                continue
            if i < len(clothes)-1 and clothes[i+1] == 2:
                clothes[i+1] -= 1
                clothes[i] += 1
                continue

    count = Counter(clothes)   # my_list에 각 개체가 몇 번 나오는지 카운트
    answer = n-count[0]
    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5,	[2, 4],	[3]))
print(solution(3,	[3],	[1]))
