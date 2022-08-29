import random
import time

def busqueda_lineal(lista, objetivo):

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    

    return macth


if  __name__ == '__main__':
    tamano_de_lista =  int(input('De que tamaño sera la lista'))
    objetivo = int(input('Que numero quieres encontrar? '))
    
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)] 
    
    econtrado = busqueda_lineal(lista, objetivo)
    print(lista)
    stard = time.time()
    print(f'El elmento {objetivo} {"esta" if econtrado else "no esta"} en la lista ')
    end =  time.time() 
    print (stard - end )
