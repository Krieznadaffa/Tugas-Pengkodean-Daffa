**ANALISIS STATISTIK**

**TABEL PRODUKSI**
| ID_Produk | Tanggal     | Jumlah_Produksi |
|-----------|-------------|-----------------|
| 1         | 2024-06-01  | 100             |
| 2         | 2024-06-02  | 150             |
| 3         | 2024-06-03  | 120             |
| 4         | 2024-06-04  | 200             |
| 5         | 2024-06-05  | 180             |
| 6         | 2024-06-06  | 130             |
| 7         | 2024-06-07  | 170             |
| 8         | 2024-06-08  | 190             |
| 9         | 2024-06-09  | 160             |
| 10        | 2024-06-10  | 140             |

**TABEL PENJUALAN**
| ID_Produk | Tanggal     | Jumlah_Penjualan |
|-----------|-------------|------------------|
| 1         | 2024-06-01  | 80               |
| 2         | 2024-06-02  | 120              |
| 3         | 2024-06-03  | 100              |
| 4         | 2024-06-04  | 150              |
| 5         | 2024-06-05  | 130              |
| 6         | 2024-06-06  | 90               |
| 7         | 2024-06-07  | 140              |
| 8         | 2024-06-08  | 160              |
| 9         | 2024-06-09  | 110              |
| 10        | 2024-06-10  | 100              |

**TABEL PERSEDIAAN**
| ID_Produk | Tanggal     | Persediaan |
|-----------|-------------|------------|
| 1         | 2024-06-01  | 20         |
| 2         | 2024-06-02  | 30         |
| 3         | 2024-06-03  | 20         |
| 4         | 2024-06-04  | 50         |
| 5         | 2024-06-05  | 50         |
| 6         | 2024-06-06  | 40         |
| 7         | 2024-06-07  | 30         |
| 8         | 2024-06-08  | 30         |
| 9         | 2024-06-09  | 50         |
| 10        | 2024-06-10  | 40         |

**LANGKAH-LANGKAH:**
1. Memahami Data: Pertama, pahami struktur data dan atribut-atributnya. Pastikan Anda mengerti apa yang setiap kolom dalam data tersebut representasikan.
2. Pemeriksaan Data: Periksa apakah ada nilai yang hilang (missing values) dalam data. Jika ada, pertimbangkan bagaimana Anda akan menangani nilai-nilai yang hilang tersebut, apakah dengan mengisi nilai rata-rata, interpolasi, atau metode lainnya.
3. Statistik Deskriptif: Hitung statistik deskriptif seperti rata-rata, median, kuartil, standar deviasi, dll., untuk setiap variabel (penjualan, produksi, persediaan). Ini akan memberi Anda gambaran umum tentang distribusi data.
4. Visualisasi Data: Buat visualisasi data seperti histogram, diagram batang, dan scatter plot untuk memahami distribusi dan hubungan antar variabel. Anda dapat menggunakan visualisasi ini untuk menemukan pola atau tren dalam data.
5. Korelasi: Hitung koefisien korelasi antara variabel-variabel untuk melihat apakah ada hubungan linier antara penjualan, produksi, dan persediaan. Ini dapat dilakukan dengan menggunakan metode korelasi Pearson atau metode korelasi lainnya.
6. Analisis Regresi: Jika Anda ingin memodelkan hubungan antara variabel-variabel, Anda dapat melakukan analisis regresi. Misalnya, Anda dapat melakukan analisis regresi linier untuk memprediksi penjualan berdasarkan produksi dan persediaan.
7. Interpretasi Hasil: Terakhir, interpretasikan hasil analisis Anda. Apa insight yang dapat Anda ambil dari data tersebut? Apakah ada hubungan antara variabel-variabel? Bagaimana Anda dapat menggunakan informasi ini untuk pengambilan keputusan lebih lanjut?
8. Validasi dan Kesimpulan: Terakhir, pastikan untuk memvalidasi hasil analisis Anda dan membuat kesimpulan yang kuat berdasarkan temuan Anda. Juga, pastikan untuk mempertimbangkan keterbatasan dari analisis Anda dan langkah-langkah selanjutnya yang perlu diambil.

**GRAFIK VISUALISASI DATA**

