import csv
import pandas as pd
import module.function as laptop

file_path = "database/data.csv"

# Opsi
while True:
    print("\nSelamat datang di Saranku!")
    print("1. Cari Gadget")
    print("2. Tampilkan Semua Gadget")
    print("3. Keluar")

    pilihan = int(input("\nMasukan pilihan: "))
    if pilihan == 1:
        target_keyword = input("Masukan Kata Kunci: ")
        result = laptop.cari_item_csv(file_path, target_keyword)
        print(result)
    
        print("\n1. Urutkan Berdasarkan Harga")
        print("2. Cek Detail Gadget")
        print("3. Kembali")
        print("4. Keluar")
        pilihan = int(input("\nMasukan pilihan: "))

        if pilihan == 1:
            print("\n1. Urutkan Berdasarkan Harga Terendah")
            print("2. Urutkan Berdasarkan Harga Tertinggi")
            pilihan = int(input("\nMasukan pilihan: "))
            if pilihan == 1:
                laptop.sort_gadget(result, 1)
                input("\nTekan enter untuk kembali....")
            elif pilihan == 2:
                laptop.sort_gadget(result, 2)
                input("\nTekan enter untuk kembali....")
        elif pilihan == 2:
            id = input("Masukan id: ")
            laptop.details(result, id)
            input("\nTekan enter untuk kembali....")
        elif pilihan == 3:
            continue
        elif pilihan == 4:
            break

    elif pilihan == 2:
        laptop.view_gadget(file_path)
        input("\nTekan enter untuk kembali....")
    elif pilihan == 3:
        break