# analysis.py
# Author contact: 22f3000808@ds.study.iitm.ac.in

import marimo as mo

app = mo.App()

# --- Cell 1: Imports & seed ---------------------------------------------------
@app.cell
def __():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    rng = np.random.default_rng(42)  # deterministic base RNG for reproducibility
    return np, pd, plt, rng
# Notes:
# - Exposes np, pd, plt, rng to downstream cells.
# - Downstream cells depend on these names.

# --- Cell 2: UI widgets (user controls) ---------------------------------------
@app.cell
def __():
    # Interactive controls
    n_slider = mo.ui.slider(50, 1000, value=300, label="Sample size (n)")
    noise_slider = mo.ui.slider(0.0, 3.0, value=1.0, step=0.1, label="Noise scale σ")

    controls = mo.hstack([n_slider, noise_slider], justify="start", gap="1rem")
    controls
    return n_slider, noise_slider
# Notes:
# - Widgets are reactive sources.
# - Any cell that references n_slider.value or noise_slider.value re-runs when they change.

# --- Cell 3: Data generation (depends on widgets + RNG) -----------------------
@app.cell
def __(np, pd, rng, n_slider, noise_slider):
    """
    Generates a synthetic linear dataset with adjustable sample size and noise.
    Data flow:
      n_slider.value, noise_slider.value -> (n, sigma) -> df (x, y)
    """
    n = int(n_slider.value)
    sigma = float(noise_slider.value)

    # True model: y = a*x + b + ε
    a, b = 2.0, 5.0
    x = np.linspace(0, 10, n)
    eps = rng.normal(0.0, sigma, size=n)
    y = a * x + b + eps

    df = pd.DataFrame({"x": x, "y": y})
    df
    return a, b, df
# Notes:
# - Downstream analysis (corr, regression, plots) depends on df.

# --- Cell 4: Analysis (correlation & simple linear regression) ----------------
@app.cell
def __(np, df):
    """
    Computes Pearson correlation and OLS via polyfit.
    Data flow:
      df -> (r, slope_hat, intercept_hat)
    """
    r = df["x"].corr(df["y"])
    slope_hat, intercept_hat = np.polyfit(df["x"], df["y"], deg=1)
    r, slope_hat, intercept_hat
    return r, slope_hat, intercept_hat
# Notes:
# - Updates automatically when df changes.

# --- Cell 5: Visualization (depends on df and regression params) --------------
@app.cell
def __(plt, df, slope_hat, intercept_hat):
    """
    Scatter plot + fitted line.
    Data flow:
      df, slope_hat, intercept_hat -> figure
    """
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(df["x"], df["y"], alpha=0.6, label="observations")
    line = slope_hat * df["x"] + intercept_hat
    ax.plot(df["x"], line, linewidth=2, label="OLS fit")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Relationship between x and y (interactive)")
    ax.legend()
    fig
    return fig, ax
# Notes:
# - Re-renders when df or coefficients change.

# --- Cell 6: Dynamic Markdown summary (depends on widgets + analysis) ---------
@app.cell
def __(mo, n_slider, noise_slider, r, slope_hat, intercept_hat):
    """
    Dynamic narrative that updates with widget values and analysis outputs.
    Data flow:
      (n_slider.value, noise_slider.value, r, slope_hat, intercept_hat) -> markdown
    """
    strength = (
        "very strong" if abs(r) > 0.9 else
        "strong" if abs(r) > 0.7 else
        "moderate" if abs(r) > 0.5 else
        "weak" if abs(r) > 0.3 else
        "very weak"
    )
    mo.md(f"""
# Interactive Analysis Summary

- **Sample size (n)**: `{int(n_slider.value)}`
- **Noise (σ)**: `{noise_slider.value:.2f}`

**Pearson correlation**: `{r:.3f}` — interpreted as **{strength}** linear relationship.

**Estimated model** (OLS):  
\\[
\\hat y = {slope_hat:.3f}\\,x + {intercept_hat:.3f}
\\]

**Algorithmic complexity note:**  
For a single-pass correlation and line fit, computation is approximately \\(\\mathcal{{O}}(n)\\) in the number of samples.
""")
# Notes:
# - Demonstrates dynamic Markdown and embedded math reacting to widget state.

# --- Cell 7: “How to use” panel ----------------------------------------------
@app.cell
def __(mo):
    mo.md("""
> **How to interact:**  
> - Drag the sliders to adjust **sample size** and **noise**.  
> - The dataset, regression, plot, and this narrative update automatically.  
> - This notebook is fully reactive; cells declare dependencies via variables they read.
""")

# --- Entrypoint ----------------------------------------------------------------
if __name__ == "__main__":
    # Run with: marimo run analysis.py
    # Or open the editor: marimo edit analysis.py
    app.run()
