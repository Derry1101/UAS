print("Nama  : Derry Pratama Widiyanto\nNIM   : 241011401464\nKelas : 01TPLK009\n============================\n")

Dataset_a = [1,2,3,4,5,6,7,8,9]
Dataset_b = [1, 19, 3, 15, 7, 5, 11, 13, 9, 17]



def linear_search(data, target):
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1  

# Mencari angka 7
result_angka = linear_search(Dataset_a, 7)
# Mencari alfabet 'f'
result_alfabet = linear_search(Dataset_b, 9)

print(f"Angka 7 ditemukan pada indeks: {result_angka}")
print(f"Alfabet 'f' ditemukan pada indeks: {result_alfabet}")




