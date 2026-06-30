from logic import TaskManager

tm = TaskManager()

while True:
    print("\n=== МЕНЕДЖЕР ЗАДАЧ ===")
    print("1 - добавить задачу")
    print("2 - показать задачи")
    print("3 - удалить задачу")
    print("0 - выход")

    choice = input("Выбери действие: ")

    if choice == "1":
        task = input("Введи задачу: ")
        tm.add(task)

    elif choice == "2":
        tm.show()

    elif choice == "3":
        tm.show()
        num = input("Какую удалить? (номер): ")
        tm.delete(num)

    elif choice == "0":
        print("Выход из программы")
        break

    else:
        print("Неверный ввод")