def tuple_stats(tpl):
    total_sum = sum(tpl)  
    average = total_sum / len(tpl)  
    unique_elements = tuple(set(tpl))  
    return total_sum, average, unique_elements

def get_user_input():
    while True:
        try:
            user_input = input("Введите числа через пробел: ")
            numbers = tuple(map(float, user_input.split())) 
            if not numbers:
                raise ValueError("Кортеж не должен быть пустым!")
            return numbers
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Попробуйте снова.")

user_tuple = get_user_input()
result = tuple_stats(user_tuple)
print("Результаты:", result)