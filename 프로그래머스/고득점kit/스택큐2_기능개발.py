def solution(progresses, speeds):
    answer = []
    # 1. len(progresses)>0 일 때까지 무한 루프, time을 +1 씩 증가시키면서 (진전도가 100 안넘을때) 진전사항이 100프로 이상일 때 찾아내기
    # 2. progresses[0]+time*speeds[0] 기능개발이 완료되었을 때, 다른 기능들도 완료가 되었으면 progresses, speeds에서 pop(0)하고 count +1
    # 3. progresses[0]+time*speeds[0] 완료되지 않았을 때, count가 0보다 크면 이미 완료된 것들은 count되고 pop 되었을 것이기에 answer 리스트에 정답을 넣고
    # 4. count를 0으로 reset 해준다 그리고 시간은 계속 +1씩 증가
    # 5. 마지막 카운트는 while문 빠져나오고 answer 리스트에 저장
    count = 0
    time = 0
    # 1
    while len(progresses) > 0:
        # 2
        if progresses[0]+time*speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        # 3
        else:
            if count > 0:
                answer.append(count)
                count = 0
            # 4
            time += 1
    # 5
    answer.append(count)
    return answer


print(solution([93, 30, 55],	[1, 30, 5]))  # 답	[2, 1]
print(solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1]))  # 답 [1, 3, 2]
