test_list = [-1, 3, -4, 5, 1, -6, 2, 1]

for index, element in enumerate(test_list):
    sum_prefix = sum(test_list[:index])
    sum_suffix = sum(test_list[index+1:])
    if sum_prefix == sum_suffix:
        print(f"equilibrium: {index}")
