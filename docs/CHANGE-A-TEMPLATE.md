# How to change a template

Every Doc and Sheet that `discovery-setup` creates comes from a template: an ordinary Excel or Word file in [`templates-source/discovery-setup/`](../templates-source/discovery-setup/). You can improve one with a browser and Excel, Word or Google Docs/Sheets. No git, no code.

## 1. Download the template

Open the [templates folder](../templates-source/discovery-setup/), click the file (for example `raid-log.xlsx`), then click **Download raw file** (the download icon on the right).

## 2. Edit it

Open it in Excel, Word, Google Sheets or Google Docs and make your change.

**Sheets (.xlsx)** carry over:

- tabs, in order
- column names in row 1, starting in A1, with no empty columns between them
- column widths
- a frozen header row (View → Freeze → 1 row)
- the header row's bold text and background colour
- dropdowns: Data → Data validation → **List of items**, with the values typed in (not a range of cells)
- fixed text in the rows below the header, such as section names in the Context Canvas

Not supported yet: formulas, merged cells, conditional formatting, frozen columns. If your file uses them, the check in step 5 tells you exactly where.

**Docs (.docx)** carry over headings (use the Heading 1, 2, 3 styles), paragraphs, bold and italic text, bullet and numbered lists, and tables. Images are not supported.

Keep it a template: section names, column names, guidance. Never put client information in it.

## 3. Save it under the same name

- Excel or Word: save as `.xlsx` or `.docx`.
- Google Sheets or Docs: **File → Download → Microsoft Excel (.xlsx)** or **Microsoft Word (.docx)**.

Keep the file name exactly as it was, for example `raid-log.xlsx`. That's how the skill knows which file the template is for.

## 4. Upload it as a proposal

1. Open the [templates folder](../templates-source/discovery-setup/) on GitHub.
2. Click **Add file → Upload files** and drop your file in.
3. Under the upload, write one line about what you changed and why, for example "RAID Log: add Due date column, we track mitigation deadlines".
4. Choose **Create a new branch for this commit and start a pull request**, then **Propose changes**, then **Create pull request**.

If you don't have write access to the repository, GitHub makes a copy (a fork) for you automatically. The steps are the same.

## 5. See how the skill will build it

On the pull request, open **Checks → Templates**. The summary shows each template the way the skill will build it: tabs, columns and dropdown values for Sheets, headings for Docs.

- A green check means your template can be built as is.
- A red cross lists what can't be carried over, file by file. Fix it, upload the file again to the same pull request, and the check runs again.

## 6. What happens next

A maintainer reviews the change and merges it. GitHub then regenerates the files the skill reads, and every BA gets the new template with the next plugin update.

## Want a new file in the Discovery folder?

That's a change to the folder structure, not only a template. Open an issue describing the file, which folder it belongs in, and why every Discovery needs it. If it's agreed, the maintainer adds it to the structure and you can upload its template the same way.
