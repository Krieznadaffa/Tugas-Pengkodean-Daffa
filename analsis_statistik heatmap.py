import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Longitude': [110.418, 106.826, 106.822, 108.642, 106.801],
    'Latitude': [-6.993, -6.192, -6.213, -6.596, -6.128],
    'Produksi': [120, 150, 180, 200, 220]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menghitung korelasi antara variabel
correlation_matrix = df.corr()

# Membuat heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='RdBu_r', vmin=-1, vmax=1)
plt.title('Heatmap Korelasi Variabel')
plt.show()
