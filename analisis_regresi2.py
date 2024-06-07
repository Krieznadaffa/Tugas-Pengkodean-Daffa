import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from pandas.tseries.offsets import DateOffset

# Data
data_produksi = {
    'Tanggal': pd.date_range(start='2023-01-01', periods=6, freq='MS'),
    'Produksi': [120, 150, 180, 200, 220, 240]
}

data_penjualan = {
    'Tanggal': pd.date_range(start='2023-01-01', periods=6, freq='MS'),
    'Penjualan': [100, 130, 160, 180, 200, 210]
}

# Membuat DataFrame
df_produksi = pd.DataFrame(data_produksi)
df_penjualan = pd.DataFrame(data_penjualan)

# Menambahkan 5 bulan ke belakang dan 5 bulan ke depan
tanggal_belakang = pd.date_range(start=df_produksi['Tanggal'].min() - DateOffset(months=5), periods=5, freq='MS')
tanggal_depan = pd.date_range(start=df_produksi['Tanggal'].max() + DateOffset(months=1), periods=5, freq='MS')

df_belakang = pd.DataFrame({'Tanggal': tanggal_belakang})
df_depan = pd.DataFrame({'Tanggal': tanggal_depan})

df_produksi = pd.concat([df_belakang, df_produksi, df_depan], ignore_index=True)
df_penjualan = pd.concat([df_belakang, df_penjualan, df_depan], ignore_index=True)

# Menggabungkan data produksi dan penjualan berdasarkan tanggal
df = pd.merge(df_produksi, df_penjualan, on='Tanggal', how='outer')  # Outer join untuk mempertahankan semua tanggal

# Mengisi nilai NaN dengan nilai rata-rata
df.fillna(df.mean(), inplace=True)

# Memisahkan fitur (X) dan target (y)
X = df['Tanggal'].astype(np.int64).values.reshape(-1, 1)  # Mengubah tanggal menjadi nilai numerik
y = df['Produksi']  # Analisis regresi untuk produksi

# Membangun model regresi linier
model = LinearRegression()
model.fit(X, y)

# Membuat prediksi untuk 5 bulan ke belakang dan 5 bulan ke depan
tanggal_prediksi = pd.date_range(start=df['Tanggal'].min() - DateOffset(months=5), periods=16, freq='MS')
X_pred = tanggal_prediksi.astype(np.int64).values.reshape(-1, 1)  # Mengubah tanggal prediksi menjadi nilai numerik
y_pred = model.predict(X_pred)

# Plot hasil regresi
plt.scatter(df['Tanggal'], df['Produksi'], color='blue', label='Data Produksi')
plt.plot(tanggal_prediksi, y_pred, color='red', linewidth=2, label='Regresi Linier Produksi')
plt.xlabel('Tanggal')
plt.ylabel('Produksi')
plt.title('Regresi Linier Produksi 5 Bulan')
plt.legend()
plt.grid(True)
plt.show()

# Koefisien regresi
print("Koefisien regresi untuk produksi:", model.coef_[0])
print("Intersep:", model.intercept_)
