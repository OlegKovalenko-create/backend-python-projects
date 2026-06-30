from utils import load, save

print("\n=== ЗАПИСЬ В ФАЙЛ ===")

data = load()

name = input("Имя: ")
age = input("Возраст: ")

data.append([name, age])

save(data)

print("Сохранено!")
print(data)