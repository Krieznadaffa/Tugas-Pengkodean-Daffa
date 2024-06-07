import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Data
data_produksi = {
    'ID_Produk': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Jumlah_Produksi': [100, 150, 120, 200, 180, 130, 170, 190, 160, 140]
}

data_penjualan = {
    'ID_Produk': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Jumlah_Penjualan': [80, 120, 100, 150, 130, 90, 140, 160, 110, 100]
}

data_persediaan = {
    'ID_Produk': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Persediaan': [20, 30, 20, 50, 50, 40, 30, 30, 50, 40]
}

# Membuat DataFrame
df_produksi = pd.DataFrame(data_produksi)
df_penjualan = pd.DataFrame(data_penjualan)
df_persediaan = pd.DataFrame(data_persediaan)

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df_produksi['ID_Produk'], df_produksi['Jumlah_Produksi'], color='blue', label='Produksi')
plt.scatter(df_penjualan['ID_Produk'], df_penjualan['Jumlah_Penjualan'], color='red', label='Penjualan')
plt.xlabel('ID Produk')
plt.ylabel('Jumlah')
plt.title('Scatter Plot Produksi vs Penjualan')
plt.legend()
plt.grid(True)
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(df_produksi['Jumlah_Produksi'], bins=5, color='blue', alpha=0.5, label='Produksi')
plt.hist(df_penjualan['Jumlah_Penjualan'], bins=5, color='red', alpha=0.5, label='Penjualan')
plt.xlabel('Jumlah')
plt.ylabel('Frekuensi')
plt.title('Histogram Produksi vs Penjualan')
plt.legend()
plt.grid(True)
plt.show()

# Diagram Venn
venn2(subsets=(10, 10, 5), set_labels=('Produksi', 'Penjualan'))
plt.title('Diagram Venn Produksi vs Penjualan')
plt.show()

# Pie chart
total_persediaan = df_persediaan['Persediaan'].sum()
sizes = df_persediaan['Persediaan'] / total_persediaan
labels = df_persediaan['ID_Produk']
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Persentase Persediaan per Produk')
plt.axis('equal')
plt.show()

# Bar chart
plt.figure(figsize=(10, 6))
plt.bar(df_produksi['ID_Produk'], df_produksi['Jumlah_Produksi'], color='blue', label='Produksi')
plt.bar(df_penjualan['ID_Produk'], df_penjualan['Jumlah_Penjualan'], color='red', label='Penjualan')
plt.xlabel('ID Produk')
plt.ylabel('Jumlah')
plt.title('Bar Chart Produksi vs Penjualan')
plt.legend()
plt.grid(True)
plt.show()
