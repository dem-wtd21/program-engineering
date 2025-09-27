value = 5
while value < 50:
    if value == 0:
        value += 5
    elif value / 5 == 1:
        value += 5
    else:
        value *= 5
    print(value)