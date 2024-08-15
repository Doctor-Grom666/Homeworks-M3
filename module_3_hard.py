data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

summa = 0


def calculate_structure_sum(structure):
    global summa
    for i in structure:
        if isinstance(i, int):
            summa += i
        elif isinstance(i, str):
            summa += len(i)
        elif isinstance(i, list):
            calculate_structure_sum(i)
        elif isinstance(i, dict):
            calculate_structure_sum(i.values())
            calculate_structure_sum(i.keys())
        elif isinstance(i, tuple):
            calculate_structure_sum(i)
        elif isinstance(i, set):
            calculate_structure_sum(i)
    return summa


result = calculate_structure_sum(data_structure)
print(result)
