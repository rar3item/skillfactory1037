def create_nums():
    global nums
    global searching_number
    try:
        nums = list(map(int, input().split()))
        nums.sort()
        searching_number = int(input())
        return nums, searching_number
    except ValueError:
        print('Ошибка ! Введено некорректное значение.')

def binary_search(nums, searching_number, left, right): 
    if left > right: # если левая граница превысила правую,
        return False # значит элемент отсутствует
    
    middle = (right+left) // 2 # находимо середину
    if nums[middle] == searching_number: # если элемент в середине,
        return middle # возвращаем этот индекс
    elif searching_number < nums[middle]: # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(nums, searching_number, left, middle-1)
    else: # иначе в правой
        return binary_search(nums, searching_number, middle+1, right)

create_nums()
print(binary_search(nums, searching_number, 0, (len(nums) - 1)))
    
