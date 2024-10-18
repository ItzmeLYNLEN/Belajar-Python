def kalkulator():
    def tambah():
        print('1. Penjumlahan')
        a = float(input('Masukkan nilai x = '))
        b = float(input('Masukkan nilai y = '))
        c = a + b
        print('x + y = ', c)
        print('')
        tanya()

    def kurang():
        print('2. Pengurangan')
        a = float(input('Masukkan nilai x = '))
        b = float(input('Masukkan nilai y = '))
        c = a - b
        print('x - y = ', c)
        print('')
        tanya()

    def kali():
        print('3. Perkalian')
        a = float(input('Masukkan nilai x = '))
        b = float(input('Masukkan nilai y = '))
        c = a * b
        print('x * y = ', c)
        print('')
        tanya()

    def bagi():
        print('4. Pembagian')
        a = float(input('Masukkan nilai x = '))
        b = float(input('Masukkan nilai y = '))
        if b != 0:
            c = a / b
            print('x / y = ', c)
        else:
            print('Pembagian dengan nol tidak diperbolehkan.')
        print('')
        tanya()

    def tanya():
        choose = input('Apakah Anda ingin mengulang (Y/T)? ')
        if choose.lower() == 'y':
            kalkulator()
        elif choose.lower() == 't':
            print('Terima kasih')
        else:
            print('Maaf, input yang Anda masukkan salah')
            print('Silahkan masukkan Y atau T')
            tanya()

    # Menu utama
    print('Program Kalkulator Sederhana')
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Perkalian')
    print('4. Pembagian')
    print('Silahkan pilih 1-4')
    print('')

    pil = int(input('Masukkan pilihan : '))
    if pil == 1:
        tambah()
    elif pil == 2:
        kurang()
    elif pil == 3:
        kali()
    elif pil == 4:
        bagi()
    else:
        print('Maaf, input yang Anda masukkan salah')
        tanya()

# Menjalankan program
kalkulator()
