# Mengimport modul tkinter untuk membuat GUI dan messagebox untuk menampilkan pesan error
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try:
        # Loop untuk mengecek setiap entry input nilai
        for entry in entries:
            # Mengambil nilai dari input dan mengonversinya menjadi integer
            nilai = int(entry.get())
            # Memastikan nilai berada di antara 0 dan 100
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")

        # Menampilkan hasil prediksi jika semua input valid
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
        # Menampilkan pesan error jika ada input yang tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Inisialisasi Tkinter
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Judul aplikasi
root.geometry("500x600")  # Ukuran jendela aplikasi
root.configure(bg="#add8e6")  # Latar belakang jendela dengan warna biru muda

# Membuat label judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#add8e6", fg="#000080")
judul_label.pack(pady=20)  # Menambahkan jarak vertikal di sekitar judul

# Frame untuk menampung input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#add8e6")  # Warna latar belakang frame biru muda
frame_input.pack(pady=10)

# Membuat list untuk menyimpan entry nilai
entries = []
for i in range(10):
    # Membuat label untuk setiap mata pelajaran
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}:", font=("Arial", 12), bg="#add8e6", fg="#000080")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  # Menempatkan label di grid, rata kanan

    # Membuat entry (input) untuk memasukkan nilai
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)  # Menempatkan entry di grid, di samping label
    entries.append(entry)  # Menyimpan entry ke dalam list entries

# Membuat tombol untuk menampilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), fg="white", bg="#000080")
prediksi_button.pack(pady=30)  # Menambahkan jarak vertikal di sekitar tombol

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic"), fg="#000080", bg="#add8e6")
hasil_label.pack(pady=20)  # Menambahkan jarak vertikal di sekitar label hasil

# Menjalankan aplikasi
root.mainloop()
