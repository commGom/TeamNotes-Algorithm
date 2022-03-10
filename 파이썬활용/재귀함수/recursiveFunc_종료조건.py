def recursive_function(i):
    # 종료 조건 명시 : i가 100일 경우 종료
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수 호출하는 중')
    recursive_function(i+1)


recursive_function(1)
