def update_employee_list(employee_tuple, new_employee):
    # Если сотрудника нет, он просто добавлятся в конец
    if new_employee not in employee_tuple:
        return employee_tuple + (new_employee,)
    else:
        # Если сотрудник есть, находится его индекс
        index_to_remove = employee_tuple.index(new_employee)

        # Если сотрудник уже в конце, возвращается исходный кортеж
        if index_to_remove == len(employee_tuple) - 1:
            return employee_tuple

        # Создается новый кортеж без этого сотрудника (исключая его срез)
        temp_tuple = employee_tuple[:index_to_remove] + employee_tuple[index_to_remove + 1:]

        # Добавление сотрудника в конец
        return temp_tuple + (new_employee,)


# Тестовые примеры (3 кейса)
# 1. Сотрудника нет (добавление)
employees_1 = ("Анна", "Борис", "Сергей")
print(f"Тест 1 (Нет в списке): {update_employee_list(employees_1, 'Дмитрий')}")

# 2. Сотрудник есть, но не в конце (перемещение в конец)
employees_2 = ("Анна", "Борис", "Сергей")
print(f"Тест 2 (В начале списка): {update_employee_list(employees_2, 'Анна')}")

# 3. Сотрудник есть, и он уже в конце списка (возврат без изменений)
employees_3 = ("Анна", "Борис", "Сергей")
print(f"Тест 3 (Уже в конце): {update_employee_list(employees_3, 'Сергей')}")