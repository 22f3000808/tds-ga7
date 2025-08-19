# 1. Load dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("q-excel-correlation-heatmap.xlsx")

# 2. Compute correlation
corr = df.corr()

# 3. Save correlation matrix as CSV
corr.to_csv("correlation.csv", index=True)

# 4. Plot heatmap (Excel-style Red-White-Green)
plt.figure(figsize=(6,6))
sns.heatmap(corr, annot=True, cmap="RdYlGn", center=0, square=True)
plt.title("Supply Chain Correlation Heatmap")
plt.savefig("heatmap.png", dpi=300, bbox_inches="tight")

# Show heatmap inline
plt.show()
