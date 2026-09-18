def read_baggage(filename):
    baggage = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.split()

            if len(parts) == 2:
                count = int(parts[0])
                weight = float(parts[1])

                baggage.append((count, weight))
    return baggage

def find_baggage(baggage, t):
    # Общее количество вещей и общий вес
    total_count = sum(item[0] for item in baggage)
    total_weight = sum(item[1] for item in baggage)
    # Средний вес одной вещи среди всего багажа
    average_weight = total_weight / total_count
    result = []
    # Ищем багаж, у которого средний вес вещи
    # отличается от общего среднего не более чем на t
    for count, weight in baggage:
        average = weight / count

        if abs(average - average_weight) <= t:
            result.append((count, weight, average))

    return result, average_weight