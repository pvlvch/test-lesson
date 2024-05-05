x = input("Введите пример: ")
def main(x):
    example = x.split()
    if len(example) != 3 or example[1] not in ['+', '-', '*', '/']:
        print("Неправильный ввод, введите по примеру выше")
        return
    try:
        num1 = int(example[0])
        num2 = int(example[2])
    except ValueError:
        print("Вводите только числа")
        return
    if num1 < 1 or num1 > 10 or num2 < 1 or num2 > 10:
        print("Вводные числа только от 1 до 10")
        return
    if example[1] == "+":
        result = num1 + num2
    elif example[1] == "-":
        result = num1 - num2
    elif example[1] == "*":
        result = num1 * num2
    elif example[1] == "/":
        result = num1 // num2

    print(f"{num1} {example[1]} {num2} = {result}")


main(x)
