import random
import time


def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    
    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2
    
    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista , comienzo, medio - 1, objetivo)

if __name__ == '__main__':
    tamano_de_lista= int(input('De que tamaño quieres las lista?: '))
    objetivo = int(input('Que numero quieres encontrar? '))
    
    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])# sorted para ordenaruna lista 
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    
    
    print(lista)
    stard = time.time()
    print(f'El elmento {objetivo} {"esta" if encontrado else "no esta"} en la lista ')
    end =  time.time() 
    print (stard - end )