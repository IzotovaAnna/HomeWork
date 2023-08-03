array = list(map(int, input("Введите числа через пробел: ").split()))

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)

element = int(input("Введите число из списка: "))

if (element not in array):
    print("Число не из списка")

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)
print("Индекс числа - ", binary_search(array, element, 0, len(array) - 1))