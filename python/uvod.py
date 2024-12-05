import my_module
import pprint

def add_two(a : float = 10, b : float = 12)->float:
    return a + b

if __name__ == "__main__":
    print("\n\nHello from 'uvod.py'.\n ")
    print("Naziv fajla uvod:")
    print(__name__)
    
    # ovo je komentar
    
    # pored osnovnih tipova promenljivih
    # imamo i: list, tuple, dict
    
    # list
    # oznacava se sa '[]', ili sa 'list()'
    # u pitanju je dinamicka lista
    # lista je mutabilan tip
    my_list = list() # [] - ovo je isto
    my_list.append(666)
    my_list.append('asdas')
    
    # pristup elementima, indeksiranje ide od 0
    # print(my_list[1])
    
    # mutabilnost
    my_2nd_list = my_list.copy()
    print(my_list)
    
    my_2nd_list[1] = 'jgkhlj'
    print(my_list)
    
    # --- tuple ---
    # uredjena n-torka
    # sve isto kao i lista
    # nije mutabilan, konstanta je
    my_tuple = tuple(my_list)
    
    # zamena vrednosti dve promenljive
    a = 10
    b = 12
    a, b = (b, a)
    
    # --- dict ---
    # recnik je definisan viticastim zagradama
    # on se sastoji od parova 'polje' : 'vrednost'
    # 'polje' moze da bude str, int, ili bilo sta drugo
    # sto je 'hashable'
    # 'vrednost' moze da bude bilo koji tip podatka
    
    my_dict = {
        "x" : 0.0,
        "y" : 1.5,
        "theta": 2.6,
        "pid": {
            "Kp": 1,
            "Ki": 0.1,
            "Kd": 0.5
        }
    }
    
    print(my_dict["pid"]["Kp"])
    
    my_dict["akjshd"] = [1,2,3,4,5]
    print(my_dict)

    rezultat = add_two(b = 1231.123)
    
    # FOR petlja
    for i in range(len(my_list)):
        print(my_list[i])
        
    print('----------------')
    
    for data in my_list:
        print(data)
        
