def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str(str_number)) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    return first
result = get_multiplied_digits(774051)
print(result)
