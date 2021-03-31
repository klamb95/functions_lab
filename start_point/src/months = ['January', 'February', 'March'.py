months_number = ['January', 'February', 'March', 'April', 'May', 
'June', 'July', 'August', 'September', 'September',
'October', 'November', 'December']

def number_to_full_month_name(number):
    return months_number[number - 1]

def number_to_short_month_name(number):
    return number_to_full_month_name(month_number)[0:3]

print(number_to_full_month_name(1))
print(number_to_short_month_name(1))
