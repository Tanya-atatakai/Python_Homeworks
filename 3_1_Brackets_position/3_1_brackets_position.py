""" Программа считывает введенную пользователем строку и определяет правильное
расположение скобочек вида '( ) [ ] { }'. Если скобочки расставленны верно, то
ответ "yes". Если закрывающей скобки нет - ответ "-1", если скобка ошибочная,
выводится ее положение в строке (начиная с нуля). Отсутствие любых скобок
расценивается как правильно расположенные скобки."""

s=input('Введите строку ')
all_brackets = [] 
opening_brackets = ('{', '[', '(')
closing_brackets = ('}', ']', ')')
wrong_bracket = None #номер неверной скобочки
i=0
if len(s) != 0:
    for symbol in s:   
        if symbol in opening_brackets:
            all_brackets.append(symbol)
            i+=1
        elif symbol in closing_brackets:
            if all_brackets and opening_brackets.index(all_brackets.pop()) != closing_brackets.index(symbol):
                wrong_bracket = s.index(symbol)
                break
        i+=1
    if wrong_bracket: print(wrong_bracket) #не знаю, нормально ли так писать условия, либо надо описать исключение? тот же вопрос в задании №5
    elif all_brackets : print (-1)
    else: print('yes')
else:
    print ("Строка пуста")
