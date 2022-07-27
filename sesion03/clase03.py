print("########### EJERCICIOS - CLASE 03 ###############")
print("**** Ejercicio 01 *****")
mi_var=14
if mi_var>0:
    print(mi_var,"es mayor que 0")
elif mi_var<0:
    print(mi_var,"es menor que 0")
else:
    print(mi_var,"es igual a 0")

print("")
print("**** Ejercicio 02 ****")
mi_var2a=45
mi_var2b="hola"
if type(mi_var2a) == type(mi_var2b):
    print("Son iguales las variables")
else:
    print("El tipo de dato de las variables no soy iguales")

print("")
print("**** Ejercicio 03 ****")
for i in range(1,21):
    if(i%2)==0:
        print("el numero",i, "es par")
    else:
        print("el numero",i,"es impar")

print("")
print("**** Ejercicio 04 ****")
for i in range(0,6):
    print(i,"elevado al cubo es:", i**3)
print("")
print("**** Ejercicio 05 ****")
