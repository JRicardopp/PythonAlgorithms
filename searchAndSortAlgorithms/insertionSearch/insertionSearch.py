import random


def insertion_search(messy_list):
    for indice in range(1, len(messy_list)):  
        curren_value =  messy_list[indice] 
        curren_position =  indice  
        
        while curren_position > 0 and messy_list[curren_position - 1] > curren_value:
            messy_list[curren_position] = messy_list[curren_position - 1]
            curren_position -= 1
            
        messy_list[curren_position] = curren_value 
        
    return messy_list
    
    
if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño la lista? ' ))
    
    messy_list = [random.randint(0, 100) for i in range (tamano_lista)]
    print(messy_list)
    
    ordered_list = insertion_search(messy_list)
    print(ordered_list)
    
    
