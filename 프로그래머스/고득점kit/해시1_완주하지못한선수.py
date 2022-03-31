def solution(participant, completion):
    answer = ''
#     전략 dict()에 participant를 key:참가자이름 value:동명이인 경우 대비 +1 씩 한 후
#     1. completion for문으로 확인하면서 해당 키 값 -1 해준 후
#     2. 딕셔너리 자료구조 for문 돌면서 value 숫자만큼 반복해서 key(참가자이름) 출력
#     3. 이 문제의 경우 단 한명의 선수만이 완주를 못하였기 때문에 value가 1인 경우 answer로 변수 재정의 한 후 return 종료 해준다
    dic = dict()
    # 1
    for name in participant:
        if name in dic:
            dic[name] += 1
        else:
            dic[name] = 1
    print(dic)

    # 2
    for name in completion:
        dic[name] -= 1

    # 3
    for name, cnt in dic.items():
        if cnt == 1:
            answer = name
            break

    return answer


print(solution(["mislav", "stanko", "mislav", "ana"],
      ["stanko", "ana", "mislav"]))
