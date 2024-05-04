import csv
from collections import Counter

with open('hududlar.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    province_hospital_count = Counter()

    for row in reader:
        province = row['Hududlar']
        hospitals_built = sum(int(row[str(year)]) for year in range(2012, 2018) if row[str(year)].isdigit())
        province_hospital_count[province] += hospitals_built

# Natijalarni sortlash
sorted_provinces = sorted(province_hospital_count.items(), key=lambda x: x[1], reverse=True)

print("2012-2017 yillarda eng ko'p kasalxonalar qurilgan viloyatlar:")
for province, count in sorted_provinces[:3]:
    print(f"{province}: {count} ta kasalxona")
