from mypackage.module1 import read_baggage,find_baggage
filename = "Bagazh.txt"
baggage = read_baggage(filename)
t = float(input("Введите t: "))
result, average_weight = find_baggage(baggage, t)
print(f"\nОбщий средний вес одной вещи: {average_weight:.2f} кг")
print("\nПодходящий багаж:")
if len(result) == 0:
    print("Такого багажа нет.")
else:
    for count, weight, average in result:
        print(
            f"Количество вещей: {count}, "
            f"общий вес: {weight:.2f} кг, "
            f"средний вес вещи: {average:.2f} кг"
        )