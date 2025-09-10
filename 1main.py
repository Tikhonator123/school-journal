import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()

# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']

# словарь с оценками
students_marks = {}

# генерация случайных оценок
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks

def print_menu():
    print('''
    Список команд:
    1. Добавить оценку ученика по предмету
    2. Вывести средний балл по всем предметам по каждому ученику
    3. Вывести все оценки по всем ученикам
    4. Удалить оценку ученика
    5. Редактировать оценку ученика
    6. Добавить нового ученика
    7. Удалить ученика
    8. Добавить новый предмет
    9. Удалить предмет
    10. Вывести все оценки по определённому ученику
    11. Вывести средний балл по каждому предмету для определённого ученика
    12. Выход из программы
    ''')

print_menu()

while True:
    try:
        command = int(input('Введите команду: '))
    except ValueError:
        print("Ошибка: введите номер команды числом.")
        continue

    if command == 1:
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        try:
            mark = int(input('Введите оценку: '))
        except ValueError:
            print("Ошибка: оценка должна быть числом.")
            continue
        if student in students_marks and class_ in students_marks[student]:
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или предмета')

    elif command == 2:
        for student in students:
            print(student)
            for class_ in classes:
                marks = students_marks[student][class_]
                if marks:
                    avg = sum(marks) / len(marks)
                    print(f'{class_} - {avg:.2f}')
            print()

    elif command == 3:
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == 4:
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks and class_ in students_marks[student]:
            print(f'Оценки: {students_marks[student][class_]}')
            try:
                index = int(input('Введите номер оценки для удаления (с 1): ')) - 1
                if 0 <= index < len(students_marks[student][class_]):
                    removed = students_marks[student][class_].pop(index)
                    print(f'Удалена оценка {removed}')
                else:
                    print("Неверный индекс.")
            except ValueError:
                print("Ошибка: индекс должен быть числом.")
        else:
            print("Ошибка: ученик или предмет не найден.")

    elif command == 5:
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks and class_ in students_marks[student]:
            print(f'Оценки: {students_marks[student][class_]}')
            try:
                index = int(input('Введите номер оценки для изменения (с 1): ')) - 1
                new_mark = int(input('Введите новую оценку: '))
                if 0 <= index < len(students_marks[student][class_]):
                    students_marks[student][class_][index] = new_mark
                    print(f'Оценка изменена на {new_mark}')
                else:
                    print("Неверный индекс.")
            except ValueError:
                print("Ошибка: вводите числа.")
        else:
            print("Ошибка: ученик или предмет не найден.")

    elif command == 6:
        student = input('Введите имя нового ученика: ')
        if student not in students_marks:
            students.append(student)
            students.sort()
            students_marks[student] = {class_: [] for class_ in classes}
            print(f'Ученик {student} добавлен.')
        else:
            print("Такой ученик уже существует.")

    elif command == 7:
        student = input('Введите имя ученика для удаления: ')
        if student in students_marks:
            del students_marks[student]
            students.remove(student)
            print(f'Ученик {student} удалён.')
        else:
            print("Такого ученика нет.")

    elif command == 8:
        class_ = input('Введите название нового предмета: ')
        if class_ not in classes:
            classes.append(class_)
            for student in students_marks:
                students_marks[student][class_] = []
            print(f'Предмет {class_} добавлен.')
        else:
            print("Такой предмет уже существует.")

    elif command == 9:
        class_ = input('Введите название предмета для удаления: ')
        if class_ in classes:
            classes.remove(class_)
            for student in students_marks:
                students_marks[student].pop(class_, None)
            print(f'Предмет {class_} удалён.')
        else:
            print("Такого предмета нет.")

    elif command == 10:
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(student)
            for class_, marks in students_marks[student].items():
                print(f'{class_}: {marks}')
        else:
            print("Такого ученика нет.")

    elif command == 11:
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(student)
            for class_, marks in students_marks[student].items():
                if marks:
                    avg = sum(marks) / len(marks)
                    print(f'{class_}: {avg:.2f}')
                else:
                    print(f'{class_}: Нет оценок')
        else:
            print("Такого ученика нет.")

    elif command == 12:
        print("Выход из программы.")
        break

    else:
        print("Неизвестная команда. Попробуйте снова.")

