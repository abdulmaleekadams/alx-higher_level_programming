def magic_calculation(a, b):
    add = __import__('magic_calculation_102', fromlist=('add', 'sub')).add
    sub = __import__('magic_calculation_102', fromlist=('add', 'sub')).sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