![sCATTER pLOT](https://github.com/Krieznadaffa/Tugas-Pengkodean-Daffa/assets/167004660/d03ab901-6551-44fe-ad44-d05f6c64c9b3)
![Pie Chart](https://github.com/Krieznadaffa/Tugas-Pengkodean-Daffa/assets/167004660/19a0b707-bc85-4d6d-ae48-b73fad9eb97a)
![Histogram](https://github.com/Krieznadaffa/Tugas-Pengkodean-Daffa/assets/167004660/7854ab38-2a79-48f8-9878-3b7e80e8ef4f)
![Diagram Venn](https://github.com/Krieznadaffa/Tugas-Pengkodean-Daffa/assets/167004660/915a35ec-6207-4e66-a648-20f628946c1a)
![Bar Chart](https://github.com/Krieznadaffa/Tugas-Pengkodean-Daffa/assets/167004660/f6b6a710-c136-4446-a7ac-c40037b56e13)

**ANALISIS REGRESI 1**

Hasil Analsis
1. Plot Regresi Linier:
   - Grafik menunjukkan hubungan linier antara jumlah produksi dan jumlah penjualan. Garis merah menunjukkan garis regresi linier yang telah diperkirakan oleh model regresi.
   - Sebagian besar titik data terletak di sekitar garis regresi, menunjukkan bahwa model regresi linier cukup sesuai dengan data.
     Koefisien Regresi:

2. Koefisien regresi (slope) menunjukkan seberapa banyak penjualan yang diharapkan meningkat untuk setiap peningkatan dalam jumlah produksi. Nilai koefisien regresi yang positif menunjukkan hubungan positif antara produksi dan penjualan.
   - Intersep menunjukkan nilai penjualan yang diharapkan ketika jumlah produksi adalah nol. Dalam konteks ini, intersep mungkin memiliki makna bisnis jika ada biaya tetap yang terkait dengan produksi.
  
Hasil Interpretasi
- Dari plot regresi linier, kita dapat melihat bahwa semakin banyak produk yang diproduksi, semakin banyak pula yang dijual. Ini menunjukkan hubungan positif antara jumlah produksi dan penjualan.
- Koefisien regresi positif menunjukkan bahwa setiap peningkatan satu unit dalam jumlah produksi diperkirakan akan meningkatkan penjualan sebesar nilai koefisien tersebut.
- Meskipun model regresi linier memberikan perkiraan hubungan antara produksi dan penjualan, perlu diingat bahwa hubungan antara kedua variabel mungkin lebih kompleks dan dipengaruhi oleh faktor-faktor lain yang tidak ditangkap oleh model ini.

![analisis regresi 1](https://github.com/Krieznadaffa/Tugas-Pengkodean-Daffa/assets/167004660/e2499de4-7dc8-4165-bb0c-9abe717455e4)

**ANALISIS REGRESI 2**
Regresi 5 bulan sebelum dan sesudah
Hasil Analisis:
1. Plot Regresi Linier Produksi:
Grafik menunjukkan hubungan linier antara tanggal produksi dan jumlah produksi. Garis merah menunjukkan garis regresi linier yang telah diperkirakan oleh model regresi.
Terdapat kenaikan yang sebagian besar linier dalam jumlah produksi dari bulan ke bulan, sesuai dengan tren yang ditunjukkan oleh model regresi.

2. Koefisien Regresi:
Koefisien regresi menunjukkan seberapa banyak jumlah produksi diharapkan berubah untuk setiap perubahan satu unit dalam nilai tanggal. Nilai koefisien regresi yang positif menunjukkan hubungan positif antara tanggal produksi dan jumlah produksi.
Intersep menunjukkan jumlah produksi yang diharapkan pada tanggal awal (5 bulan sebelum data yang ada).

Interpretasi:
- Dari plot regresi linier produksi, kita dapat melihat tren kenaikan yang linier dalam jumlah produksi dari bulan ke bulan.
- Koefisien regresi positif menunjukkan bahwa dengan bertambahnya tanggal produksi, jumlah produksi cenderung meningkat. Ini mungkin disebabkan oleh peningkatan permintaan atau efisiensi proses produksi seiring berjalannya waktu.
- Model regresi linier memberikan perkiraan jumlah produksi berdasarkan tanggal produksi. Namun, perlu diingat bahwa faktor-faktor lain seperti musim atau perubahan tren pasar mungkin juga memengaruhi jumlah produksi dan perlu dipertimbangkan dalam pengambilan keputusan.

![Analisis Regresi 2](https://github.com/Krieznadaffa/Tugas-Pengkodean-Daffa/assets/167004660/6dc5b358-c39b-41d3-9221-9c0189733677)

**ANALISIS SKEWNESS**

Hasil Analisis:
1. Skewness dari Variabel Produksi:
Skewness adalah suatu ukuran statistik yang menggambarkan kemiringan distribusi data. Nilai skewness yang positif menunjukkan bahwa ekor distribusi lebih panjang ke kanan dari nilai rata-rata, sementara nilai skewness yang negatif menunjukkan bahwa ekor distribusi lebih panjang ke kiri dari nilai rata-rata. Nilai skewness mendekati nol menunjukkan bahwa distribusi relatif simetris.
Dari plot batang, kita dapat melihat bahwa skewness untuk variabel produksi adalah positif, yang menunjukkan bahwa distribusi data produksi cenderung condong ke kanan. Ini menunjukkan bahwa sebagian besar nilai produksi berada di bawah rata-rata, dengan sedikit nilai yang tinggi.

2. Skewness dari Variabel Longitude dan Latitude:
Skewness untuk variabel longitude dan latitude juga positif, yang menunjukkan bahwa distribusi data koordinat geografis juga cenderung condong ke kanan. Ini mungkin menunjukkan bahwa sebagian besar nilai koordinat berada di bawah rata-rata, dengan sedikit nilai yang tinggi.

Interpretasi:
- Skewness dapat memberikan wawasan tentang bentuk distribusi data. Nilai skewness yang positif menunjukkan bahwa sebagian besar data cenderung berada di bagian bawah dari rentang nilai, sementara beberapa nilai ekstrim berada di atas rata-rata.
- Dalam konteks ini, skewness yang positif untuk variabel produksi, longitude, dan latitude menunjukkan bahwa sebagian besar observasi memiliki nilai di bawah rata-rata, dengan sedikit observasi yang memiliki nilai yang jauh di atas rata-rata.
- Ini dapat menjadi informasi yang berguna dalam pemodelan statistik atau dalam pengambilan keputusan bisnis, terutama jika ada kebutuhan untuk memahami distribusi data secara lebih rinci.

![Analisis Skewness](https://github.com/Krieznadaffa/Tugas-Pengkodean-Daffa/assets/167004660/73521d89-28bf-4fbd-8906-c2d2e284dbcc)

**ANALISIS HEATMAP**

Hasil Analisis:
1. Korelasi Antara Variabel Produksi, Longitude, dan Latitude:
Korelasi adalah ukuran statistik yang menunjukkan seberapa erat hubungan antara dua variabel. Nilai korelasi berkisar antara -1 hingga 1. Korelasi positif menunjukkan hubungan yang positif di mana kedua variabel bergerak ke arah yang sama, sedangkan korelasi negatif menunjukkan hubungan yang negatif di mana kedua variabel bergerak ke arah yang berlawanan.
Dari heatmap korelasi, kita dapat melihat bahwa variabel produksi memiliki korelasi yang tinggi dengan variabel lainnya. Ini menunjukkan bahwa produksi cenderung berkorelasi positif dengan longitude dan latitude.

Interpretasi:
- Korelasi yang tinggi antara produksi dengan longitude dan latitude menunjukkan bahwa terdapat hubungan yang kuat antara lokasi geografis (longitude dan latitude) dengan jumlah produksi. Hal ini mungkin disebabkan oleh adanya faktor-faktor lingkungan atau geografis tertentu yang mempengaruhi proses produksi atau distribusi produk.
- Korelasi ini dapat menjadi indikasi penting dalam pengambilan keputusan, misalnya dalam perencanaan lokasi pabrik atau gudang, atau dalam analisis faktor-faktor yang memengaruhi efisiensi produksi. Namun, penting untuk diingat bahwa korelasi tidak menyiratkan kausalitas, dan faktor-faktor lain yang tidak ditangkap dalam analisis ini juga dapat memengaruhi produksi.

![Analisis Heat Map](https://github.com/Krieznadaffa/Tugas-Pengkodean-Daffa/assets/167004660/246761f9-a08d-4a57-83d7-65cd1f584a5d)
