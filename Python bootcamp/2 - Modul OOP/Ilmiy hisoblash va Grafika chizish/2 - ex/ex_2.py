import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

total_passengers = df.shape[0]
men = df[df["Sex"] == "male"].shape[0]
women = df[df["Sex"] == "female"].shape[0]

print(f"Umimiy Yo'lovchilar: {total_passengers}")
print(f"Erkaklar soni: {men}")
print(f"Ayollar soni: {women}")

plt.figure(figsize=(6, 6))
plt.pie([men, women], labels=["Men", "Women"], autopct="%1.1f%%")
plt.title("Titanikda gender taqsimoti")
plt.show()

total_fare = df["Fare"].sum()
average_fare = df["Fare"].mean()

print(f"Umumiy chipta narxi: {total_fare:.2f}")
print(f"O'rtacha chipta narxi: {average_fare:.2f}")

filtered_df = df[(df["Age"] >= 15) & (df["Age"] <= 40)]
percentage = (len(filtered_df) / total_passengers) * 100

print(f"Yo'lovchilar ulushi (15-40 yosh): {percentage:.2f}%")

surviving_children = df[(df["Age"] < 16) & (df["Survived"] == 1)]
total_children = df[df["Age"] < 16].shape[0]
percentage = (len(surviving_children) / total_children) * 100

print(f"Tirik qolgan bolalar ulushi (16 yoshgacha): {percentage:.2f}%")
