
import pandas as pd

# Load data
data = pd.read_csv("students.csv")

# Hitung rata-rata
data["Average"] = data[["Math", "English", "Science"]].mean(axis=1)

# Function grading
def get_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

# Apply grade
data["Grade"] = data["Average"].apply(get_grade)

# Sorting ranking
data = data.sort_values(by="Average", ascending=False)

# Print hasil
print(data)
# Save ke file baru
data.to_csv("result.csv", index=False)

print("\nData berhasil disimpan ke result.csv")
# Distribusi grade
grade_counts = data["Grade"].value_counts()
print("\nGrade Distribution:")
print(grade_counts)

# Rata-rata keseluruhan
overall_avg = data["Average"].mean()
print("\nOverall Average Score:", round(overall_avg, 2))

# Top 5 siswa
top5 = data.head(5)
print("\nTop 5 Students:")
print(top5[["Name", "Average"]])
print("Student Score Analyzer Started")

import matplotlib.pyplot as plt

# --- BAGIAN VISUALISASI ---
# Kita bikin grafik batang untuk distribusi Grade
grade_counts.plot(kind='bar', color=['green', 'blue', 'orange', 'red'])

plt.title('Distribusi Grade Siswa')
plt.xlabel('Grade')
plt.ylabel('Jumlah Siswa')

# Simpan grafiknya jadi gambar biar bisa dipajang di GitHub
plt.savefig('grade_distribution.png')
print("Grafik berhasil dibuat: grade_distribution.png")