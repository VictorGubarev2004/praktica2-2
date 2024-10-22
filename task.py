def task0(): 
	print("Задачи::") 
	print("№1: Определение скорости") 
	print("№2: Определение массы")
	print("№3: Определение температуры по Цельсию") 
	print("№4: Определение работы") 
	print("№5: Определение кинетической энергии") 
	print("№6: Определение потенциальной энергии") 
	print("№7: Определение давления") 
	print("№8: Определение теплоты") 
	print("№9: Определение частоты") 
	print("№10: Определение объема") 
	print("q: Выход") 
	return input("Введите номер задачи или 'q' для выхода: ")
def task1():
	distance = float(input("Введите расстояние в километрах: "))
	time = float(input("Введите время в часах: "))
	speed = distance / time
	print(f"Скорость: {speed} км/ч")
def task2():
	force = float(input("Введите силу в Ньютонах: "))
    	acceleration = float(input("Введите ускорение в м/с^2: "))
    	mass = force / acceleration
	print(f"Масса: {mass} кг")
def convert_temperature():
	fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
    	celsius = (fahrenheit - 32) * 5.0 / 9.0
	print(f"Температура: {celsius} °C")

def main():
	while True:
		choice = task0()
		if choice == "q":
			break
		elif choice == "1":
			task1()
		elif choice == "2":
			task2()
		elif choice == "3":
			task3()
		else:
			print("Эта задача пока не решена. Выберите другую.")
if __name__ == "__main__":
	main()

