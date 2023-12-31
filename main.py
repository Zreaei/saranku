import time
import pandas as pd
import module.function as laptop
from module.function import clear

file_path = "database/data.csv"

# Opsi
while True:
    clear()
    print("][==========][ Selamat datang di Saranku! ][==========][\n")
    print("1. Cari Gadget")
    print("2. Tampilkan Semua Gadget")
    print("3. Keluar")

    pilihan = input("\nMasukan pilihan: ")

    if pilihan == "1":
        while True:
            clear()
            print("][==========][ Cari Gadget ][==========][\n")
            target_keyword = input("Masukan Kata Kunci: ")
            result = laptop.cari_item_csv(file_path, target_keyword)

            if not result.empty:
                clear()
                print("][==========][ Hasil Pencarian ][==========][\n")
                print(result[["id", "brand", "nama_laptop", "processor", "vga", "harga"]])
            else:
                clear()
                print(f"==[!]== Tidak Ditemukan Laptop {target_keyword} ==[!]==\n")
                input("Tekan enter untuk kembali....")
                continue
            
            print("\n1. Urutkan Berdasarkan Harga")
            print("2. Cek Detail Gadget")
            print("3. Kembali")

            pilihan = input("\nMasukan pilihan: ")

            if pilihan == "1":
                while True:
                    clear()
                    print("][==========][ Hasil Pencarian ][==========][\n")
                    print(result[["id", "brand", "nama_laptop", "processor", "vga", "harga"]])\
                    
                    print("\n1. Urutkan Berdasarkan Harga Terendah")
                    print("2. Urutkan Berdasarkan Harga Tertinggi")
                    print("3. Kembali")

                    pilihan = input("\nMasukan pilihan: ")

                    if pilihan == "1":
                        clear()
                        print("][==========][ Harga Terendah ][==========][\n")
                        sorting = laptop.sort_gadget(result, 1)
                        print(sorting)
                        
                        print("\n1. Cek Detail Laptop")
                        print("2. Kembali")

                        pilihan = input("\nMasukan pilihan: ")

                        if pilihan == "1":
                            clear()
                            id = input("Masukan id: ")
                            laptop.detail_search(result, id)
                            input("\nTekan enter untuk kembali....")
                            break
                        elif pilihan == "2":
                            break

                    elif pilihan == "2":
                        clear()
                        print("][==========][ Harga Tertinggi ][==========][\n")
                        sorting = laptop.sort_gadget(result, 2)
                        print(sorting)
                        print("\n1. Cek Detail Laptop")
                        print("2. Kembali")

                        pilihan = input("\nMasukan pilihan: ")

                        if pilihan == "1":
                            id = input("Masukan id: ")
                            laptop.detail_search(result, id)
                            input("\nTekan enter untuk kembali....")
                            break
                        elif pilihan == "2":
                            break
                    elif pilihan == "3":
                        break
                    else:
                        clear()
                        print("==[!]== Masukan Inputan Yang Valid! ==[!]==")
                        time.sleep(2)
                 
            elif pilihan == "2":
                id = input("Masukan id: ")
                clear()
                print("][==========][ Detail Laptop ][==========][\n")
                laptop.detail_search(result, id)
                input("\nTekan enter untuk kembali....")
            elif pilihan == "3":
                continue
            else:
                clear()
                print("==[!]== Masukan Inputan Yang Valid! ==[!]==")
                time.sleep(2)

    elif pilihan == "2":
        while True:
            clear()
            print("][==========][ List Gadget ][==========][\n")
            laptop.view_gadget(file_path)
            print("\n1. Urutkan Berdasarkan Harga")
            print("2. Cek Detail Gadget")
            print("3. Kembali")

            pilihan = input("\nMasukan pilihan: ")

            if pilihan == "1":
                while True:
                    clear()
                    print("1. Urutkan Berdasarkan Harga Terendah")
                    print("2. Urutkan Berdasarkan Harga Tertinggi")
                    print("3. Kembali")
                    pilihan = input("\nMasukan pilihan: ")

                    if pilihan == "1":
                        clear()
                        laptop.sort_view_gadget(file_path, 1)
                        input("\nTekan enter untuk kembali....")
                        clear()
                        break
                    elif pilihan == "2":
                        clear()
                        laptop.sort_view_gadget(file_path, 2)
                        input("\nTekan enter untuk kembali....")
                        clear()
                        break
                    elif pilihan == "3":
                        clear()
                        break
                    else:
                        clear()
                        print("==[!]== Masukan Inputan Yang Valid! ==[!]==")
                        time.sleep(2)

            elif pilihan == "2":
                id = input("\nMasukan id berdasarkan gadget yang dipilih: ")
                clear()
                df = pd.read_csv(file_path)
                selected_columns = ['brand', 'nama_laptop', 'processor', 'vga', 'monitor', 'harga']
                laptop.detail_view(df, id, selected_columns)
                input("\nTekan enter untuk kembali....")
            elif pilihan == "3":
                break
            else:
                clear()
                print("==[!]== Masukan Inputan Yang Valid! ==[!]==")
                time.sleep(2)

    elif pilihan == "3":
        clear()
        break
    else:
        clear()
        print("==[!]== Masukan Inputan Yang Valid! ==[!]==")
        time.sleep(2)
        continue