import moj_modul as mm

if __name__ == "__main__":
    # print("\nHello from uvod\n")
    # mm.print_module()
    
    # print(__name__)


    # Osnovni tipovi:
    # float
    # int
    # boolean
    # byte
    # list
    # tuple
    # dict

    # list
    # - mutabilnost
    # - dinamcko zauzimanje memorije
    # - indeksiranje od 0
    # - ne mora da sadrzi isti tip podataka u sebi
    
    myList = [] # list() ---> ovo je drugi nacin inicijalizacije prazne liste
    # dodavanje objekta u listu
    myList.append(13)
    myList.append("Mehatronika")
    myList.append([22, 11])
    print("\nmyList:\n{}\n{}\n".format(myList, [123,123,123,123]))
    print(f"\nmyList:\n{myList}\n{[2312,23123,12312321]}\n")
    
    list_to_add = [1, 2, 3, 4, 5]
    for i in range(0, len(list_to_add), 1):
        myList.append(list_to_add[i])
    
    # for data in list_to_add:
    #     print(data)
    
    # for i, data in enumerate(list_to_add):
    #     print(i, data)

    # prosirivanje liste drugom listom
    myList.extend([232, 16236, "asdsa"])
    print(myList)
    print()
    
    # mutabilnost
    myList2 = myList
    myList2[2] = "skjghfdjkhgkjdfhg"
    print(myList)
    
    # -----------------------
    # tuple
    # - uredjena n-torka
    # - nije-mutabilna == konstanta
    # moguca iteracija kroz tuple kao kroz listu
    
    myTuple = () # tuple() --> drugi nacin kreiranja praznog tuple-a
    myTuple = (10, 20, 15, 22, "lazar", 13, 1231)
    
    # rasclanivanje
    # a, b = myTuple
    # # zamena mesta promenljivima pomocu tuple-a
    # a, b = (b, a)
    id = myTuple.index(13)
    print(id)
    
    # -----------------
    # dict
    myDict = {} # dict() --> drugi nacin kreiranja praznog recnika
    
    # sastoji se od parova kljuc:vrednost
    
    myDict = {
        "odom":{
            "x": 0.0,
            "y": 0.0,
            "theta": 0.0
        },
        "pid": {
            "Kp": 10.0,
            "Ki": 1.0,
            "Kd": 0.25
        }
    }
    
    # pristup recniku
    print(myDict["odom"])

    # dodavanje elemenata
    myDict["config"] = [1, 2, 3, 4, 3, 2, 1] # type: ignore
    print(myDict)
    
    
    
