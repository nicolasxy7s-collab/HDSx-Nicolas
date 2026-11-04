# Dashboard Adaptation Note

## Audience

A public-health analyst preparing a short classroom briefing on descriptive BMI patterns in the prepared NHANES Health Equity dataset.

## Dashboard Question

Among included adults aged 20-80, how does average BMI vary across NHANES cycles for the selected income group?

## Control And Visualization

- Control or interaction: `selected_income`, with values `"Low Income (<1.3)"`, `"Middle Income"`, and `"High Income (>3.5)"`. The selected value is changed in the source before rendering; the HTML is static.
- Visualization affected: a line chart of mean BMI by NHANES cycle, accompanied by a table of cycle-specific counts and means.
- What changes when the control changes: rendering again updates the selected-group output, table values, chart title, and plotted means.

## Before And After

| Original text | Revised text | Why the revision helps |
|---|---|---|
| For the selected income group, the table and figure describe the mean BMI pattern across available NHANES cycles in the prepared classroom dataset. The dashboard should help the audience ask better questions about pattern, timing, and context rather than treat the line as a causal explanation. | Each point is the average BMI of included adults aged 20-80 in the selected income group for one NHANES cycle; the table shows how many records contributed. These unweighted classroom summaries describe the included records and do not show that income caused BMI to change or that the pattern applies to all US adults.<br><br>The prepared dataset moves directly from the 2017-2018 cycle to the 2021-2023 cycle, with no intervening cycle included. Although the 2021-2023 label spans three calendar years, it represents approximately two years of collection, from August 2021 to August 2023 ([CDC documentation](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/overviewbrief.aspx?Cycle=2021-2023)). Cycle labels are equally spaced rather than positioned by elapsed time; the connecting line does not show intervening annual measurements or an annual rate of change. Each cycle summarizes a different sample of adults, rather than changes in the same individuals. The vertical scale adjusts to the selected group, so compare table values rather than apparent heights or slopes across group settings. No uncertainty intervals or statistical tests are shown. | The revision explains the displayed summaries, distinguishes the cycle gap from the approximately two-year collection period, and clarifies the limits of visual comparisons. |

All four R chunks remained unchanged. Student-facing starter instructions were removed from the displayed dashboard.

## Test Result

On 2026-11-03, I rendered the dashboard in a fresh GitHub Codespace using VS Code’s Quarto Render command with HTML selected, R 4.6.1, and Quarto 1.10.19. Low- and middle-income outputs each contained 11 cycles, with 15,293 and 19,228 included records respectively; counts and means matched separate base-R checks, and the table, chart title, and plotted values updated correctly. Low income was restored, and the final revised dashboard rendered successfully with the same numerical results.

## Limitation

These unweighted classroom summaries describe only the included records and cannot establish causal effects of income on BMI or represent the US adult population.

## Privacy Check

I checked that the dashboard and preview displayed aggregate counts and means without participant records, credentials, or private links. The smallest cycle count in the two tested settings was 1,089, and the interpretation made no small-cell, causal, or national-population claims.