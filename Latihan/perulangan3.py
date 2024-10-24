ulang = int(input("Masukan Banyaknya Data : "))


for i in range(ulang):
    print("data Ke - " +str(i+1))
    nim = input("Masukan NIM anda : ")
    nama = input("Masukan Nama anda : ")
    uts = int(input("Masukan Nilai UTS anda : "))
    uas = int(input("Masukan Nilai UAS anda : "))
    print("NIM anda adalah %s Nama anda adalah %s nilai UTS anda adalah %i nilai UAS anda adalah %i" % (nim,nama,uts,uas))
    print("-----------------------------------------------------------------------------------------\n")