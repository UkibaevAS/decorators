import random


def sum_args_1(x1, x2, x3, x4, *args, **kwargs):
    temp = x1 + x2 + x3 + x4
    temp += sum(args[:2]) if len(args) >= 2 else sum(args)
    if len(kwargs) != 0:
        data = list(kwargs.items())
        temp += data[random.randint(0, len(kwargs) - 1)][1]

    return temp

print(sum_args_1(1, 2, 3, 4, 5, 6, 7, 10, d=10, e=100, f=1000))
