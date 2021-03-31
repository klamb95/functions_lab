def return_10():
    return 10

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

def length_of_string(word):
    return len(word)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

months = ['January', 'February', 'March', 'April', 'May', 
'June', 'July', 'August', 'September', 'September',
'October', 'November', 'December']

def number_to_full_month_name(number):
    return months[number - 1]

months_short = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

def number_to_short_month_name(number):
    return months_short[number - 1]

def vol_of_cube(size):
    return (size * size * size)