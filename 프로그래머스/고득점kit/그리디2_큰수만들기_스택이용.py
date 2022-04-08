def solution(number, k):
    answer = []  # Stack

    for num in number:
        print(k, answer)

        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                # 정답에 들어있는 마지막 값이 num보다 작으면 pop해서 k(제거할 숫자 갯수) 체크해준다.
                answer.pop()
                k -= 1
                # k(k개만큼 숫자제거) or answer이 비어있을 때 while문 빠져나감
                if not answer or k <= 0:
                    break
        # 제일 큰 수를 stack에 넣는다
        answer.append(num)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)


print(solution("1924", 2))  # "94"
print(solution("1231234", 3))  # "3234"
print(solution("4177252841", 4))  # "775841"
