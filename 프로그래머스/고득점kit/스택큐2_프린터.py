import time


def solution(priorities, location):
    answer = 0
  # 1. 중요도 importance를 priorities에서 count 할 것이다 (1~9)
    importance = [0]*10
    # start = time.time()
    for i in range(len(importance)):
        importance[i] = priorities.count(i)
    # for i in priorities:
    #     importance[i] += 1
    # end = time.time()
    # print(end-start)
    # print(importance)
  # 2. queue 자료구조를 만들어 (우선순위,위치)를 주어진 순서대로 넣는다
    queue = []
    for i in range(len(priorities)):
        queue.append((priorities[i], i))

  # 3. 중요도 1~9까지 이므로 9에서부터 1까지 내려오면서
    for k in range(9, 0, -1):
        # 3-2. while 반복문으로 중요도의 숫자가 높은 순으로 카운트 갯수가 0이 아닐때 까지 점검 importance[중요도]값이 0이 아니면 존재하는 것 queue에서 제일 앞에 있는 것 pop 한 후
        # 3-3-1. while 반복문에 해당하는 중요도 k 값일 경우 중요도 갯수를 카운트 한 것 -1하고 출력 answer 카운트를 +1
        # 3-3-2. 그리고 해당 위치의 출력이면 location과 일치할 경우 해당 answer를 return 한다
        # 3-4-1. while 반복문에 해당하는 중요도 k와 다를 경우 다시 queue에 넣어준다
        # while문은 해당하는 중요도를 만나면 -1을 하거나 정답일 경우 return을 하므로 0이 될때까지 반복할 것이다.
        while importance[k] != 0:
            # 0이면 다음 중요도 k
            vals = queue.pop(0)
            # 우선 순위와 해당하는 위치 vals=(priority,location)
            if vals[0] == k:
                importance[k] -= 1
                answer += 1
                if vals[1] == location:
                    return answer
            else:
                queue.append(vals)
    answer = 0
    return answer


print(solution([2, 1, 3, 2],	2))
print(solution([1, 1, 9, 1, 1, 1],	0))
