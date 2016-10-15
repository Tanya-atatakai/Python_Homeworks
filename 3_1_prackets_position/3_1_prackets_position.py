""" Программа считывает введенную пользователем строку и определяет правильное
расположение скобочек вида '( ) [ ] { }'. Если скобочки расставленны верно, то
ответ "yes". Если закрывающей скобки нет - ответ "-1", если скобка ошибочная,
выводится ее положение в строке (начиная с нуля). Отсутствие любых скобок
расценивается как правильно расположенные скобки."""

s=input('Введите строку ')
square = 0 # счетчик для квадратных скобок
angle = 0 # счетчик для круглых скобок
curve = 0 # счетчик для фигурных скобок
wrongbracket = None #номер неверной скобочки
i=0
while i<len(s) :
    #в цикле проверяется каждый элемент строки. счетчик каждой скобочки увеличивается, если скобка открылась,
    #и уменьшается, если закрылась. Если какой-то из счетчиков становится отрицательным - значит появилась лишняя скобочка
	###в общем в интернете почитала, что вместо свич-кейсов в питоне можно использовать словари. пробовала создать словарь формата
	###f = {'(' : square += 1, ')' square -= 1, ...} и т.д., но вместо значения ключа функция в таком виде приниматься не хотела.. 
	###нужно отдельно создавать функции и их все передавать, как ты делал в примере про перевод слов во множественное число? или можно сделать как-то проще и короче?
    if s[i] =='[': square += 1
    elif s[i] ==']' : square -= 1
    elif s[i] == '(' : angle+=1
    elif s[i] == ')': angle -= 1 
    elif s[i] =='{' : curve += 1
    elif s[i] =='}' : curve -= 1
    if square < 0 or angle < 0 or curve < 0 :
        wrongbracket = i
        break
    i+=1
if wrongbracket: print(wrongbracket) #не знаю, нормально ли так писать условия, либо надо описать исключение? тот же вопрос в задании №5
elif square > 0 or angle > 0 or curve > 0 : print (-1)
else: print('yes')
