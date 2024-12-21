def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

def get_set_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            user_set = set(map(int, user_input.split()))
            return user_set
        except ValueError:
            print("Ошибка ввода: Пожалуйста, введите числа, разделенные пробелом.")

if __name__ == "__main__":
    print("Введите элементы первого множества")
    set1 = get_set_input("Первое множество: ")

    print("Введите элементы второго множества")
    set2 = get_set_input("Второе множество: ")

    result = symmetric_difference(set1, set2)
    print("Симметрическая разность двух множеств:")
    print(result)