# bornday.py

# Правильные данные
correct_year = 1799
correct_day = 6

# Спрашиваем пользователя
user_year = int(input("Введите год рождения А.С. Пушкина: "))

# Проверка года
if user_year == correct_year:
    user_day = int(input("Введите день рождения А.С. Пушкина: "))
    if user_day == correct_day:
        print("Верно")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год рождения")