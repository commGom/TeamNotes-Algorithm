def solution(brown, yellow):
    answer = []
    # 노란색의 경우의 수 yellow%i (i는 1부터) ==0 일때
    # yello_x=max(i,yellow//i) yello_y=min(i,yellow//i)
    # brown == 2(yellow_x+2)+yello_y break
    for i in range(1, yellow+1):
        if yellow % i == 0:
            yello_x = max(i, yellow//i)
            yello_y = min(i, yellow//i)
            if brown == 2*(yello_x+2)+2*yello_y:
                answer = [yello_x+2, yello_y+2]
                break
    return answer


print(solution(10, 2))  # [4, 3]
print(solution(8,	1))  # [3, 3]
print(solution(24,	24))  # [8, 6]
