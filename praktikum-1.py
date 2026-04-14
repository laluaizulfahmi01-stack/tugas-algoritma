mahasisiwa=[]
def tampilkan_data():
    if len (mahasisiwa)==0:
        print("\ndata kosong!")
    else:
        print("\nDaftar Mahasisiwa!")
        for i, mhs in enumerate(mahasisiwa, start=1):
            print(f"{i}.Nama: {mhs ['nama']}, Nilai:{mhs['nilai']}")

def tambaha_data():
    namam = input ("masukkan nama mahasiiswa:")
    nilai = int (input ("masukkan nilai mahasiiswa:"))
    data = {
        "nama" : nama,
        "nilai": nilai
    }
    mahasisiwa.append(data)
    print("Data berhasil ditambhakan!")
def hapus_data():
    tampilkan_data()
    if len (mahasisiwa) > 0:
        index = int (input("pilih nomor yang akan dihapus:"))-1

        if 0 <= index < len(mahasiswa):
            mahaisiwa.pop(index)
            print("Data berhasil dihapus!")
        else:
            print("index tidak valid!")
def cari_mahasisiwa():
    keyword = input ("masukkan nama yang akan dicari: ").lowwr()
    ditemukan= False

    for mhs in mahasisiwa:
        if keyword in mhs["nama"].lower():
            print(f"Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")
            ditemukan = True
    if not ditemukan:
        print("Data tidak ditemukan!")

def rata_rata():
    if len (mahasiswa)== 0:
        print ("belum ada data.")
    else:
        total = 0
        for mhs in mahasisiwa:
            total += mhs ['nilai']

        rata = total / len (mahasisiwa)
        print (f"rata-rata nilai: {rata:.2f}")

#
while True: 
    print ("\n=== Menu ===")
    print ("1. Tampilkan Data")
    print ("2. Tambah Data")
    print ("3. Hapus Data")
    print ("4. Cari Mahasiswa")
    print ("5. Rata-rata Nilai")
    print ("6. Keluar")

    pilihan = input ("pilih menu (1-6):")
    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        cari_mahasisiwa()
    elif pilihan == "5":
        rata_rata()
    elif pilihan == "6":
        print("Terima kasih!")
        break
    else:
        print("pilihan tidak valid!")