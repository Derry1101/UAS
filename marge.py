# Fungsi untuk menggabungkan dua bagian yang terurut
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i]['waktu_pemesanan'] < right[j]['waktu_pemesanan']:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Fungsi Merge Sort
def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    
    return merge(left, right)

# Data pesanan contoh
pesanan = [
    {'id_pesanan': 1, 'lokasi_pengambilan': 'A', 'lokasi_tujuan': 'B', 'waktu_pemesanan': '2025-01-05 10:30:00'},
    {'id_pesanan': 2, 'lokasi_pengambilan': 'C', 'lokasi_tujuan': 'D', 'waktu_pemesanan': '2025-01-05 08:00:00'},
    {'id_pesanan': 3, 'lokasi_pengambilan': 'B', 'lokasi_tujuan': 'A', 'waktu_pemesanan': '2025-01-05 09:15:00'},
    {'id_pesanan': 4, 'lokasi_pengambilan': 'D', 'lokasi_tujuan': 'C', 'waktu_pemesanan': '2025-01-05 07:45:00'},
]

# Mengurutkan data pesanan
pesanan_urut = merge_sort(pesanan)
print("Nama  : Derry Pratama Widiyanto\nNIM   : 241011401464\nKelas : 01TPLK009\n============================\n")
# Menampilkan hasil pengurutan
for pesanan in pesanan_urut:
    print(f"ID Pesanan: {pesanan['id_pesanan']}, Waktu Pemesanan: {pesanan['waktu_pemesanan']}")
