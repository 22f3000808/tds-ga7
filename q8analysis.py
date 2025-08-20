import matplotlib.pyplot as plt
import pandas as pd

# Email for verification
email = "22f3000808@ds.study.iitm.ac.in"

# Quarterly data
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "InventoryTurnover": [0.53, 5.37, 9.98, 7.31]
}
industry_target = 8

# Create DataFrame
df = pd.DataFrame(data)
df["Target"] = industry_target

# Compute average
average_turnover = df["InventoryTurnover"].mean()
print(f"Average Inventory Turnover Ratio: {average_turnover:.2f}")

# Visualization
plt.figure(figsize=(8, 5))
plt.plot(df["Quarter"], df["InventoryTurnover"], marker="o", label="Company")
plt.axhline(industry_target, color="red", linestyle="--", label=f"Industry Target ({industry_target})")
plt.title("Quarterly Inventory Turnover Ratio vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("Inventory Turnover Ratio")
plt.legend()
plt.tight_layout()
plt.savefig("inventory_turnover.png")
plt.close()
