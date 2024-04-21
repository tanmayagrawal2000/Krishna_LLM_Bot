import re
QUOTE = '>'

def filter_user_number(input_string):
    digits = ''.join(filter(str.isdigit, input_string))
    integer_value = int(digits)
    return integer_value

def add_linebreak_and_quote(string, enclosure='"'):
    pattern = re.compile(r'({}.*?{})'.format(re.escape(enclosure), re.escape(enclosure)))
    replaced_string = re.sub(pattern, lambda match: "\n" + QUOTE + " " + match.group(1) + "\n", string)
    return replaced_string