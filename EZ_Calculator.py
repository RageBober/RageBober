#Разработка простого калькулятора.
num_a = int(input("Введите число А: "))
num_b = int(input("Введите число Б: "))
deistvie = input("Что нужно сделать?(символ) ")
otvet = 0
if deistvie == "-":
    otvet = num_a - num_b
    print(f"результат чисел {otvet}")
elif deistvie == "+":
    otvet = num_a + num_b
    print(f"результат чисел {otvet}")
elif deistvie == "*":
    otvet = num_a * num_b
    print(f"результат чисел {otvet}")
elif deistvie == "*":
    otvet = num_a / num_b
    print(f"результат чисел {otvet}")