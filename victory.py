# victory.py

def quiz():
    # Список знаменитостей и их годов рождения
    celebrities = {
        "А.С. Пушкин": 1799,
        "Л.Н. Толстой": 1828,
        "Ф.М. Достоевский": 1821,
        "И.С. Тургенев": 1818,
        "М.Ю. Лермонтов": 1814
    }

    correct_answers = 0
    total_questions = len(celebrities)

    for name, year in celebrities.items():
        user_input = int(input(f"Введите год рождения {name}: "))
        if user_input == year:
            correct_answers += 1

    incorrect_answers = total_questions - correct_answers
    correct_percentage = (correct_answers / total_questions) * 100
    incorrect_percentage = 100 - correct_percentage

    print(f"Количество правильных ответов: {correct_answers}")
    print(f"Количество ошибок: {incorrect_answers}")
    print(f"Процент правильных ответов: {correct_percentage:.2f}%")
    print(f"Процент неправильных ответов: {incorrect_percentage:.2f}%")

    # Предлагаем начать заново
    restart = input("Хотите начать игру сначала? (да/нет): ").strip().lower()
    if restart == 'да':
        quiz()

# Запуск викторины
if __name__ == "__main__":
    quiz()
