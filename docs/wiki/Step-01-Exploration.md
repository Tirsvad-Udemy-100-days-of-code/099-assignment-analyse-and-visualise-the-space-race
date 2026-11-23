**English** · [Dansk](Step-01-Exploration-da) · [Bahasa Malaysia](Step-01-Exploration-ms)

# Step 1: Preliminary data exploration

![Step 1: Preliminary data exploration](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/01-preliminary-data-exploration.png)

## What the step does

The notebook loads the file and asks the first questions: how many rows and columns, what are the columns called, and are there missing values or duplicates?

## What was gained

- The file has 4,324 rows and 9 columns, two of which only hold a row index.
- `Price` is the only column with missing values (3,360 of 4,324), so most launches have no published price.
- One row is an exact duplicate. Looking before changing anything shows what the cleaning step must do.

## Code in `src/space_race/`

`load_missions`, `explore`
