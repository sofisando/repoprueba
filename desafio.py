print ('A continuacion escriba nombre de libros, para finalizar el ingreso presione Z')
biblioteca = {} 

while True:
    variable = input('Escribir el nombre del libro: ')
    if variable.upper() != 'Z': 
        archivo= open ('desafio.txt','a')  #la a lo hace append
        biblioteca[variable]=int(input('Diga el precio del libro: '))
        
    else:
        break
archivo.write(f"\n{biblioteca}") #abrimos para escribir 
archivo.close() #y luego cerramos

var = input('¿Quiere ver lo que ha guardado? s/n: ')
if var.upper() == 'S':
    print(biblioteca)
else:
    print('Arios')