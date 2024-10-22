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

def main():
	while True:
		choice = task0()
		if choice == "q":
			break
		elif choice == "1":
			task1()
		else:
			print("Эта задача пока не решена. Выберите другую.")
if __name__ == "__main__":
	main()

