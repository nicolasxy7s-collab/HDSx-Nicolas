# AI-Use Note

## Audit trail
AI prompt: Create a Quarto document with an example A4 title, a placeholder for my name, and a simple R code chunk that I will modify to load data. Place it in assignments/assignment04-polyglot/submission. please use examples/nhanes-equity/data/nhanes_equity_v6.csv
Verified: I confirmed the Quarto file is in the requested submission folder, contains an A4 title and name placeholder, and renders successfully. The AI did use the relavant location correctly.

AI prompt: Under Pipeline 1, use the nhanes dataframe, remove rows with missing BMI, IncomeGroup, or Gender, then calculate sample size, mean BMI, and standard deviation of BMI by IncomeGroup and Gender. Sort and print the summary table.
Verified: I checked that rows with missing values in those three columns were excluded, confirmed the group counts, means, and standard deviations against the filtered data, and checked the table’s sort order.

AI prompt: Arrange the summary table in the order High Income, Middle Income, and Low Income.
Verified: I checked that the printed table shows the income groups in that order and that the summary values stayed the same.

AI prompt: Can you import the nhanes dataset in my Jupyter notebook using Python and pandas
Verified: I ran the import cell, and checked that the dataframe loaded with the expected rows and columns.

AI prompt: Write code to show how many rows and columns are in the NHANES dataset.
Verified: I ran the code and checked that the reported dimensions match the dataframe’s shape.

AI prompt: In a new Jupyter cell, translate my R Pipeline 1 code into Python. Exclude missing BMI, IncomeGroup, and Gender values; calculate n, mean_BMI, and sd_BMI by IncomeGroup and Gender; then sort High Income, Middle Income, and Low Income, with Gender within each group.
Verified: I compared the Python output with the R summary table. The group counts, means, and sample standard deviations matched, and the rows appeared in the requested order.

AI prompt: In helpers.py, translate my R summarise_mean_sd function into a reusable Python helper. Use it to summarize BMI by IncomeGroup and Gender, round the mean and standard deviation to two decimal places, and order the income groups High, Middle, then Low.
Verified: I called the helper from the notebook and compared its output with r_function_summary. The missing-value exclusions, group counts, rounded means, sample standard deviations, and row order matched.

AI prompt: Call the new helper from helpers.py once in translation.ipynb.
Verified: I ran the notebook cell, confirmed it calls the helper once, and checked that its output matches the R function summary.

## What AI helped with
AI helped set up the Quarto assignment and load the NHANES data in R and Python. It helped translate the R summary pipeline into pandas and create a reusable Python helper. It also helped organize the income-group order and document the parity checks.

## What I changed
I reviewed the translated workflow and kept the Python analysis in separate, step-by-step notebook cells. I added the missing-BMI check and completed the parity documentation with the group labels, counts, rounded means, and standard deviations.

## How I verified the result
I checked the dataset dimensions and confirmed both languages read 105,626 rows and 18 columns. I verified that filtering missing BMI, IncomeGroup, or Gender left 87,647 rows and that both summaries contained six groups. I compared the group labels, counts, rounded BMI means, and rounded sample standard deviations, and confirmed they matched in the requested order.