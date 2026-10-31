# AI-Use Note

## Audit trail

```text
# AI prompt: Load the cached CSV with relative paths and define ages 20-80 inclusive.
# Verified: Checked the actual CSV columns and boundary filter; rendered locally in a fresh R process.

# AI prompt: Count missing values for six key variables before complete-case filtering.
# Verified: Matched missing counts to separate base-R counts; percentages use the age-eligible N.

# AI prompt: Exclude missing Table 1 variables only and show the number removed.
# Verified: Checked complete-case N against base-R complete.cases on BMI, Age, and IncomeGroup.

# AI prompt: Summarize N and BMI/age mean (SD) by IncomeGroup and export the same table.
# Verified: Compared N, means, and sample SDs with independent base-R summaries; checked CSV read-back.
```

## What AI helped with

ChatGPT (Codex) helped draft the cohort filter, missingness checks, Table 1, and CSV export, and organize the planted-error audit.

## What I changed

I corrected the age boundaries, limited missing-data exclusions to the Table 1 variables, replaced variance with SD, used relative paths, and removed unsupported significance and causal claims.

## How the result was verified

The cohort counts, missingness, group sizes, means, and SDs were checked against separate base-R calculations using the repository CSV. The exported CSV was compared with the calculated table, and the rendered HTML was checked for the required content.