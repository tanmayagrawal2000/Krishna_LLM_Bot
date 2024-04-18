def filter_user_number(input_string):
    digits = ''.join(filter(str.isdigit, input_string))
    integer_value = int(digits)
    print(integer_value)