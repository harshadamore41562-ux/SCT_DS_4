import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- User interaction ---
dataset_path = input("Enter dataset path (e.g., trafic_accident.csv): ").strip()
analysis_choice = input("Choose analysis (city/cause/both): ").strip().lower()
save_plots = input("Do you want to save plots as PNG? (yes/no): ").strip().lower()

# 1. Load dataset
data = pd.read_csv(dataset_path)

# Clean column names (remove hidden spaces)
data.columns = data.columns.str.strip()

# 2. Rename columns correctly
data.rename(columns={
    'Million Plus Cities': 'Cities',   # <-- important fix
    'Cause category': 'Cause',
    'Cause Subcategory': 'Subcause',
    'Outcome of Incident': 'Outcome',
    'Count': 'Count'
}, inplace=True)

print("\nColumns after renaming:", data.columns.tolist())

# 3. Filter totals
city_totals = data[data['Outcome'] == 'Total number of Accidents']

# --- Analysis by City ---
if analysis_choice in ["city", "both"]:
    if 'Cities' in city_totals.columns:
        city_counts = city_totals.groupby('Cities')['Count'].sum().sort_values(ascending=False)
        print("\nAccidents by City:")
        print(city_counts)

        plt.figure(figsize=(12,6))
        sns.barplot(x=city_counts.index, y=city_counts.values)
        plt.xticks(rotation=90)
        plt.title("Total Accidents by City")
        if save_plots == "yes":
            plt.savefig("total_accidents_by_city.png")
        plt.show()
    else:
        print("Column 'Cities' not found. Check dataset headers.")

# --- Analysis by Cause ---
if analysis_choice in ["cause", "both"]:
    if 'Cause' in city_totals.columns:
        cause_totals = city_totals.groupby('Cause')['Count'].sum().sort_values(ascending=False)
        print("\nAccidents by Cause Category:")
        print(cause_totals)

        plt.figure(figsize=(8,6))
        sns.barplot(x=cause_totals.index, y=cause_totals.values)
        plt.xticks(rotation=45)
        plt.title("Total Accidents by Cause Category")
        if save_plots == "yes":
            plt.savefig("total_accidents_by_cause.png")
        plt.show()
    else:
        print("Column 'Cause' not found. Check dataset headers.")

print("\nScript finished successfully!")
