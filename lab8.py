import tkinter as tk

def calculate_minimum():
    n = 4
    K = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    K.append([i, j, k, l])

    min_sum = float('inf')
    min_combination = None

    for combination in K:
        # Проверяем ограничения на четность и нечетность элементов
        if all(x % 2 == 1 for x in combination[::2]) and all(x % 2 == 0 for x in combination[1::2]):
            # Вычисляем значение целевой функции
            sum_mod = sum(abs(x) for x in combination) % 6
            # Обновляем минимальное значение и комбинацию переменных
            if sum_mod < min_sum:
                min_sum = sum_mod
                min_combination = combination

    result_label.config(text="Минимальное значение: {}\nКоличество допустимых комбинаций: {}\nНабор переменных, при котором достигается минимум: {}".format(min_sum, sum_mod, min_combination))

root = tk.Tk()

calculate_button = tk.Button(root, text="Calculate Minimum", command=calculate_minimum)
calculate_button.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()