data_pengguna = {
    "234567": {"pin": 918918, "saldo": 1000000},
    "992299": {"pin": 458458, "saldo": 580000},
    "237788": {"pin": 765765, "saldo": 200000}
}

tagihan_data = {
    "ABC123": {"nama": "Tagihan Listrik", "jumlah": 150000},
    "DEF456": {"nama": "Tagihan Air", "jumlah": 100000},
    "GHI789": {"nama": "Tagihan Internet", "jumlah": 200000},
}

def format_rupiah(amount):
    return "Rp {:,}".format(amount).replace(",", ".")

def cek_saldo(nomor_rekening):
    if nomor_rekening in data_pengguna:
        print("******************************************************")
        print("        Saldo Anda: ", format_rupiah(data_pengguna[nomor_rekening]["saldo"]))
        print("******************************************************")
    else:
        print(" Rekening Tidak Ditemukan.")

def tarik_tunai(nomor_rekening):
    if nomor_rekening in data_pengguna:
        print("******************************************************")
        print("                     Pilih Nominal                    ")
        print("******************************************************")
        print("1. Rp 100.000")
        print("2. Rp 200.000")
        print("3. Rp 500.000")
        print("4. Rp 1.000.000")
        print("5. Rp 2.000.000")
        print("6. Lainnya")
        print("******************************************************")
        
        pilihan_nominal = input(" Pilih Nominal (1-5): ")
        if pilihan_nominal == "1":
            jumlah = 100000
        elif pilihan_nominal == "2":
            jumlah = 200000
        elif pilihan_nominal == "3":
            jumlah = 500000
        elif pilihan_nominal == "4":
            jumlah = 1000000
        elif pilihan_nominal == "5":
            jumlah = 2000000
        elif pilihan_nominal == "6":
            jumlah = int(input(" Masukkan Jumlah Penarikan: "))
        else:
            print(" Pilihan Tidak Valid.")
            

        if data_pengguna[nomor_rekening]["saldo"] >= jumlah:
            data_pengguna[nomor_rekening]["saldo"] -= jumlah
            print("******************************************************")
            print("        Penarikan Berhasil")
            print("        Sisa Saldo Anda: ", format_rupiah(data_pengguna[nomor_rekening]["saldo"]))
            print("******************************************************")
        else:
            print(" Saldo Anda Tidak Mencukupi.")
    else:
        print(" Rekening Tidak Ditemukan.")


def transfer(nomor_rekening_pengirim, nomor_rekening_tujuan, jumlah):
    if nomor_rekening_pengirim in data_pengguna and nomor_rekening_tujuan in data_pengguna:
        if data_pengguna[nomor_rekening_pengirim]["saldo"] >= jumlah:
            data_pengguna[nomor_rekening_pengirim]["saldo"] -= jumlah
            data_pengguna[nomor_rekening_tujuan]["saldo"] += jumlah
            print("******************************************************")
            print("        Transfer Berhasil")
            print("        Sisa Saldo Anda : ", format_rupiah(data_pengguna[nomor_rekening_pengirim]["saldo"]))
            print("******************************************************")
        else:
            print(" Saldo Anda Tidak Mencukupi.")
    else:
        print(" Rekening Tidak Ditemukan.")

def ganti_pin(nomor_rekening):
    if nomor_rekening in data_pengguna:
        pin_baru = int(input(" Masukkan PIN Baru: "))
        data_pengguna[nomor_rekening]["pin"] = pin_baru
        print(" PIN Berhasil Diubah.")
    else:
        print(" Rekening Tidak Ditemukan.")

def show_help():
    print("==============================================================")
    print("                    Menu Bantuan                              ")
    print("==============================================================")
    print("1. Cek Saldo - Cek rekening anda.")
    print("2. Transfer Uang - Mengirim uang ke rekening lain.")
    print("3. Tarik Tunai - Tarik tunai dari rekening anda.")
    print("4. Ganti PIN - Ganti PIN akun anda.")
    print("5. Riwayat - Melihat seluruh riwayat transaksi rekening anda.")
    print("7. Bayar Tagihan - Bayar Tagihan Rekening Anda.")
    print("8. Keluar - Keluar dari ATM.")
    print("==============================================================")


