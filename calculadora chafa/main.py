name = input('Dime tu nombre: ')
print ('Hola ' + name + ', mucho gusto. ¿Necesitas hacer algún calculo?, tons toma la calculadora más malota de todo Occidente')


opcion = 0
n1 = int(input('Primer número: '))
n2 = int(input('Segundo número: '))
while True:
    print ("""
    ¿Qué quieres hacer?
    1) Sumar
    2) Restas
    3) Multiplicar
    4) Dividir
    5) Sorprendeme
    6) Salir de la calculadora
    """)
    option = int(input('Dime el tipo de operación que quieres hacer: '))

    if option == 1:
        print (' ')
        print ('Resultado:',n1 + n2)
    elif option == 2:
        print (' ')
        print ('Resultado:',n1 - n2)
    elif option == 3:
        print (' ')
        print ('Resultado:',n1 * n2)
    elif option == 4:
        print (' ')
        print ('Resultado:',n1 / n2)
    elif option == 5:
        print (' ')
        print ('https://matias.ma/nsfw/ copia y pega esto en el navegador')
    elif option == 6:
        print ('Regrese pronto')
        break