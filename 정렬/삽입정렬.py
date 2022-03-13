def insertion_sort(data):
    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            if data[j-1] > data[j]:
                data[j], data[j-1] = data[j-1], data[j]
            else:  # 작거나 같을 경우 앞에 부분은 다 정렬과정을 거쳐서 왔다.
                break


array = [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]
print("정렬 전:", array)
# ex 0 5 9 7 3 1 6 2 4 8 -> 0 1 2 3 4 5 6 7 8 9
insertion_sort(array)
print("정렬 후:", array)
