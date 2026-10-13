print('введите стороны треугольника a,b,c')
a = float(input('введите а'))
b = float(input('введите b'))
c = float(input('введите с'))
if c>=a and c>=b:
    d = a**2+b**2-c**2
elif a>=b and a>=c:
    d = b**2+c**2-a**2
else:
    d=c**2+a**2-b**2
if d>0:
    print('треугольник остроугольный')
elif d==0:
    print('треугольник прямоугольный')
else:
    print('треугольник тупой')