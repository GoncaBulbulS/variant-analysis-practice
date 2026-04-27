import pandas as pd

# Load the data
df = pd.read_csv("sample_variants.csv")

# Apply filters
filtered = df[(df["quality"] >= 30) & (df["frequency"] <= 0.01)]

# Save filtered results
filtered.to_csv("filtered_variants.csv", index=False)

print("Filtered variants:")
print(filtered)
