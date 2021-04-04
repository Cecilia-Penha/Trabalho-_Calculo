import math
#Trabalho aplicado 1 - Cecília Penha
#Equação 1
def func(x):
    f = (x*x*x)-math.cos(x)-x+1
    return f
def valor(a,b,f1,f2):
    if(f1==0):
        print("raiz = %f\n" %a)
        return
    if(f2==0):
        print("raiz = %f\n" %b)
        return
    if(f1>0 and f2<0):
        print("a equacao tem pelo menos um solucao nesse intervalo: [%f,%f]\n" %(a,b))
        return
    elif(f1<0 and f2>0):
        print("a equacao tem pelo menos uma solucao nesse intervalo: [%f,%f]\n" %(a,b))
        return
    else:
        print("nao e possivel afirmar que existe uma solucao nesse intervalo, tente outros dois numeros")
        return
a = float(input("digite a:\n"))
b = float(input("digite b:\n"))
f1 = func(a)
f2 = func(b)
r = valor(a,b,f1,f2)
print(r)
    