import re

""" ниже преобразования встроенными функциями """

url_start = ('www.', 'http://', 'https://')
url_ends = ('.ru', '.com', '.рф', '.org', '.net')


def is_it_url (s):
    """ поиск строки, начинающейся с url_start и заканчивающейся url_ends """
    for something in url_start:
        if s.startswith(something):
            for anything in url_ends:
                if s.endswith(anything):
                    return True
                #else:
                    #return False

    

def is_it_email (s):
    """ поиск строки, имеющей одну собачку и домен из url_ends """
    if s.find('@') != -1:
        for something in url_ends:
            if s.endswith(something):
                return True
            #else:
                #return False


def is_it_threedigits (s):
    if len(s)>3 and s.isdigit():
        return True
    else: return False


s = input('Введите строку ')
new_string = ' '
print('Преобразования встроенными функциями... ')
strings = s.split(' ')
for string in strings:
    replace = ''
    if is_it_url(string):
        replace = '[ссылка запрещена]'    
    elif is_it_email(string):
        replace = '[контакты запрещены]'
    elif is_it_threedigits(string):
        continue       
    if len(replace) > 0:
        new_string += replace + ' '
    else:
        new_string += string + ' '

print(new_string[1] + new_string[2:].lower()) #тут первым символом я так поняла может быть символ в любом регистре

""" ниже преобразования страшными регулярками """

print('Преобразование с помощью регулярный выражений... ')
new_string_regular = re.sub(r'\w',s[0], s[0]) + re.sub(r'\w', lambda get_low: get_low.group(0).lower(), s[1:])

print(new_string_regular)       

