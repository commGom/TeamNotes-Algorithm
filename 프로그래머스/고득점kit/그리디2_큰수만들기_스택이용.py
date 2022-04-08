def solution(number, k):
    answer = []  # Stack

    for num in number:
        print(k, answer)
        answer.append(num)

        # if not answer:
        #     answer.append(num)
        #     continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                # k(k개만큼 숫자제거) or answer이 비어있을 때 while문 빠져나감
                if not answer or k <= 0:
                    break
        # answer.append(num)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)


print(solution("1924", 2))  # "94"
print(solution("1231234", 3))  # "3234"
print(solution("4177252841", 4))  # "775841"
