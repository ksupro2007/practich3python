print ('введите a, b, f')
a = int(input('введите а'))
b = int(input('введите b'))
f = int(input('введите f'))
d = False
while d != True:
    if a == 0:
        print("а не должно быть равно 0!")
        a = int(input('введите а'))
        d = False
    else:
        o = (a + b - f / a) + f * a * a - (a + b)
        d = True
print(o)