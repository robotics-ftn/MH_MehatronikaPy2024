import moj_modul

def sum(a : float, b : float)->float:
    return a + b

def main():
    # list
    
    list1 = []
    list2 = list()
    
    # lista je:
    # mutabilna
    # dinamicki promenljiva
    
    # tuple
    # uredjena n-torka
    # konstantan - nepromenljiv - nemutabilan
    tuple1 = tuple()
    tuple2 = ()

    tuple3 = (1,2,3,4)
    a,b,c,d = tuple3
    a,b = (b,a)
    
    # recnik (dictionary)
    # sastoji se od parova: kljuc-vrednost
    # kljuc je najcesce 'str' tipa
    # vrednost moze da bude bilo sta, ukljucujuci i recnik
    
    moj_recnik = {}
    moj_recnik2 = dict()
    
    my_dict = {}
    for i in range(10):
        my_dict[f"id_{i}"] = {
            "x": i,
            "y": i*i,
            "theta": 3.14*i
        }
    # print(my_dict)
    
    config = {
        "pid": {
            "kp": 10,
            "ki": 0.1,
            "Kd": 0.2
        },
        "motor": {
            "max_vel": 1,
            "max_acc": 2.5,
        }
    }
    
    moj_modul.print_nesto()
    
    
    
    

if __name__ == "__main__":
    main()
