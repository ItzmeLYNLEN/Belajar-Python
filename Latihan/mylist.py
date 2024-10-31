
my_list = ['p', 'y', 't', 'h', 'o', 'n', 'i', 'n', 'd','o']

# anggota list dari 3 - 5
print(my_list[ 3:6 ])

# anggota list dari 4 - end 
print(my_list[ 4: ])

# anggota list dari 0 - 4
print(my_list[ :5])

# indeks dari belakang dari -1 - -4
print(my_list[ -1:-5])

# Output 'y'
print(my_list.pop(1))

del my_list[2]
print(my_list)

my_list.clear()

# Ouput []
print(my_list)


# MENGUBAH LIST

# misal ada nilai yang salah
ganjil = [1,3,4,7,9]

# ubah item ke 3 (indeks ke 2)
ganjil[2] = 5
print(ganjil)

# mengubah sekali banyak
ganjil[2:5] = [11,13,15]
print(ganjil)


ganjil = [1,3,5,7]
ganjil.append(9)
print(ganjil)
ganjil.extend([11,13,15])
print(ganjil)