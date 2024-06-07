import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Data
data_produksi = {
    'ID_Produk': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Jumlah_Produksi': [100, 150, 120, 200, 180, 130, 170, 190, 160, 140]
}

data_penjualan = {
    'ID_Produk': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Jumlah_Penjualan': [80, 120, 100, 150, 130, 90, 140, 160, 110, 100]
}

# Membuat DataFrame
df_produksi = pd.DataFrame(data_produksi)
df_penjualan = pd.DataFrame(data_penjualan)

# Menggabungkan data produksi dan penjualan berdasarkan ID_Produk
df = pd.merge(df_produksi, df_penjualan, on='ID_Produk')

# Memisahkan fitur (X) dan target (y)
X = df[['Jumlah_Produksi']]
y = df['Jumlah_Penjualan']

# Membangun model regresi linier
model = LinearRegression()
model.fit(X, y)

# Membuat prediksi
y_pred = model.predict(X)

# Plot hasil regresi
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X, y_pred, color='red', linewidth=2, label='Regresi Linier')
plt.xlabel('Produksi')
plt.ylabel('Penjualan')
plt.title('Regresi Linier antara Produksi dan Penjualan')
plt.legend()
plt.grid(True)
plt.show()

# Koefisien regresi
print("Koefisien regresi:", model.coef_[0])
print("Intersep:", model.intercept_)
