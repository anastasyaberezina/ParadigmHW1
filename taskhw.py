numbers = [10, 1, 5, 8, 9, 0, 2]

#Императивный
def sort_list_imperative(numbers): 
    flag = True
    while flag:
        flag = False
        for i in range(len(numbers) - 1):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                flag = True
    return numbers

#Декларативный
def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    return numbers

print(sort_list_imperative(numbers))
print(sort_list_declarative(numbers))
