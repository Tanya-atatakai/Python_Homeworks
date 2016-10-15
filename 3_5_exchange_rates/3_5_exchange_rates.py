""" получение курса валют """
import urllib.request
from xml.dom import minidom #на хабре написали, что это плохая либа, мол, с выкидонами, но самую нормульную инфу (на русском) для парсинга xml я нашла только по ней. Напиши, пожалуйста, если есть лучше и где почитать

name = None
try:
    url = "http://www.cbr.ru/scripts/XML_daily.asp" #ссылка на XML с курсом вают у центробанка
    f = urllib.request.urlopen(url) #открываем ссылку
    connection = True
except urllib.error.URLError: #исключение, если ссылка не открылась
    print ("Не получается открыть ссылку, проверьте соединение с интернетом... ")
    connection = False
if connection: #не совсем уверена, что правильно\красиво исключение описала, может надо было в функцию обернуть?
    data = f.read() 
    fname = "exchange_rate.xml" 
    with open (fname, "wb") as File: #WB - writing binary, пишем в двоичном режиме ибо data представлена в bytes
        File.write(data) 
    f.close() #закрываем веб-страницу
#Кирилл, подскажи, пожалуйста, правильно ли делаю, что сначала url пишу в файл и потом этот файл анализирую
#Я не проверяла, что делается быстрее - парсинг урл или запись url в файл, а как это технически всё происходит вообще не знаю
#но подумала, что если интернет плохой, вдруг в процессе парсинг упадет, если отвалится соединение? как лучше тут делать?
    Code = input("Введите символьный код валюты ")
    parser = minidom.parse(fname)
    valute = parser.getElementsByTagName("Valute") #пишем коллекцию элементов с тегом Valute вначале файла
    for item in valute:
        charcode = item.getElementsByTagName("CharCode")[0].firstChild.data      
        if charcode ==  Code:
            name = item.getElementsByTagName("Name")[0].firstChild.data
            nominal = item.getElementsByTagName("Nominal")[0].firstChild.data
            value = item.getElementsByTagName("Value")[0].firstChild.data
    if name: # правильно ли так писать, или быдлокод и лучше тоже исключением?  
        print(nominal, " ", name, " = ", value, " рублям")
    else:
        print("Введенная валюта не найдена")
