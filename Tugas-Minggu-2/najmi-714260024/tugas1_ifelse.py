# =============================================
# Tugas Mandiri Modul 1 - Program Percabangan
# Nama  : (najmi afifah j. siregar)
# NIM   : (714260024)
# Kelas : (1B)
# =============================================

print("="*45)
print("   PROGRAM KONVERSI NILAI KE HURUF MUTU")
print("="*45)

# 1. Input wajib dari user, tidak hardcode
try:
    nilai = float(input("Masukkan nilai akhir (0-100): "))
except ValueError:
    print("---------------------------------------------")
    print("Error: Input harus berupa angka!")
    print("Terima kasih telah menggunakan program ini.")
    exit()

print("---------------------------------------------")

# 2. Pemeriksaan di luar rentang 0-100
if nilai < 0 or nilai > 100:
    print(f"Nilai {nilai} tidak valid!")
    print("Nilai harus berada di rentang 0 - 100.")
else:
    # 3. Minimal 4 elif (ini gue pakai 4 elif = total 5 kondisi + else)
    if nilai >= 80:
        huruf = "A"
        keterangan = "Lulus - Sangat Baik"
    elif nilai >= 70:
        huruf = "B"
        keterangan = "Lulus - Baik"
    elif nilai >= 60:
        huruf = "C"
        keterangan = "Lulus - Cukup"
    elif nilai >= 50:
        huruf = "D"
        keterangan = "Tidak Lulus - Kurang"
    else: # di bawah 50
        huruf = "E"
        keterangan = "Tidak Lulus - Sangat Kurang"

    # 4. Wajib pakai f-string dan tampilan rapi
    print(f"Nilai Angka : {nilai}")
    print(f"Huruf Mutu  : {huruf}")
    print(f"Keterangan  : {keterangan}")

print("="*45)
print("Terima kasih telah menggunakan program ini.")
print("="*45)