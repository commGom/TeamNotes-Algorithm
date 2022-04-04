def solution(citations):
    answer = 0
    # 1. citataions 오름차순으로 정렬
    citations.sort()
    print(citations)
    # 2. len(citataions)-(i+1)+1 (남은 거 갯수 카운트) >= citations[i] (h 목표)
    n = len(citations)
    for i in range(len(citations)):
        high_count = len(citations)-(i+1)+1
        low_count = n-high_count
        h = citations[i]

        if high_count >= h and low_count < h:
            answer = citations[i]
    return answer


print(solution([3, 0, 6, 1, 5]))
# return 값 : 3
