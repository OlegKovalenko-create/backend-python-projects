class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)
        print("Добавлено!")

    def show(self):
        if len(self.tasks) == 0:
            print("Список пуст")
            return

        print("\nТВОИ ЗАДАЧИ:")
        for i in range(len(self.tasks)):
            print(str(i + 1) + ". " + self.tasks[i])

    def delete(self, num):
        try:
            num = int(num)
            removed = self.tasks.pop(num - 1)
            print("Удалено:", removed)
        except:
            print("Ошибка удаления")