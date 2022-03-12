
def selection_sort(data):
    for i in range(len(data)):
        min_idx = i  # 가장 작은 원소 값을 찾아서 index를 변수 지정하여 i 위치에 있는 값과 원소값 바꾸기
        for j in range(i+1, len(data)):
            if data[min_idx] > data[j]:  # min_idx에 최소값을 찾기 위해 작은 값이 나오면 바꿔주기 위한 조건문
                min_idx = j  # 인덱스 j에 있는 원소값이 작으면

        data[i], data[min_idx] = data[min_idx], data[i]  # 값 change


array = [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]
print("정렬 전:", array)
# ex 0 5 9 7 3 1 6 2 4 8 -> 0 1 2 3 4 5 6 7 8 9
selection_sort(array)
print("정렬 후:", array)
