"""Input cipher key string, get user input on route direction as dict value."""
col_order = """1 3 4 2"""
key = dict()
cols = [int(i) for i in col_order.split()]
for col in cols:
    while True:
        key[col] = input("Direction to read Column {} (u = up, d = down): "
                         .format(col).lower())
        if key[col] == 'u' or key[col] == 'd':
            break
        else:
            print("Input should be 'u' or 'd'")

    print("{}, {}".format(col, key[col]))
