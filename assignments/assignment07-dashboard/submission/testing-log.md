# Testing Log

- **2026-11-03:** Tested the dashboard in a fresh GitHub Codespace using VS Code’s Quarto Render command with HTML selected. The render successfully created `dashboard.html`, using R 4.6.1 and Quarto 1.10.19.
- **Control check:** Tested `"Low Income (<1.3)"` and `"Middle Income"`. Both outputs contained 11 cycles, with 15,293 and 19,228 included records respectively. The table values, chart title, and plotted points updated, while the caption, Interpretation, and Limitation remained present. Low income was restored and rendered again for the final version.
- **Warnings or errors:** None appeared in the render output. The editor’s Problems panel reported “Do not use empty rulesets,” a CSS warning; the HTML was created successfully.