def riwayat(nomor_rekening):
    if nomor_rekening in data_pengguna:
        transactions = [
            "25/10/2024 - Tarik Tunai Rp 1.000.000",
            "23/10/2024 - Transfer Rp 500.000",
            "21/10/2024 - Setor Tunai Rp 2.000.000",
        ]
        print("******************************************************")
        print("                   Riwayat")
        for transaction in transactions:
            print(transaction)
        print("******************************************************")
    else:
        print(" Rekening Tidak Ditemukan.")

def bayar_tagihan(nomor_rekening):
    kode_bayar = input(" Masukkan Kode Bayar: ")
    if kode_bayar in tagihan_data:
        tagihan = tagihan_data[kode_bayar]
        print("******************************************************")
        print(f"        {tagihan['nama']}")
        print(f"        Jumlah Tagihan: {format_rupiah(tagihan['jumlah'])}")
        print("******************************************************")
        konfirmasi = input(" Apakah Anda ingin membayar tagihan ini? (y/n): ").lower()
        if konfirmasi == "y":
            if data_pengguna[nomor_rekening]["saldo"] >= tagihan["jumlah"]:
                data_pengguna[nomor_rekening]["saldo"] -= tagihan["jumlah"]
                print("******************************************************")
                print("        Pembayaran Berhasil")
                print("        Sisa Saldo Anda: ", format_rupiah(data_pengguna[nomor_rekening]["saldo"]))
                print("******************************************************")
            else:
                print(" Saldo Anda Tidak Mencukupi.")
        else:
            print(" Pembayaran Dibatalkan.")
    else:
        print(" Kode Bayar Tidak Ditemukan.")



def pilih_bahasa():
    print("Pilih Bahasa:")
    print("1. Bahasa Indonesia")
    print("2. English")
    pilihan_bahasa = input(" Pilih (1/2): ")
    if pilihan_bahasa == "1":
        print("Bahasa Indonesia dipilih.")
    elif pilihan_bahasa == "2":
        print("English selected.")
    else:
        print("Pilihan tidak valid.")


def transaksi_lagi():
    pilihan = input("Apakah ingin melakukan transaksi lain? (y/n): ").lower()
    return pilihan == "y"

while True:
    print("==============================================================")
    print("                  Selamat Datang di ATM                      ")
    print("==============================================================")
    pilih_bahasa()
    nomor_rekening = input(" Masukkan Nomor Rekening: ")
    pin = int(input(" Masukkan Pin Anda: "))
    print("")  
    
    if nomor_rekening in data_pengguna and data_pengguna[nomor_rekening]["pin"] == pin:
        while True:
            print("")
            print("==============================================================")
            print("                         Pilih Menu                           ")
            print("==============================================================")
            print("(1). Cek Saldo                              (5). Riwayat")
            print("(2). Transfer Uang                          (6). Informasi")
            print("(3). Tarik Tunai                            (7). Bayar Tagihan")
            print("(4). Ganti PIN                              (8). Keluar")
            print("==============================================================")
            pilihan = input(" Pilih Menu (1-8): ")
            print("")

            if pilihan == "1":
                cek_saldo(nomor_rekening)
            elif pilihan == "2":
                nomor_rekening_tujuan = input(" Masukkan Nomor Rekening Tujuan: ")
                jumlah = int(input(" Masukkan Jumlah Transfer: "))
                transfer(nomor_rekening, nomor_rekening_tujuan, jumlah)
            elif pilihan == "3":
                tarik_tunai(nomor_rekening)
            elif pilihan == "4":
                ganti_pin(nomor_rekening)
            elif pilihan == "5":
                riwayat(nomor_rekening)
            elif pilihan == "6":
                show_help()
            elif pilihan == "7":
                bayar_tagihan(nomor_rekening)
            elif pilihan == "8":
                print(" Terima kasih telah menggunakan ATM kami.")
                break
            else:
                print(" Pilihan Tidak Valid.")

            print("")
            if not transaksi_lagi():
                print("")
                print(" Terima kasih telah menggunakan ATM kami.")
                break
    else:
        print(" Nomor Rekening atau Pin Anda Salah.")