import sys
input = sys.stdin.readline

# K1KA5CB7 -> ABCKK13
# AJKDLSI412K4JSJ9D -> ADDIJJJKKLSS20

input_value = input().rstrip()
# input_value='K1KA5CB7'
# input_value='AJKDLSI412K4JSJ9D'

answer_alpha = []
answer_digit = 0

for val in input_value:
    if val.isalpha():
        answer_alpha.append(val)
    elif val.isdigit():
        answer_digit += int(val)
answer_alpha.sort()

answer = ''.join(answer_alpha)+str(answer_digit)
print(answer)
