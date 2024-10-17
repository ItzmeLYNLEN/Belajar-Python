nama_pembeli = input("Masukkan Nama Pembeli: ")
kode_mainan = input("Masukkan Kode Mainan: ")
harga = int(input("Masukkan Harga: "))
jumlah = int(input("Masukkan Jumlah Beli: "))

total = harga * jumlah

print("\n*")
print("TOKO MAINAN ANAK")
print("*")
print(f"Nama Pembeli : {nama_pembeli}")
print(f"Kode Mainan  : {kode_mainan}")
print(f"Harga        : {harga}")
print(f"Jumlah Beli  : {jumlah}")
print(f"Total        : {total}")