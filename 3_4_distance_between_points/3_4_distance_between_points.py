def distinct (x1, y1, x2, y2):
    """ функция возвращает расстояние между двумя точками """
    return ((x2-x1)**2+(y2-y1)**2)**0.5

x = []
y = []
d = []

f = open('points.txt', 'r')
for line in f:   
    x_dots, y_dots = line.split(" ")
    x.append(float(x_dots))
    y.append(float(y_dots))
count = len(x)
print(x)
print(count)
f.close()
max_distance = min_distance = distinct(x[0],y[0],x[1],y[1])
dist = open('dist.txt', 'w') #в этотй файл пишу две координаты точек и расстояние между ними
for i in range(0, count-2):
    for j in range(i+1, count-1):
        p = distinct(float(x[i]),float(y[i]),float(x[j]),float(y[j]))
        d.append(p)
        dist.write(str(x[i]) + " " + str(y[i]) + " " + str(x[j]) + " " + str(y[j]) + " " + str(d[i]) + '\n')
        if min_distance > d[i]:
            min_distance = d[i]
        if max_distance < d[i]:
            max_distance = d[i]            
dist.close()
print("Минимальное расстояние между точками: " + str(min_distance))
print("Максимальное расстояние между точками: " + str(max_distance))







            
            
            

    

