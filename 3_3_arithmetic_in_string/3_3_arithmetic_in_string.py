expression = ''
bool = False
calculated_symbols = (' ','-','+','*','/','.','(',')','0','1','2','3','4','5','6','7','8','9')
s = input("Введите текст и арифметические выражения ")
if len(s) != 0:
    for line in s:
        if line in calculated_symbols:
            expression += line
        elif len(expression) != 0:
            print(expression.strip() + '=' + str(eval(expression)))
            bool = True
            expression = ''
else:
    print("Строка пуста!")

if bool == False or len(expression) != 0:
    print(expression.strip() + ' = ' + str(eval(expression)))

