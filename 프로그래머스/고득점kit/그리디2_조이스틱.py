def solution(name):
    answer = 0
    change = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]
    idx = 0

    while True:
        answer += change[idx]
        change[idx] = 0
        if sum(change) == 0:
            return answer

      # 좌, 우 이동방향 정하기
        left, right = 1, 1
        while change[idx-left] == 0:
            left += 1
        while change[idx+right] == 0:
            right += 1

        answer += left if left < right else right
        # idx 조정
        idx += -left if left < right else right

    return answer


# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
# A B C D E F G H I J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
print(solution("JEROEN"))  # answer=56
print(solution("JAN"))  # answer=23
