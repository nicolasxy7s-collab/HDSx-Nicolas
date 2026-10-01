# AI-Use Note

## Audit trail
# AI prompt: 
Using the R dataset `nhanes`, create an analysis-ready summary table called `analysis_ready_table` using at least three `dplyr` verbs and the native pipe `|>`.Keep participants older than 65, excluding rows with missing BMI or Gender. Group by Gender, calculate the number of participants and mean BMI, round mean BMI to one decimal place, and sort by participant count from largest to smallest. Return an ungrouped table and display it.
# Verified: 
Checked column names against names(nhanes) and compared mean BMI values with summary().

## What AI helped with 
AI helped generate a pipeline using filter(), group_by(), summarise(), mutate(), and arrange() to produce participant counts and mean BMI by Gender for participants older than 65.


## What I changed 
The pipeline shown retains the AI-generated structure. My prompt specified the age restriction, missing-value exclusions, grouping variable, summary statistics, rounding, and sorting.


## How I verified the result 
I checked that the column names used in the pipeline matched names(nhanes) and compared the calculated means with summary() output.

# AI-Use Note

## Audit trail
## AI prompt: 
Write a custom R function named `mean_sd_with_n()` that accepts a numeric vector `x` and returns a one-row tibble with three columns:
- `n`: the number of nonmissing values.
- `mean`: the mean, excluding missing values.
- `sd`: the sample standard deviation, excluding missing values.
Use `sum(!is.na(x))`, `mean(x, na.rm = TRUE)`, and `sd(x, na.rm = TRUE)`. Assume tidyverse is already loaded. Demonstrate the function using `nhanes$BMI`, then test it with `c(1, 2, 3, NA)`, which should return n = 3, mean = 2, and sd = 1.

## What AI helped with 
ChatGPT/Codex suggested a custom function that calculates the nonmissing count, mean, and sample standard deviation. It also provided an example using `nhanes$BMI` and a small test with known expected results.

## What I changed 
My original function, `mean_with_n()`, returned only the count and mean. The AI-suggested revision adds standard deviation and renames the function `mean_sd_with_n()`; I have not documented any further manual edits.

## How I verified the result 
I checked that `BMI` exists in `names(nhanes)`. The test `mean_sd_with_n(c(1, 2, 3, NA))` in `analysis-note.qmd` returned n = 3, mean = 2, and sd = 1 in the rendered report.