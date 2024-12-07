items = {
    'r': (25, 3),
    'p': (15, 2),
    'a': (15, 2),
    'm': (20, 2),
    'i': (5, 1),
    'k': (15, 1),
    'x': (20, 3),
    't': (25, 1),
    'f': (15, 1),
    'd': (10, 1),
    's': (20, 2),
    'c': (20, 2),
}


initial_points = 20
required_items = ['i']
backpack_cells = 7
best_combo = None
max_points = float('-inf')


def generate_combinations_with_replacement(elements, length):
    if length == 0:
        return [[]]
    combinations = []
    for i in range(len(elements)):
        for subcombo in generate_combinations_with_replacement(elements[i:], length - 1):
            combinations.append([elements[i]] + subcombo)
    return combinations


item_keys = list(items.keys())
combinations = generate_combinations_with_replacement(item_keys, backpack_cells)
for combo in combinations:
        flag = True
        for item in required_items:
            if item not in combo:
                flag = False
                break

            pres_points = 0
            for item in combo:
                pres_points += items[item][0]

            miss_points = 0
            for item in items:
                if item not in combo:
                    miss_points += items[item][0]
            total_points = initial_points + pres_points - miss_points
            if total_points > max_points:
                max_points = total_points
                best_combo = combo


if best_combo:
    backpack = []
    combo_list = list(best_combo)
    inventory_rows, inventory_cols = 2, 4
    for i in range(0, len(combo_list), inventory_cols):
        backpack.append(combo_list[i:i + inventory_cols])
    for row in backpack:
        print(",".join(f"[{item}]" for item in row))
    print(f"Итоговые очки выживания = {max_points}")    
else:
    print("Нет подходящих комбинаций")