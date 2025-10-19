def find_entry_exit_sequence(log_tuple, employee_id):
    if employee_id not in log_tuple:
        return ()
    first_occurrence_index = log_tuple.index(employee_id)

    try:
        second_occurrence_index = log_tuple.index(employee_id, first_occurrence_index + 1)
        return log_tuple[first_occurrence_index : second_occurrence_index + 1]

    except ValueError:
        return log_tuple[first_occurrence_index:]

# Примеры использования из задания
print(find_entry_exit_sequence((1, 2, 3), 8))
print(find_entry_exit_sequence((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(find_entry_exit_sequence((1, 2, 8, 5, 1, 2, 9), 8))