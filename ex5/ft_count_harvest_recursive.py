def ft_count_harvest_recursive():
    count = int(input("Days until harvest: "))
    i = 0
    ft_recursion(count, i)


def ft_recursion(count, i):
    if count == i:
        print("Harvest time!")
    else:
        i += 1
        print("Day", i)
        ft_recursion(count, i)
