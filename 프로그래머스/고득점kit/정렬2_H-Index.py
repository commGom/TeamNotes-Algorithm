def solution(citations):
    answer = 0
    # 1. citataions 오름차순으로 정렬
    citations.sort()
    # print(citations)
    # 2. len(citataions)-(i+1)+1 (남은 거 갯수 카운트) >= citations[i] (h 목표)
    n = len(citations)
    for i in range(len(citations)):
        h_index = len(citations)-(i+1)+1

        if citations[i] >= h_index:
            answer = h_index
            break
    return answer


print(solution([3, 0, 6, 1, 5]))
# return 값 : 3
