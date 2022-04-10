print([1, 2, 3, 4] == [1, 2, 3, 4])
arr1 = [1, 2, 3, 4]
arr2 = [2, 3, 4, 5]
arr3 = [1, 2, 3, 4]
print(arr1 == arr2)
print(arr2 == arr3)
print(arr1 == arr3)

arr4 = ["a", "b", "c"]
print("".join(arr4))
print(" ".join(arr4))
print(" ".join(arr4)[1:])

for i in arr2:
    print(i)