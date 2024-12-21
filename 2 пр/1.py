import statistics

def analyze_list(lst):
    if not lst:
        return {'max': None, 'min': None, 'avg': None, 'med': None}
    
    return {
        'max': max(lst),
        'min': min(lst),
        'avg': sum(lst) / len(lst),
        'med': statistics.median(lst)
    }

def get_user_input():
    while True:
        user_input = input("Введите список чисел, разделенных пробелом: ")
        try:
            num_list = list(map(float, user_input.split()))
            if not num_list:
                raise ValueError("Список пуст!")
            return num_list
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Пожалуйста, введите корректные числа.")

if __name__ == "__main__":
    user_list = get_user_input()
    result = analyze_list(user_list)
    print("Результат анализа списка:")
    print(result)