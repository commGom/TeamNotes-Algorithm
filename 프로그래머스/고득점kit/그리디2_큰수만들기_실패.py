from itertools import combinations


def solution(number, k):
    answer = "".join(number[:len(number)-k])
    number = list(map(str, number))
    extracted_list = list(combinations(number, len(number)-k))
    for extracted_number in extracted_list:
        # print(extracted_number)
        compared_answer = "".join(extracted_number)
        answer = max(answer, compared_answer)
    return answer


print(solution("1924", 2))  # "94"
print(solution("1231234", 3))  # "3234"
print(solution("4177252841", 4))  # "775841"
