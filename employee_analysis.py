# Email for verification
# 22f3000808@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Step 1: Load dataset
# -----------------------------
# If you have a CSV file, uncomment:
# df = pd.read_csv("employee_data.csv")

# Simulating employee dataset (100 rows)
import random

departments = ["Marketing", "Sales", "HR", "Finance", "IT", "Operations"]
regions = ["North", "South", "East", "West"]

data = {
    "EmployeeID": range(1, 101),
    "Department": [random.choice(departments) for _ in range(100)],
    "Region": [random.choice(regions) for _ in range(100)],
    "PerformanceScore": [random.randint(1, 5) for _ in range(100)]
}

df = pd.DataFrame(data)

# -----------------------------
# Step 2: Frequency count for Marketing
# -----------------------------
marketing_count = (df["Department"] == "Marketing").sum()
print(f"Number of employees in Marketing: {marketing_count}")

# -----------------------------
# Step 3: Histogram of departments
# -----------------------------
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="Department", palette="Set2")
plt.title("Distribution of Employees by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()

# Save visualization as HTML (using mpld3)
import mpld3
html_str = mpld3.fig_to_html(plt.gcf())

with open("employee_analysis.html", "w") as f:
    f.write(html_str)

print("employee_analysis.html generated successfully.")
