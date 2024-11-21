import pandas as pd


list_kode = []
list_nama = []
list_harga = []
list_jumlah = []
list_total = []

ulang = int(input("Masukan Banyaknya Jumlah Obat : "))
print("")
for i in range(ulang):
    print("Data Ke - " + str(i + 1))
    kode = input("Kode Obat (PD/PM/DD): ").upper()
    print("")

    if kode == "PD":
        nama = "Panadol"
        harga = 15000
        print(f"Nama Obat: {nama}")
        print(f"Harga Satuan: Rp {harga:,}")
    elif kode == "PM":
        nama = "Promag"
        harga = 20000
        print(f"Nama Obat: {nama}")
        print(f"Harga Satuan: Rp {harga:,}")
    elif kode == "DD":
        nama = "Bodrex"
        harga = 10000
        print(f"Nama Obat: {nama}")
        print(f"Harga Satuan: Rp {harga:,}")
    else:
        print("Kode Obat Tidak Ditemukan")
        continue

    print("")
    jumlah = int(input("Jumlah: "))
    print("")

    list_kode.append(kode)
    list_nama.append(nama)
    list_harga.append(harga)
    list_jumlah.append(jumlah)
    list_total.append(harga * jumlah)


obat = {
    "Kode Obat": list_kode,
    "Nama Obat": list_nama,
    "Harga Satuan": list_harga,
    "Jumlah": list_jumlah,
    "Total Harga": list_total,
}

data_obat = pd.DataFrame(obat)


grand_total = data_obat["Total Harga"].sum()

print("")
print("==================== Daftar Obat ===============================")
print("NO",data_obat)  
print("================================================================")
print("\033[32m" + f"Total Keseluruhan Harga: Rp {grand_total:,}"+ "\033[0m")
print("")

uang_bayar = int(input("Uang Bayar: Rp "))
if uang_bayar < grand_total:
            print("Uang bayar tidak cukup. Silakan masukkan jumlah yang benar.")
else:
            kembalian = uang_bayar - grand_total
            print("\033[32m" + f"Kembalian: Rp {kembalian:,}" + "\033[0m")
