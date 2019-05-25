import math #подключение математической библиотеки
#ввод данных задания №1
print("Введите a")
a=int(input())
print("Введите b")
b=int(input())
print("Введите c")
c=int(input())
print("Введите d")
d=int(input())
print("Введите f")
f=int(input())
if (a==0): #проверка делимости на 0
    print("Нельзя посчиать выражение!")
else:
    s=math.fabs(a-b*c*math.pow(d,3)+((math.pow(c,5)-a*a)/a+pow(f,3)*(a-213)))
    print("s = ", float(s))
lst = [1,10,2,6,9,3,4,5,8,7,11] #исходный список для задания №2
type(lst) #вывод этоого списка
proizv=1
i=0
print("Строка из нечетных чисел списка:")
while(i<len(lst)): #цикл с условием, при котором проверяется четность числа
    if lst[i] % 2==1:
        print(lst[i],end = " ")    
    if lst[i]<10:
        proizv=proizv*lst[i]
    i+=1
i=0
print("")
print("Произведение чисел, меньших 10 равно: - ",proizv)
print(sorted(lst))
def median(lst): #описание функции, находящей медианное число
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0 
        
print("Медианное число списка равно ",median(lst))   
