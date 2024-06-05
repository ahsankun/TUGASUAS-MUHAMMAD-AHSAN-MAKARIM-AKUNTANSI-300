import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Load data
df = pd.read_csv("generated_data.csv")

# Menampilkan distribusi umur (Histogram)
plt.figure(figsize=(8, 6))
sns.histplot(df['umur'], bins=20, kde=True, color='skyblue')
plt.title('Distribusi Umur')
plt.xlabel('Umur')
plt.ylabel('Frekuensi')
plt.show()

# Barplot
plt.figure(figsize=(8, 6))
sns.countplot(x='pendidikan', data=df, palette='muted')
plt.title('Distribusi Pendidikan')
plt.xlabel('Pendidikan')
plt.ylabel('Frekuensi')
plt.show()

# Kluster menggunakan KMeans
# Menggunakan hanya umur dan gaji untuk klasterisasi
X = df[['umur', 'gaji']]

# Menentukan jumlah kluster
num_clusters = 3

# Membuat model KMeans
kmeans = KMeans(n_clusters=num_clusters, random_state=42)

# Melakukan klasterisasi
kmeans.fit(X)

# Mendapatkan label kluster untuk setiap data point
df['cluster'] = kmeans.labels_

# Plot kluster
plt.figure(figsize=(8, 6))
sns.scatterplot(x='umur', y='gaji', hue='cluster', data=df, palette='Set1', legend='full')
plt.title('Plot Kluster dengan KMeans')
plt.xlabel('Umur')
plt.ylabel('Gaji')
plt.show()

# Scatterplot untuk hubungan antara umur dan gaji
plt.figure(figsize=(8, 6))
sns.scatterplot(x='umur', y='gaji', data=df, color='orange')
plt.title('Scatterplot Umur vs Gaji')
plt.xlabel('Umur')
plt.ylabel('Gaji')
plt.show()

# Boxplot untuk distribusi gaji dalam setiap kluster
plt.figure(figsize=(8, 6))
sns.boxplot(x='cluster', y='gaji', data=df, palette='Set2')
plt.title('Distribusi Gaji dalam Setiap Kluster')
plt.xlabel('Kluster')
plt.ylabel('Gaji')
plt.show()
