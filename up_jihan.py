# Aplikasi Pemesanan Tiket Bioskop

print("=== SELAMAT DATANG DI CINEMA ===")
print("Daftar Harga Tiket:")
print("1. Reguler : Rp35.000")
print("2. VIP     : Rp50.000")
print("3. Premium : Rp75.000")
print("Diskon 10% jika membeli lebih dari 3 tiket")
print("=" * 32)

lanjut = "y"

# Proses berulang untuk melayani beberapa pelanggan

while lanjut.lower() == "y":

    # 1. Input nama pelanggan
    nama = input("\nMasukkan nama pelanggan: ")

    # 2. Input jenis dan jumlah tiket
    print("\nPilih jenis tiket:")
    print("1. Reguler")
    print("2. VIP")
    print("3. Premium")
    pilihan = int(input("Masukkan pilihan (1/2/3): "))
    jumlah = int(input("Masukkan jumlah tiket: "))

    # 3. Tentukan harga berdasarkan jenis tiket (percabangan)
    if pilihan == 1:
        jenis = "Reguler"
        harga = 35000
    elif pilihan == 2:
        jenis = "VIP"
        harga = 50000
    elif pilihan == 3:
        jenis = "Premium"
        harga = 75000
    else:
        print("Pilihan tidak valid! Silakan ulangi.")
        continue

    total = harga * jumlah

    # 4. Cek diskon jika membeli lebih dari 3 tiket
    if jumlah > 3:
        diskon = total * 0.10
        total_bayar = total - diskon
    else:
        diskon = 0
        total_bayar = total

    # Tampilkan hasil pemesanan

    print("\===== STRUK PEMESANAN =====")
    print("Nama Pelanggan :", nama)
    print("Jenis Tiket    :", jenis)
    print("Jumlah Tiket   :", jumlah)
    print("Harga Satuan   : Rp{:,.0f}".format(harga).replace(",", "."))
    print("Diskon         : Rp{:,.0f}".format(diskon).replace(",", "."))
    print("Total Bayar    : Rp{:,.0f}".format(total_bayar).replace(",", "."))
    print("===========================")

    # 5. Proses berulang
    lanjut = input("\nLayani pelanggan lain? (y/n): ")

print("\nTerima kasih! Program selesai.")