archivo= open('archivo.txt','r')
for linea in archivo.readlines():
    print(linea)
archivo.close()

#Rudimentario sistema de persistencia de datos. Siempre que pongamos este programa se guardan los programas
#que tengamos en el archivo.txt