import math

k = str(input('Введите названия вашей фигуры:'))

if k =='Треугольник':

    a = int(input('Введите сторону A:'))

    b = int(input('Введите сторону B:'))

    c = int(input('Введите сторону C:'))

    p = (a+b+c)/2       
    
    s = math.sqrt((p*(p-a)*(p-b)*(p-c)))

elif k =='Прямоугольник':

    a = int(input('Введите сторону A:'))

    l = int(input('Введите сторону L:'))
    
    d = int(input('Введите сторону D:'))
    
    b = int(input('Введите сторону B:'))


    p = (a+b+d+l)/2       
    
    s=a*l*d*b  
    

elif k =='квадрат':

    a = int(input('Введите сторону A:'))

    b = int(input('Введите сторону B:'))

    l = int(input('Введите сторону L:'))
    
    d = int(input('Введите сторону D:'))

    p = (a+b+l+d)/2       
    
    s=a*b*l*d
    
print ('Площадь фигуры будет состовлять:', s)