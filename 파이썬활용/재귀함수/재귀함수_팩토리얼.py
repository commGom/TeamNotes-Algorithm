# 반복적으로 팩토리얼 구현한 함수
def factorial_iterative(n):
    result = 1
    for num in range(1, n+1):
        result *= num
    return result

# 재귀함수를 이용한 팩토리얼 구현한 함수


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n*factorial_recursive(n-1)


# 각각 결과 출력
print(f'반복적으로 팩토리얼 구현:factorial_iterative(5)-> {factorial_iterative(5)}')
print(f'재귀적으로 팩토리얼 구현:factorial_recursive(5)-> {factorial_recursive(5)}')
