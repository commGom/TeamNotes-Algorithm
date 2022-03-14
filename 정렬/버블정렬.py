def bubble_sort(data):
    for i in range(len(data)):
        for j in range(1, len(data)):
            # 앞의 원소가 뒤의 원소보다 크면 swap
            if data[j-1] > data[j]:
                data[j-1], data[j] = data[j], data[j-1]


array = [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]
print("정렬 전:", array)
# ex 0 5 9 7 3 1 6 2 4 8 -> 0 1 2 3 4 5 6 7 8 9
bubble_sort(array)
print("정렬 후:", array)
