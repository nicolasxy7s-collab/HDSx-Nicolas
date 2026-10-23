# Visual Audit Note

## Plot Question

How does **mean BMI** compare across income groups and the available NHANES cycles for adults aged 20–80 in the prepared NHANES Health Equity classroom dataset?

## Issues Checked

| Issue in the flawed script | Category | Why it matters | Correction |
|---|---|---|---|
| The subtitle says “adults age 20–80,” but the summary does not filter `Age`. | Correctness | The plotted means include people outside the stated cohort. | Filter to ages 20–80 before calculating means. |
| The script keeps only the first and last cycles, while the subtitle claims BMI “climbed steadily across every NHANES cycle.” | Correctness | Two endpoints cannot establish what happened in the intervening cycles. | Show every available cycle in chronological order and remove the steady-rise claim. |
| The title calls the outcome “obesity,” although the code calculates mean `BMI`. | Correctness | Mean BMI is not an obesity prevalence measure. | Name the plotted statistic “mean BMI” in the title and y-axis label. |
| `scale_y_continuous(limits = c(24, 28))` starts the axis near the plotted values. | Design | Small differences appear much larger. | Include zero on the y-axis, following the Week 6 audit guidance. |
| “Low income drives” asserts a causal effect, and the plot does not say its means are unweighted. | Interpretation | An unweighted descriptive summary cannot establish causation or a population trend. | Use a descriptive title and state the unweighted, classroom-data limitation in the caption. |
| Missing values are excluded silently, and the plot provides no cell counts. | Bias and aggregation | Readers cannot see the exclusions or judge whether groups are sparse. | Disclose exclusions, calculate `n` for every cycle–income cell, and retain cells with `n >= 30`. In this CSV, all 33 corrected cells pass; the smallest has 1,089 records. |
| The first data-path option points to one analyst’s desktop. | Reproducibility | It could load a different local file when available. | Use repository-relative paths that work from the repository root or the submission folder. |

## Final Caption

Mean BMI (kg/m²) by income group across the available NHANES cycles in the prepared NHANES Health Equity classroom CSV, among adults aged 20–80. Values are unweighted arithmetic means; records missing BMI, income group, or cycle were excluded, and only cycle–income cells with at least 30 records are shown. Lines connect observed cycle summaries; this descriptive classroom figure does not estimate population trends, obesity prevalence, or causal effects of income.

## AI-Use Check

AI assisted with the audit wording, caption, and revised R code. The column names and group counts were checked against the supplied CSV; the revised R plot code ran and its exported image was inspected.

## Sources

- [Week 6 worked example](https://ehsanx.github.io/HDSx/weeks/week06-visualization/viz03-worked-example.html)
- [Week 6 visual-audit studio](https://ehsanx.github.io/HDSx/weeks/week06-visualization/viz06-studio-visual-audit.html)
- [Assignment 5 walkthrough](https://ehsanx.github.io/HDSx/weeks/week06-visualization/viz07-assignment-a5-and-reference.html)
- [Flawed plot script](https://github.com/nicolasxy7s-collab/HDSx-Nicolas/blob/main/assignments/assignment05-visualization/flawed-plot-code.R)