import sys
input = sys.stdin.readline

# 숫자 두 개 최대공약수 구하기


# 최대공약수 Greatest common divisor gcd() 함수로 정의
def gcd(num1, num2):
    if num1 % num2 == 0:
        return num2
    return gcd(num2, num1 % num2)


# 숫자 두개 입력 받기 ex) 192, 162 -> 6
num1, num2 = map(int, input().rstrip().split())
print(num1, num2)

print(gcd(max(num1, num2), min(num1, num2)))
