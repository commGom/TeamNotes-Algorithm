import re


def solution(call):
    answer = ''
    count = 0
    patterns = []
    # 반복 문자 갯수 1~length까지
    for i in range(1, len(call)+1):
        for j in range(len(call)):
            pattern = call[j:j+i]
            # pattern 일치 갯수 count
            p = re.compile(pattern, re.I)
            check_count = len(p.findall(call))
            if check_count > count:
                count = check_count
                patterns = list(pattern)
            elif check_count == count:
                patterns.append(pattern)
    patterns.sort(key=lambda x: -len(x))

    for p in patterns:
        call = "".join(call.split(p))
    answer = call
    return answer
