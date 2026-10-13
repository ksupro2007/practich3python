import math
print ('введите х и у')
x = float(input('введите х'))
y = float(input('введите у'))
if x >= 0 and y >=0 and y <=0.5 and y <= math.sin(x) :
    print ('точка принадлежит заштрихованной области')
else:
    print('точка не принадлежит заштрихованной области')