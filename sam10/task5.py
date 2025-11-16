# Создаем собственное исключение для проверки возраста
class AgeRestrictionException(Exception):
    pass
# Первая функция - проверка возраста для фильма
def check_movie_age(age, movie_rating):
    if age < movie_rating:
        # Выбрасываем наше исключение с информацией о фильме
        raise AgeRestrictionException(f"Возраст {age} меньше разрешенного {movie_rating}+")
    print(f"Можно смотреть фильм {movie_rating}+ (возраст: {age})")
    return True


# Вторая функция - проверка возраста для вождения
def check_driving_age(age, country):
    driving_ages = {'Россия': 18, 'США': 16, 'Германия': 17}
    min_age = driving_ages.get(country, 18)

    if age < min_age:
        # Используется то же исключение для другой ситуации
        raise AgeRestrictionException(f"В {country} нельзя водить с {age} лет (минимум: {min_age})")
    print(f"Можно водить в {country} (возраст: {age})")
    return True


# Тест функций с исключениями
if __name__ == '__main__':
    print("ПРОВЕРКА ВОЗРАСТА ДЛЯ ФИЛЬМОВ")

    # Тест 1: Подходящий возраст для фильма
    try:
        check_movie_age(20, 16)  # 20 лет для фильма 16+
    except AgeRestrictionException as e:
        print(f"Ошибка: {e}")

    # Тест 2: Слишком молод для фильма
    try:
        check_movie_age(14, 18)  # 14 лет для фильма 18+
    except AgeRestrictionException as e:
        print(f"Ошибка: {e}")

    print("\nПРОВЕРКА ВОЗРАСТА ДЛЯ ВОЖДЕНИЯ")

    # Тест 3: Можно водить в России
    try:
        check_driving_age(20, 'Россия')  # 20 лет для России
    except AgeRestrictionException as e:
        print(f" Ошибка: {e}")

    # Тест 4: Нельзя водить в США
    try:
        check_driving_age(15, 'США')  # 15 лет для США
    except AgeRestrictionException as e:
        print(f"Ошибка: {e}")

    print("\nПРЯМОЙ ВЫЗОВ ИСКЛЮЧЕНИЯ")

    # Тест 5: Демонстрация прямого вызова исключения
    try:
        raise AgeRestrictionException("Специальное сообщение об ошибке возраста")
    except AgeRestrictionException as e:
        print(f"Сообщение: {e}")