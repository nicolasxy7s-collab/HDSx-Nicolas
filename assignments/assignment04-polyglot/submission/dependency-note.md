# Dependency Note

The R analysis in `polyglot-parity.qmd` loads `tidyverse` and uses `dplyr` for filtering, grouping, and summarising the data. It reads the CSV with `read.csv()`, which is included with R.

The Python notebook and `helpers.py` use `pandas` to load and summarise the same data. The helper also uses `pathlib`, which is included with Python.

The repository’s `.devcontainer/requirements.txt` already lists `pandas` and `jupyter`.