import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Longitude': [110.418, 106.826, 106.822, 108.642, 106.801],
    'Latitude': [-6.993, -6.192, -6.213, -6.596, -6.128],
    'Produksi': [120, 150, 180, 200, 220]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menghitung skewness dari setiap kolom numerik
skewness = df.skew()

# Membuat plot batang untuk skewness
plt.figure(figsize=(8, 6))
skewness.plot(kind='bar', color='skyblue')
plt.title('Skewness dari Hubungan Antara Variabel')
plt.xlabel('Variabel')
plt.ylabel('Skewness')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

