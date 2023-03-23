#Probando math
import math

a = 11; 
b = 7; 
c = 3;

determinante = b*b -4*a*c

if determinante < 0:
    print("Determinante negativo")
else:
    raiz1 = (-b+ (math.sqrt(determinante)))/(2*a)
    raiz2 = (-b- (math.sqrt(determinante)))/(2*a)
    print(raiz1)
    print(raiz2)

mayor = a
if a<b and b>c:
    mayor = b
elif c>b and c>a:
    mayor = c

print("El mayor es:",mayor)

lista = [2,6,7,8,1,3,6]

par = 0
impar = 0


for i in lista:
    if i%2 == 0:
        par=par+1
    else:
        impar = impar+1
        
print("La cantidad de pares es:", par);        
print("La cantidad de impares es:", impar);        











