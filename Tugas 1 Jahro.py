print("Selamat datang di Aplikasi perhitungan nilai Mahasiswa")

# Get user inputs for nilai tugas, UTS, and UAS
nilai_tugas = float(input("Silahkan Masukan nilai Tugas Anda: "))
nilai_uts = float(input("Silahkan Masukan nilai UTS Anda: "))
nilai_uas = float(input("Silahkan Masukan nilai UAS Anda: "))

# Calculate the final grade with weighted scores
nilai_akhir = (0.25 * nilai_tugas) + (0.35 * nilai_uts) + (0.40 * nilai_uas)

# Display the final grade and corresponding grade letter
print("Nilai Akhir Anda: ", nilai_akhir)

if nilai_akhir > 85:
    print("Dalam Huruf: A")
elif nilai_akhir > 80:
    print("Dalam Huruf: A-")
elif nilai_akhir > 75:
    print("Dalam Huruf: B+")
elif nilai_akhir > 70:
    print("Dalam Huruf: B")
elif nilai_akhir > 65:
    print("Dalam Huruf: B-")
elif nilai_akhir > 60:
    print("Dalam Huruf: C+")
elif nilai_akhir > 55:
    print("Dalam Huruf: C")
elif nilai_akhir > 50:
    print("Dalam Huruf: C-")
elif nilai_akhir > 30:
    print("Dalam Huruf: D")
else:
    print("Dalam Huruf: E")