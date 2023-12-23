import csv
import pandas as pd

file_path = "database/data.csv"

# View Gadget
def view_gadget(file_path):
    # Membaca file CSV
    df = pd.read_csv(file_path)
    columns = ["brand", "nama_laptop", "processor", "vga", "harga"]
    view_columns = df[columns]
    # Menampilkan DataFrame
    print(view_columns)

# Search Gadget
def cari_item_csv(file_path, target_keyword):
    try:
        # Membaca file CSV ke dalam DataFrame
        df = pd.read_csv(file_path)

        # Menerapkan pencarian menggunakan pandas
        matching_rows = []  # Inisialisasi list untuk menyimpan baris yang cocok

        # Loop melalui setiap baris DataFrame
        for index, row in df.iterrows():
            # Loop melalui setiap sel dalam baris
            for cell in row:
                # Pemeriksaan kata kunci pencarian
                if target_keyword.lower() in str(cell).lower():  #.lower berguna untuk menghilangkan huruf kapital contoh: Asep Narindi menjadi asep narindi
                    matching_rows.append(row)  # Menambahkan baris yang cocok ke dalam list
                    break  # Keluar dari loop jika sudah menemukan satu sel yang cocok

        result_df = pd.DataFrame(matching_rows, columns=df.columns)  # Membuat DataFrame dari list

        # Menampilkan hasil pencarian
        if not result_df.empty:
            return result_df  # Menampilkan DataFrame jika ada hasil
        else:
            print(f"Tidak ditemukan informasi dengan kata kunci '{target_keyword}' dalam file.")
    except FileNotFoundError:
        print(f"File tidak ditemukan: {file_path}")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

# Sort Gadget
def sort_gadget(result, pilihan):
    if pilihan == 1:
         # Mengurutkan DataFrame berdasarkan kolom 'harga' secara ascending
        df_sorted = result.sort_values(by='harga')
        # Menampilkan hasil
        print(df_sorted)

    elif pilihan == 2:
         # Mengurutkan DataFrame berdasarkan kolom 'harga' secara descending
        df_sorted = result.sort_values(by='harga', ascending=False)
        # Menampilkan hasil
        print(df_sorted)

# Detail Gadget v2
def details(df, selected_id):
    # Input untuk memilih satu baris berdasarkan ID
    if selected_id and selected_id.isdigit():
        selected_row = df[df['id'] == int(selected_id)]
        if not selected_row.empty:
            # Menampilkan informasi dengan format yang diinginkan
            print("\nInformasi Laptop:")
            print(f"Brand: {selected_row['brand'].values[0]}")
            print(f"Nama Laptop: {selected_row['nama_laptop'].values[0]}")
            print(f"Processor: {selected_row['processor'].values[0]}")
            print(f"VGA: {selected_row['vga'].values[0]}")
            print(f"RAM: {selected_row['ram'].values[0]}")
            print(f"Penyimpanan: {selected_row['storage'].values[0]}")
            print(f"Monitor: {selected_row['monitor'].values[0]}")
            print(f"Harga: {selected_row['harga'].values[0]}")
        else:
            print(f"Tidak ada baris dengan ID {selected_id}.")
    else:
        print("ID yang dimasukkan tidak valid.")