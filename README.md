# TeamNotes-Algorithm
## 입력
- 문자열로 받은 숫자 한자리씩 리스트로 저장

```python
import sys
input = sys.stdin.readline

number_list = list(map(int, input().rstrip()))

print(number_list)

# 입력값 : 02987
# 출력값 : [0,2,9,8,7]
```

- 띄어 쓰기로 숫자 입력 받아서 리스트로 정렬된 상태로 저장

```python

import sys
input = sys.stdin.readline

input_sorted_list=sorted(list(map(int, input().rstrip().split())), reverse=True)


# 입력값 : # 2 3 1 2 2
# 출력값 : [3,2,2,2,1]

```

## 백준
### 그리디
| 분류       | 제목              | 날짜 |
| -------- | ----------------- | ------ |
| 그리디   | 1이 될 때 까지         | 22-03-08      |
| 그리디   | 1이 될 때 까지         | 22-03-08      |
| 그리디(백준)   | 11047 동전        | 22-03-08      |
