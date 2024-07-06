# bornyearforewer.py

# Правильный год рождения А.С. Пушкина
correct_year = 1799

while True:
    user_input = int(input("Введите год рождения А.С. Пушкина: "))
    if user_input == correct_year:
        print("Верно")
        break
    else:
        print("Неверно")