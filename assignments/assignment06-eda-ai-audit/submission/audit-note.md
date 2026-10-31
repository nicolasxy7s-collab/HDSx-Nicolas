# Table 1 Audit Note

## Cohort

The intended cohort is recorded ages 20-80, inclusive. The corrected file uses `filter(Age >= 20, Age <= 80)`, then complete cases for BMI, age, and IncomeGroup only.

## Missingness

The corrected analysis reports missing counts and percentages for BMI, Age, IncomeGroup, Gender, Race, and Cycle before excluding incomplete records. The denominator is the age-eligible cohort. Only the three Table 1 variables determine complete-case inclusion.

## Planted issues

Audited file: `assignments/assignment06-eda-ai-audit/planted-error-starter.qmd`.

| Issue | Category | Why it matters | Corrected approach |
|---|---|---|---|
| The prose includes ages 20 and 80, but the code uses `Age > 20, Age < 80`. | Correctness | Both boundary ages are excluded despite the stated cohort. | Use `Age >= 20, Age <= 80` and report the cohort flow. |
| `na.omit()` operates on every column. | Correctness | Missing education, marital status, or other unused variables can remove otherwise eligible Table 1 records. | Filter missing BMI, Age, and IncomeGroup only, after reporting missingness. |
| There is no missingness table or count of missing-data exclusions. | Correctness | Readers cannot identify the denominators or assess selection due to missing data. | Report missing N and percent in the age-eligible cohort, then the number of distinct records excluded. |
| Both columns labeled mean (SD) use `var()` for the parenthetical statistic. | Correctness | Variance is in squared units and is not the promised standard deviation. | Use `sd(BMI)` and `sd(Age)` after complete-case filtering; keep mean (SD) labels. |
| The candidate list prioritizes `C:/Users/analyst/Documents/nhanes_equity_v6.csv`. | Reproducibility | Although relative fallbacks exist, an existing local file could silently replace the repository snapshot on another machine. | Remove the machine-specific option and resolve the cached CSV through relative repository paths. |
| The loading comment claims a fresh NHANES download last week. | Stewardship | The code reads a local CSV and does not establish that date, access method, or provenance. | Identify the prepared classroom snapshot derived from CDC/NCHS public-use NHANES and cached in the workspace. |
| The interpretation declares statistical significance. | Interpretation | No hypothesis test or uncertainty analysis is performed. | Describe observed sample means without a significance claim. |
| The interpretation says income determines BMI. | Interpretation | A descriptive grouped table cannot establish causation or account for confounding. | State that the observed comparison is non-causal and limited to retained classroom records. |
| Removing every incomplete row is presented as making results complete and publication-ready. | Interpretation | Complete-case selection can bias the sample; deleting rows establishes neither representativeness nor publication readiness. | Acknowledge selection from missingness and state that this unweighted exercise does not support national population estimates. |

## AI-use check

ChatGPT (Codex) helped inspect the actual starter, draft corrections, and organize the audit. The listed problems were checked against the starter's code and prose. The corrected analysis was run on the repository CSV using relative paths, with separate base-R checks of counts and summary statistics.
