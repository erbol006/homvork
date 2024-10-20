mentors = ['Тимур', 'Арсен', 'Гулина', 'Даниель']

while True:

    command = input('''Выберите команду:(1)Добавление (2)Изменение (3)Удаление (4)Выход''')
    if command == '1':
        if len(mentors) >= 10:
            print("Список менторов полон.")
        else:
            new_name = input("Введите имя нового ментора: ").strip()

            if len(new_name) > 15:
                print("Имя не должно превышать 15 символов.")
            elif new_name in mentors:
                print("Такое имя уже есть в списке.")
            else:
                mentors.append(new_name)
                print(f"Ментор '{new_name}' добавлен.")

    elif command == '2':
        old_name = input("Введите имя ментора для замены: ").strip()

        if old_name not in mentors:
            print("Такого ментора нет в списке.")
        else:
            new_name = input("Введите новое имя ментора: ").strip()

            if len(new_name) > 15:
                print("Имя не должно превышать 15 символов.")
            else:
                mentors[mentors.index(old_name)] = new_name
                print(f"Ментор '{old_name}' заменен на '{new_name}'.")

    elif command == '3':
        remove_name = input("Введите имя ментора для удаления: ").strip()

        if remove_name not in mentors:
            print("Такого ментора нет в списке.")
        else:
            mentors.remove(remove_name)
            print(f"Ментор '{remove_name}' удален.")

    elif command == '4':
        print("Выход из программы.")
        break

    else:
        print("Неверная команда. Попробуйте снова.")
https://github.com/erbol006/homvork/tree/main/0708208205