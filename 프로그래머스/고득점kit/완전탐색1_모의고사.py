def checkAnswer(a, b):
    result = 0
    if a == b:
        result = 1
    return result


def solution(answers):
    answer = []
    # 1. 1, 2, 3 반복되는 답 패턴 리스트에 넣기
    # dict 1번,2번,3번 수포자 : 맞힌 갯수
    # answer for문 돌면서
    # 1
    answers1 = [1, 2, 3, 4, 5]
    answers2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answers3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # 2
    dic = dict({1: 0, 2: 0, 3: 0})
    for i in range(len(answers)):
        dic[1] += checkAnswer(answers[i], answers1[i % len(answers1)])
        dic[2] += checkAnswer(answers[i], answers2[i % len(answers2)])
        dic[3] += checkAnswer(answers[i], answers3[i % len(answers3)])
    max_cnt = max(dic.values())
    for key in dic:
        if dic[key] == max_cnt:
            answer.append(key)
    return answer


print(solution([1, 3, 2, 4, 2]))
