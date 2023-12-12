import database.data_laptop as laptop

gadgets = laptop.dummy_laptop_database

def detail_gadget():
    for gadget in gadgets:
        for key, value in gadget.items():
            print(f"{key}: {value}")
        print("\n")
        
detail_gadget()