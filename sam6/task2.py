def remove_first_occurrence(tpl, element_to_remove):
    if element_to_remove not in tpl:
        return tpl
    try:
        index_to_remove = tpl.index(element_to_remove)
    except ValueError:
        return tpl
    new_tpl = tpl[:index_to_remove] + tpl[index_to_remove + 1:]

    return new_tpl

print(remove_first_occurrence((1, 2, 3), 1))
print(remove_first_occurrence((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove_first_occurrence((2, 4, 6, 6, 4, 2), 9))