nama = input("Input Nama Pembeli: ")
no_hp = int(input("Input No. Handphone: "))
jurusan = input("Input Jurusan [SBY/BL/LMP]: ")
jumlah = int(input("Masukan Jumlah Beli: "))

if jurusan.upper() == "SBY":
    kota = "Surabaya"
    harga = 300000
elif jurusan.upper() == "BL":
    kota = "Bali"
    harga = 350000
elif jurusan.upper() == "LMP":
    kota = "Lampung"
    harga = 500000
else:
    print("Jurusan tidak tersedia.")
    harga = 0

if jumlah >= 3:
    potongan = 0.1  
else:
    potongan = 0 

if harga > 0:
    total_harga = (jumlah * harga) * (1 - potongan)
    potongan_harga = (jumlah * harga) * potongan

    print("--------------------------------------------------------------------")
    print("                        PENJUALAN TIKET BUS                         ")
    print("--------------------------------------------------------------------")
    print("Nama Pembeli: " + nama)
    print("No HP: " + str(no_hp))
    print("Kode Jurusan Yang Dipilih: " + jurusan)
    print("Nama Kota Tujuan: " + kota)
    print(f"Harga Tiket: Rp {harga:,.0f}")
    print("Jumlah Beli: ", jumlah)
    print("--------------------------------------------------------------------")
    print("                               BAYAR                                ")
    print("--------------------------------------------------------------------")
    print(f"Potongan: Rp {potongan_harga:,.0f}")
    print(f"Total Harga: Rp {total_harga:,.0f}")
    

    uang_bayar = int(input("Masukan Uang Bayar : "))
    
    kembali = uang_bayar - total_harga
    if uang_bayar >= total_harga:
        print(f"Uang Kembali: Rp {kembali:,.0f}")
    else:
        print("Uang Tidak Cukup")
else:
    print("Tidak ada harga karena inputan salah.")
