# AI-Use Note

## Audit trail

**Data-loading chunk**

```text
# AI prompt: "Load the classroom CSV with repository-relative paths and check the variables needed for the BMI audit."
# Verified: Column names were checked against the supplied CSV; this R code ran locally.
```

**Summary, plot, and export chunk**

```text
# AI prompt: "Revise the flawed plot using all available NHANES cycles and adults aged 20–80. Exclude missing values, calculate each income-group-by-cycle cell count and unweighted mean BMI, retain cells with n >= 30, use a y-axis that includes zero, write descriptive labels and a caption covering the source, exclusions, and limitations, and export corrected-plot.png."
# Verified: The R code produced 33 cells, all with n >= 1,089. The zero-based plot and exported PNG were inspected.
```

## What AI helped with

I used ChatGPT to review the Week 6 guidance and the flawed R script, then help drafting the visual audit note, Quarto code, and caption. It helped write the relative-path setup, descriptive BMI summary and plot, and limitation-aware labels.

## What I changed

I replaced the starter’s desktop-specific path and endpoint-only comparison, applied the stated ages 20–80 restriction, and revised the axis, title, and caption to match the statistic and its limitations. I also moved the AI prompt and verification lines inside their R chunks after they appeared as headings in the first HTML render.

## How I verified the result

I checked the column names against the supplied CSV and confirmed that the revised summary has 33 income-by-cycle cells, each with at least 1,089 records. I inspected the exported PNG and rendered HTML for the zero-based axis, descriptive labels, and caption, and checked the interpretation against the Week 6 guidance.