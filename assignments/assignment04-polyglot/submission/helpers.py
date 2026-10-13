from pathlib import Path
import pandas as pd


def load_and_preview(path, n_rows=5):
    """Load a CSV, print its shape, and return the first rows."""
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Could not find file: {csv_path}")

    data = pd.read_csv(csv_path)
    print(f"Loaded {data.shape[0]} rows and {data.shape[1]} columns")
    return data.head(n_rows)

# AI prompt: In helpers.py, translate my R summarise_mean_sd function into a reusable Python helper. Use it to summarize BMI by IncomeGroup and Gender, round the mean and standard deviation to two decimal places, and order the income groups High, Middle, then Low.
# Verified: I called the helper from the notebook and compared its output with r_function_summary. The missing-value exclusions, group counts, rounded means, sample standard deviations, and row order matched.

def summarise_mean_sd(data, value, group1, group2, group1_order=None):
    """Summarize a numeric column by two grouping columns."""
    complete_cases = data.dropna(subset=[value, group1, group2])
    summary = (
        complete_cases.groupby([group1, group2], as_index=False, observed=True)
        .agg(
            n=(value, "size"),
            mean_value=(value, "mean"),
            sd_value=(value, "std"),
        )
        .round({"mean_value": 2, "sd_value": 2})
    )

    order = (
        {level: index for index, level in enumerate(group1_order)}
        if group1_order is not None
        else None
    )
    return summary.sort_values(
        [group1, group2],
        key=lambda column: column.map(order)
        if column.name == group1 and order is not None
        else column,
        ignore_index=True,
    )
