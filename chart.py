# chart.py
# Author: 22f3000808@ds.study.iitm.ac.in

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# Generate realistic synthetic data
# -----------------------------
np.random.seed(42)

n_customers = 100

data = pd.DataFrame({
    "Purchase_Frequency": np.random.poisson(lam=5, size=n_customers),
    "Average_Spend": np.random.normal(loc=200, scale=50, size=n_customers),
    "Website_Visits": np.random.poisson(lam=20, size=n_customers),
    "App_Usage_Time": np.random.normal(loc=15, scale=5, size=n_customers),  # minutes per day
    "Customer_Satisfaction": np.random.uniform(1, 5, size=n_customers),     # 1–5 rating
    "Referral_Count": np.random.poisson(lam=2, size=n_customers)
})

# -----------------------------
# Calculate correlation matrix
# -----------------------------
corr = data.corr()

# -----------------------------
# Plot with Seaborn
# -----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")  # presentation-ready

plt.figure(figsize=(8, 8))  # 8 inches * 64 dpi = 512 pixels
ax = sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="RdYlGn",
    cbar=True,
    square=True,
    linewidths=0.5
)

plt.title("Customer Engagement Correlation Matrix", fontsize=16, pad=20)

# -----------------------------
# Save chart with exact 512x512 pixels
# -----------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
