import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
data = pd.read_csv("df.csv")

# 2. Rename columns for easier access
data.rename(columns={
    '+Million Plus Cities': 'City',
    'Cause category': 'Cause',
    'Cause Subcategory': 'Subcause',
    'Outcome of Incident': 'Outcome',
    'Count': 'Count'
}, inplace=True)

# 3. Quick look
print("First 5 rows:")
print(data.head())
print("\nColumn names:")
print(data.columns)

# 4. Total accidents by city
city_totals = data[data['Outcome'] == 'Total number of Accidents']
city_counts = city_totals.groupby('City')['Count'].sum().sort_values(ascending=False)
print("\nAccidents by City:")
print(city_counts)

# 5. Total accidents by cause category
cause_totals = city_totals.groupby('Cause')['Count'].sum().sort_values(ascending=False)
print("\nAccidents by Cause Category:")
print(cause_totals)

# 6. Visualizations
plt.figure(figsize=(12,6))
sns.barplot(x=city_counts.index, y=city_counts.values)
plt.xticks(rotation=90)
plt.title("Total Accidents by City")
plt.savefig("total_accidents_by_city.png")
plt.show()

plt.figure(figsize=(8,6))
sns.barplot(x=cause_totals.index, y=cause_totals.values)
plt.xticks(rotation=45)
plt.title("Total Accidents by Cause Category")
plt.savefig("total_accidents_by_cause.png")
plt.show()

print("Script finished successfully!")
