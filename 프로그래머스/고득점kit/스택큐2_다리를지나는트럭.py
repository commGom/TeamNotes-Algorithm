def solution(bridge_length, weight, truck_weights):

    answer = 0
    # 조건 정리
    # 1초에 길이 1씩 이동
    # weight 이하만큼 트럭이 올라갈 수 있다.
    one_truck_weight = truck_weights.pop(0)
    weight_on_bridge = one_truck_weight
    check_queue = [[one_truck_weight, 0]]
    time = 0
    while True:
        # print(truck_weights, check_queue, time, bridge_length)
        # 1초 증가
        time += 1
        for i in range(len(check_queue)-1, -1, -1):
            # print(i)
            check_queue[i][1] += 1
            if check_queue[i][1] == bridge_length:
                w, l = check_queue.pop(0)
                weight_on_bridge -= w
        if truck_weights and weight_on_bridge+truck_weights[0] <= weight:
            one_truck_weight = truck_weights.pop(0)
            weight_on_bridge += one_truck_weight
            check_queue.append([one_truck_weight, 0])

        if not check_queue:
            break
    answer = time+1
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100,	[10]))
print(solution(100,	100,	[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))

# 다리 길이 2
# 최대 무게 10
# 7 4 5 6
# step 1. 다리위의 무게 weight_on_bridge=0, 시간 time=0(1 증가할 때 length 1 씩 증가)으로 두고 시작
# step 2. 1초 증가할 때, weight_on_brige+=truck_weights[0]<=weight 기다리고 있는 트럭에서 하나뺀다 queue.append([truck_weights.pop(0),현재위치0])
# step 3. queue를 반복하면서(나중에 넣은 값부터 거꾸로 반복) idx=1에 있는 현재 위치 +1 하고 값이 bridge_length와 같으면 pop(0)해서 빼내고 brige_on_bridge-= idx=0에 있는 값
# step 4. answer=time
