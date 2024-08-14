def max_school(kwargs):
    max_num = 1
    max_name = ""
    for key, val in kwargs.items():
        max1 = max(val)
        if max1 > max_num:
            max_num = max1
            max_name = key

    return (max_name, max_num)



